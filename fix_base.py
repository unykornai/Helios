"""Apply Ask Helios nav link + floating AI widget to base.html"""
import pathlib

path = pathlib.Path(r"C:\Users\Kevan\helios-os\templates\base.html")
content = path.read_text(encoding="utf-8")

# ── 1. Add 'Ask Helios' nav link before Treasury ──────────────────
old_nav = '<a href="/treasury">Treasury</a>'
new_nav = '<a href="/ask" class="nav-ask">Ask Helios</a>\n                <a href="/treasury">Treasury</a>'
content = content.replace(old_nav, new_nav, 1)

# ── 2. Add floating AI agent widget before {% block scripts %} ────
fab_widget = """    <!-- FLOATING AI AGENT -->
    <div class="helios-fab" id="heliosFab" onclick="window.location.href='/ask'" title="Ask Helios AI Advisor">
        <div class="fab-glow"></div>
        <div class="fab-ring"></div>
        <div class="fab-core">&#9728;&#65039;</div>
        <div class="fab-label">Ask Helios</div>
    </div>
    <style>
    .helios-fab{position:fixed;bottom:1.5rem;right:1.5rem;z-index:9999;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:.3rem;transition:all .3s}
    .helios-fab:hover{transform:translateY(-3px)}
    .helios-fab:hover .fab-core{border-color:rgba(41,151,255,0.5);box-shadow:0 0 30px rgba(41,151,255,0.2)}
    .helios-fab:hover .fab-glow{opacity:.8;transform:scale(1.15)}
    .fab-glow{position:absolute;width:70px;height:70px;border-radius:50%;background:radial-gradient(circle,rgba(41,151,255,0.12) 0%,transparent 70%);animation:fab-breathe 3s ease-in-out infinite;top:-5px;left:50%;transform:translateX(-50%)}
    @keyframes fab-breathe{0%,100%{opacity:.3;transform:translateX(-50%) scale(.9)}50%{opacity:.6;transform:translateX(-50%) scale(1.1)}}
    .fab-ring{position:absolute;width:58px;height:58px;border-radius:50%;border:1px solid rgba(41,151,255,0.12);animation:fab-spin 15s linear infinite;top:1px;left:50%;transform:translateX(-50%)}
    .fab-ring::before{content:'';position:absolute;top:-2px;left:50%;width:4px;height:4px;border-radius:50%;background:var(--primary);box-shadow:0 0 8px var(--primary)}
    @keyframes fab-spin{to{transform:translateX(-50%) rotate(360deg)}}
    .fab-core{width:56px;height:56px;border-radius:50%;background:rgba(10,10,12,0.85);backdrop-filter:blur(20px);border:1px solid rgba(41,151,255,0.15);display:flex;align-items:center;justify-content:center;font-size:1.4rem;transition:all .3s;position:relative;z-index:2}
    .fab-label{font-size:.6rem;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:.08em;opacity:.7;transition:opacity .3s}
    .helios-fab:hover .fab-label{opacity:1;color:var(--primary)}
    @media(max-width:768px){.helios-fab{bottom:1rem;right:1rem}.fab-core{width:48px;height:48px;font-size:1.2rem}.fab-ring{width:50px;height:50px}.fab-glow{width:60px;height:60px}.fab-label{display:none}}
    </style>

"""

old_scripts = "    {% block scripts %}{% endblock %}"
new_scripts = fab_widget + "    {% block scripts %}{% endblock %}"
content = content.replace(old_scripts, new_scripts, 1)

path.write_text(content, encoding="utf-8")

# Verify
final = path.read_text(encoding="utf-8")
print(f"OK  base.html updated ({len(final)} chars)")
print(f"  nav-ask link:  {'nav-ask' in final}")
print(f"  helios-fab:    {'helios-fab' in final}")
print(f"  fab-core:      {'fab-core' in final}")
print(f"  fab-breathe:   {'fab-breathe' in final}")
