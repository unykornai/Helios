"""
Helios Voice — ElevenLabs TTS Integration
──────────────────────────────────────────
Ask Helios speaks. Plain English. Warm and human.
Every answer can be heard, not just read.
"""

import io
import base64
import hashlib
import os
from pathlib import Path
from config import HeliosConfig, BASE_DIR


class HeliosVoice:
    """
    Text-to-speech engine powered by ElevenLabs.
    Converts Ask Helios answers into natural speech.
    Caches audio to avoid redundant API calls.
    """

    CACHE_DIR = Path(BASE_DIR) / "data" / "voice_cache"

    def __init__(self):
        self.api_key = HeliosConfig.ELEVENLABS_API_KEY
        self.voice_id = HeliosConfig.ELEVENLABS_VOICE_ID
        self.model = HeliosConfig.ELEVENLABS_MODEL
        self.stability = HeliosConfig.ELEVENLABS_STABILITY
        self.similarity = HeliosConfig.ELEVENLABS_SIMILARITY
        self.available = bool(self.api_key)

        # Ensure cache directory exists
        self.CACHE_DIR.mkdir(parents=True, exist_ok=True)

    # ─── Main TTS ──────────────────────────────────────────────────────

    def speak(self, text: str, use_cache: bool = True, voice_id: str = None) -> dict:
        """
        Convert text to speech audio.
        Returns base64-encoded MP3 audio data.
        Optional voice_id overrides the default voice.
        """
        # Allow per-request voice override
        if voice_id:
            self._override_voice = voice_id
        else:
            self._override_voice = None
        if not self.available:
            return {
                "audio": None,
                "error": "Voice service not configured",
                "available": False
            }

        # Clean text for speech (strip markdown-like formatting)
        clean_text = self._clean_for_speech(text)

        if not clean_text or len(clean_text.strip()) < 2:
            return {
                "audio": None,
                "error": "Text too short to speak",
                "available": True
            }

        # Check cache first
        cache_key = self._cache_key(clean_text)
        if use_cache:
            cached = self._get_cached(cache_key)
            if cached:
                return {
                    "audio": cached,
                    "format": "mp3",
                    "source": "cache",
                    "available": True
                }

        # Call ElevenLabs API
        try:
            audio_data = self._call_elevenlabs(clean_text)

            # Cache the result
            if use_cache and audio_data:
                self._save_cache(cache_key, audio_data)

            # Return base64-encoded audio
            audio_b64 = base64.b64encode(audio_data).decode("utf-8")

            return {
                "audio": audio_b64,
                "format": "mp3",
                "source": "elevenlabs",
                "available": True
            }

        except Exception as e:
            return {
                "audio": None,
                "error": f"Voice generation failed: {str(e)}",
                "available": True
            }

    def get_voices(self) -> dict:
        """List available ElevenLabs voices."""
        if not self.available:
            return {"voices": [], "error": "Voice service not configured"}

        try:
            import requests

            response = requests.get(
                "https://api.elevenlabs.io/v1/voices",
                headers={"xi-api-key": self.api_key},
                timeout=10
            )
            response.raise_for_status()
            data = response.json()

            voices = [
                {
                    "voice_id": v["voice_id"],
                    "name": v["name"],
                    "category": v.get("category", "unknown"),
                    "preview_url": v.get("preview_url")
                }
                for v in data.get("voices", [])
            ]

            return {
                "voices": voices,
                "current": self.voice_id,
                "total": len(voices)
            }

        except Exception as e:
            return {"voices": [], "error": str(e)}

    def get_status(self) -> dict:
        """Check voice service health and usage."""
        if not self.available:
            return {
                "status": "not_configured",
                "message": "Add HELIOS_ELEVENLABS_API_KEY to .env"
            }

        try:
            import requests

            response = requests.get(
                "https://api.elevenlabs.io/v1/user/subscription",
                headers={"xi-api-key": self.api_key},
                timeout=10
            )
            response.raise_for_status()
            data = response.json()

            return {
                "status": "active",
                "tier": data.get("tier", "unknown"),
                "character_count": data.get("character_count", 0),
                "character_limit": data.get("character_limit", 0),
                "remaining": data.get("character_limit", 0) - data.get("character_count", 0),
                "voice_id": self.voice_id
            }

        except Exception as e:
            return {
                "status": "error",
                "message": str(e)
            }

    # ─── ElevenLabs API Call ───────────────────────────────────────────

    def _call_elevenlabs(self, text: str) -> bytes:
        """Call the ElevenLabs TTS API and return raw audio bytes."""
        import requests

        active_voice = getattr(self, '_override_voice', None) or self.voice_id
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{active_voice}"

        headers = {
            "xi-api-key": self.api_key,
            "Content-Type": "application/json",
            "Accept": "audio/mpeg"
        }

        payload = {
            "text": text,
            "model_id": self.model,
            "voice_settings": {
                "stability": self.stability,
                "similarity_boost": self.similarity
            }
        }

        response = requests.post(url, json=payload, headers=headers, timeout=30)
        response.raise_for_status()

        return response.content

    # ─── Text Cleaning ─────────────────────────────────────────────────

    def _clean_for_speech(self, text: str) -> str:
        """Clean text for natural speech output."""
        import re

        # Remove bullet points and list markers
        text = re.sub(r'[•\-\*]\s*', '', text)
        # Remove markdown-style formatting
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
        text = re.sub(r'\*(.+?)\*', r'\1', text)
        # Remove numbered list markers like "1." at start of lines
        text = re.sub(r'^\d+\.\s*', '', text, flags=re.MULTILINE)
        # Collapse multiple newlines into pauses
        text = re.sub(r'\n{2,}', '. ', text)
        text = re.sub(r'\n', ' ', text)
        # Remove excessive whitespace
        text = re.sub(r'\s+', ' ', text).strip()

        # Truncate to ElevenLabs limit (5000 chars)
        if len(text) > 4800:
            text = text[:4800] + "... That's the key information."

        return text

    # ─── Cache Management ──────────────────────────────────────────────

    def _cache_key(self, text: str) -> str:
        """Generate a cache key from text + voice settings."""
        active_voice = getattr(self, '_override_voice', None) or self.voice_id
        content = f"{text}:{active_voice}:{self.model}"
        return hashlib.md5(content.encode()).hexdigest()

    def _get_cached(self, key: str) -> str:
        """Retrieve cached audio as base64 string."""
        cache_file = self.CACHE_DIR / f"{key}.mp3"
        if cache_file.exists():
            audio_data = cache_file.read_bytes()
            return base64.b64encode(audio_data).decode("utf-8")
        return None

    def _save_cache(self, key: str, audio_data: bytes):
        """Save audio data to cache."""
        cache_file = self.CACHE_DIR / f"{key}.mp3"
        cache_file.write_bytes(audio_data)

    def clear_cache(self) -> dict:
        """Clear the voice cache directory."""
        count = 0
        for f in self.CACHE_DIR.glob("*.mp3"):
            f.unlink()
            count += 1
        return {"cleared": count, "message": f"Removed {count} cached audio files"}
