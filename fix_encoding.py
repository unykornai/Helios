"""
Phase 17: Fix UTF-8 mojibake across all Helios OS templates.

Root cause: UTF-8 bytes were double-encoded through a Windows-1252 (cp1252) layer.
Original UTF-8 bytes were misread as cp1252, then re-encoded as UTF-8.

Fix: iterate through text, find mojibake lead-byte characters, attempt
sloppy-cp1252 round-trip to recover original UTF-8 characters.
Uses a custom encoder that handles the 5 "undefined" cp1252 positions
(0x81, 0x8D, 0x8F, 0x90, 0x9D) as pass-through.
"""
import os
import glob

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')

# ── Build sloppy cp1252 encode/decode tables ───────────────────────────
# Standard cp1252 leaves 5 positions undefined. Many real-world encoders
# treat them as pass-through (U+0081 <-> 0x81, etc). Python's codec rejects
# them, so we build our own.

# Forward table: byte (0-255) -> Unicode code point (for decoding)
_FWD = {}
for b in range(256):
    try:
        _FWD[b] = bytes([b]).decode('cp1252')
    except UnicodeDecodeError:
        _FWD[b] = chr(b)  # Pass-through for undefined positions

# Reverse table: Unicode char -> byte value (for encoding)
_REV = {ch: b for b, ch in _FWD.items()}

# Build the set of characters that result from sloppy-cp1252-decoding
# UTF-8 continuation bytes (0x80-0xBF).
CONT_CHARS = set()
for byte_val in range(0x80, 0xC0):
    CONT_CHARS.add(_FWD[byte_val])


def sloppy_cp1252_encode(text):
    """Encode a Unicode string to bytes using sloppy cp1252 (with pass-through)."""
    result = bytearray()
    for ch in text:
        byte_val = _REV.get(ch)
        if byte_val is not None:
            result.append(byte_val)
        else:
            raise UnicodeEncodeError('sloppy-cp1252', ch, 0, 1, 'character not in sloppy cp1252')
    return bytes(result)


def fix_mojibake(text):
    """
    Iterate through text and fix mojibake sequences by attempting
    sloppy-cp1252 encode -> utf-8 decode round-trip.
    Returns (fixed_text, fix_count).
    """
    result = []
    fixes = 0
    i = 0
    n = len(text)

    while i < n:
        ch = text[i]
        code = ord(ch)
        fixed = False

        # 4-byte UTF-8 lead (0xF0-0xF4)
        if 0xF0 <= code <= 0xF4 and i + 3 < n:
            seq = text[i:i+4]
            if all(c in CONT_CHARS for c in seq[1:]):
                try:
                    raw = sloppy_cp1252_encode(seq)
                    recovered = raw.decode('utf-8')
                    result.append(recovered)
                    fixes += 1
                    i += 4
                    fixed = True
                except (UnicodeDecodeError, UnicodeEncodeError):
                    pass

        # 3-byte UTF-8 lead (0xE0-0xEF)
        if not fixed and 0xE0 <= code <= 0xEF and i + 2 < n:
            seq = text[i:i+3]
            if all(c in CONT_CHARS for c in seq[1:]):
                try:
                    raw = sloppy_cp1252_encode(seq)
                    recovered = raw.decode('utf-8')
                    result.append(recovered)
                    fixes += 1
                    i += 3
                    fixed = True
                except (UnicodeDecodeError, UnicodeEncodeError):
                    pass

        # 2-byte UTF-8 lead (0xC2-0xDF)
        if not fixed and 0xC2 <= code <= 0xDF and i + 1 < n:
            seq = text[i:i+2]
            if seq[1] in CONT_CHARS:
                try:
                    raw = sloppy_cp1252_encode(seq)
                    recovered = raw.decode('utf-8')
                    result.append(recovered)
                    fixes += 1
                    i += 2
                    fixed = True
                except (UnicodeDecodeError, UnicodeEncodeError):
                    pass

        if not fixed:
            result.append(ch)
            i += 1

    return ''.join(result), fixes


# ASCII chars that may have replaced smart-quote cp1252 chars
# Order matters: try right-quote first (more common in mojibake contexts)
QUOTE_SUBS = {
    '"': ['\u201d', '\u201c'],  # ASCII " -> try right then left double smart quotes
    "'": ['\u2019', '\u2018'],  # ASCII ' -> try right then left single smart quotes
}


def fix_partial_mojibake(text):
    """
    Fix mojibake where the last byte's smart quote was normalized to ASCII.
    E.g. a euro + ASCII-quote instead of smart-quote after a 3-byte lead.
    """
    result = []
    fixes = 0
    i = 0
    n = len(text)

    while i < n:
        ch = text[i]
        code = ord(ch)
        fixed = False

        # 3-byte lead where third char is an ASCII quote
        if 0xE0 <= code <= 0xEF and i + 2 < n:
            c2, c3 = text[i+1], text[i+2]
            if c2 in CONT_CHARS and c3 in QUOTE_SUBS:
                # Try substituting the ASCII quote with each smart-quote variant
                for smart_q in QUOTE_SUBS[c3]:
                    seq = ch + c2 + smart_q
                    try:
                        raw = sloppy_cp1252_encode(seq)
                        recovered = raw.decode('utf-8')
                        result.append(recovered)
                        fixes += 1
                        i += 3
                        fixed = True
                        break
                    except (UnicodeDecodeError, UnicodeEncodeError):
                        continue

        if not fixed:
            result.append(ch)
            i += 1

    return ''.join(result), fixes


def fix_file(filepath):
    """Fix all mojibake in a single template file. Returns count of fixes."""
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    original = text
    total_fixes = 0

    # Run up to 3 passes (in case of triple-encoding or nested artifacts)
    for _ in range(3):
        text, fixes = fix_mojibake(text)
        total_fixes += fixes
        if fixes == 0:
            break

    # Fix partial mojibake (smart quotes normalized to ASCII quotes)
    text, partial_fixes = fix_partial_mojibake(text)
    total_fixes += partial_fixes

    if text != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)

    return total_fixes


def main():
    templates = sorted(glob.glob(os.path.join(TEMPLATE_DIR, '*.html')))
    print(f"Scanning {len(templates)} template files...\n")

    grand_total = 0
    for fpath in templates:
        fname = os.path.basename(fpath)
        fixes = fix_file(fpath)
        if fixes > 0:
            print(f"  FIXED: {fname} ({fixes} replacements)")
            grand_total += fixes
        else:
            print(f"  CLEAN: {fname}")

    print(f"\n{'='*50}")
    print(f"Total fixes applied: {grand_total}")
    print(f"Files processed: {len(templates)}")
    print("Done.")


if __name__ == '__main__':
    main()
