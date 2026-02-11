"""
Phase 17 Part 3 — Sweet Spot $500, Spin Game, QR Sales, Urgency Everywhere
"""
import pathlib, re

ROOT = pathlib.Path(r"C:\Users\Kevan\helios-os\templates")

# ═══════════════════════════════════════════════════════════════════════
# 1. REBUILD ACTIVATE.HTML — $500 SWEET SPOT PSYCHOLOGY
# ═══════════════════════════════════════════════════════════════════════
print("═══ Rebuilding activate.html ═══")
activate_path = ROOT / "activate.html"

# Delete and recreate
activate_path.unlink(missing_ok=True)
activate_path.write_text(r'''{% extends "base.html" %}
{% block title %}Activate — Helios Protocol{% endblock %}
{% block og_title %}Activate Your Smart Contract — Helios Protocol{% endblock %}
{% block og_description %}Choose your contract level. Every dollar has a published destination. $500 is the founding sweet spot — maximum value per dollar with 10× token multiplier.{% endblock %}
{% block og_url %}/activate{% endblock %}

{% block head %}
<style>
/* ═══════════════════════════════════════════════════════════════════
   ACTIVATE PAGE — $500 SWEET SPOT PSYCHOLOGY
   ═══════════════════════════════════════════════════════════════════ */
.act-hero { text-align:center; padding:4rem 2rem 2rem; }
.act-hero h1 { font-size:2.2rem; font-weight:700; color:var(--gold); letter-spacing:.1em; margin-bottom:.5rem; }
.act-hero .act-sub { color:var(--text-muted); font-size:1.05rem; max-width:640px; margin:0 auto 1rem; line-height:1.7; }

/* Founding Window Banner */
.founding-strip {
    background:linear-gradient(90deg,rgba(251,191,36,.06),rgba(41,151,255,.06),rgba(251,191,36,.06));
    border:1px solid rgba(251,191,36,.2); border-radius:var(--radius);
    padding:.8rem 1.5rem; text-align:center; max-width:700px; margin:0 auto 2rem;
}
.founding-strip .fs-title { font-size:.72rem; text-transform:uppercase; letter-spacing:.12em; font-weight:700; color:var(--gold); margin-bottom:.3rem; font-family:'Inter',sans-serif; }
.founding-strip .fs-desc { font-size:.88rem; color:var(--text-muted); line-height:1.5; }
.founding-strip .fs-desc strong { color:var(--gold); }
.founding-strip .fs-multiplier {
    display:inline-block; background:rgba(251,191,36,.1); border:1px solid rgba(251,191,36,.3);
    padding:.15rem .6rem; border-radius:12px; font-size:.75rem; font-weight:700;
    color:var(--gold); margin-top:.4rem; animation:pulse-badge 2s ease-in-out infinite;
}
@keyframes pulse-badge { 0%,100%{box-shadow:0 0 0 0 rgba(251,191,36,.2)} 50%{box-shadow:0 0 12px 3px rgba(251,191,36,.1)} }

.act-section { max-width:1060px; margin:0 auto; padding:0 2rem 3rem; }
.act-section h2 { font-size:1.4rem; font-weight:600; color:var(--text); margin-bottom:.5rem; }
.act-section .section-desc { color:var(--text-muted); font-size:.95rem; line-height:1.7; margin-bottom:1.5rem; max-width:720px; }

/* ─── The Sweet Spot Hero (only $500) ─────────────────────────────── */
.sweet-spot-hero {
    position:relative; max-width:480px; margin:0 auto 2.5rem;
    background:var(--bg-card); border:2px solid var(--gold);
    border-radius:16px; padding:2rem 2rem 1.5rem; text-align:center;
    box-shadow:0 0 60px rgba(251,191,36,.08), 0 0 120px rgba(41,151,255,.04);
    overflow:hidden;
}
.sweet-spot-hero::before {
    content:''; position:absolute; top:0; left:0; right:0; height:3px;
    background:linear-gradient(90deg,transparent,var(--gold),transparent);
}
.sweet-spot-hero::after {
    content:'FOUNDING SWEET SPOT'; position:absolute; top:14px; right:-32px;
    background:var(--gold); color:var(--bg); font-size:.58rem; font-weight:800;
    padding:.15rem 2.5rem; transform:rotate(45deg); font-family:'Inter',sans-serif;
    letter-spacing:.06em; box-shadow:0 2px 8px rgba(0,0,0,.3);
}
.sweet-glow {
    position:absolute; top:-40px; left:50%; transform:translateX(-50%);
    width:200px; height:200px; border-radius:50%;
    background:radial-gradient(circle,rgba(251,191,36,.1) 0%,transparent 70%);
    animation:sweet-breathe 3s ease-in-out infinite; pointer-events:none;
}
@keyframes sweet-breathe { 0%,100%{opacity:.3;transform:translateX(-50%) scale(.9)} 50%{opacity:.7;transform:translateX(-50%) scale(1.1)} }
.sweet-badge-row { display:flex; justify-content:center; gap:.5rem; margin-bottom:.8rem; flex-wrap:wrap; }
.sweet-badge {
    font-size:.62rem; text-transform:uppercase; letter-spacing:.1em; font-weight:700;
    padding:.2rem .6rem; border-radius:12px; font-family:'Inter',sans-serif;
}
.sweet-badge.popular { background:rgba(251,191,36,.15); color:var(--gold); border:1px solid rgba(251,191,36,.3); }
.sweet-badge.value { background:rgba(52,211,153,.1); color:#34d399; border:1px solid rgba(52,211,153,.2); }
.sweet-name { font-size:.75rem; text-transform:uppercase; letter-spacing:.14em; color:var(--text-muted); font-weight:600; font-family:'Inter',sans-serif; margin-bottom:.2rem; }
.sweet-price { font-size:3.2rem; font-weight:800; color:var(--gold); font-family:'Inter',sans-serif; line-height:1; margin-bottom:.3rem; }
.sweet-mult { font-size:.95rem; color:var(--text-muted); margin-bottom:.8rem; }
.sweet-stats { list-style:none; padding:0; margin:0 0 .8rem; text-align:left; }
.sweet-stats li {
    padding:.4rem 0; border-bottom:1px solid rgba(36,40,51,.4);
    display:flex; justify-content:space-between; font-size:.85rem; color:var(--text-muted);
}
.sweet-stats li:last-child { border-bottom:none; }
.sweet-stats .stat-val { color:var(--gold); font-weight:700; font-family:'Inter',sans-serif; }
.sweet-social {
    font-size:.72rem; color:var(--text-muted); margin-bottom:1rem;
    padding:.5rem; background:rgba(41,151,255,.03); border-radius:8px;
    font-family:'Inter',sans-serif;
}
.sweet-social strong { color:var(--gold); }
.sweet-cta {
    display:block; width:100%; padding:.85rem 0;
    background:var(--gold); color:var(--bg); border:none; border-radius:var(--radius-sm);
    font-weight:700; font-size:1rem; font-family:'Inter',sans-serif;
    text-align:center; text-decoration:none; cursor:pointer; transition:all .25s;
    letter-spacing:.02em;
}
.sweet-cta:hover { opacity:.9; transform:translateY(-1px); box-shadow:0 6px 20px rgba(251,191,36,.2); }
.sweet-savings { font-size:.7rem; color:var(--gold); margin-top:.5rem; font-weight:600; font-family:'Inter',sans-serif; }

/* ─── Other Tiers Grid ────────────────────────────────────────────── */
.other-tiers-label {
    text-align:center; font-size:.72rem; text-transform:uppercase;
    letter-spacing:.12em; color:var(--text-muted); font-weight:600;
    margin-bottom:1rem; font-family:'Inter',sans-serif;
}
.act-tiers {
    display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr));
    gap:1rem; margin-bottom:3rem;
}
.act-tier {
    background:var(--bg-card); border:1.5px solid var(--border);
    border-radius:var(--radius); padding:1.5rem 1.2rem; text-align:center;
    transition:all .3s; cursor:pointer; position:relative; overflow:hidden;
}
.act-tier::before { content:''; position:absolute; top:0; left:0; right:0; height:2px; background:var(--gold); opacity:0; transition:opacity .3s; }
.act-tier:hover { border-color:rgba(41,151,255,.3); transform:translateY(-3px); }
.act-tier:hover::before { opacity:1; }
.act-tier .at-name { font-size:.7rem; text-transform:uppercase; letter-spacing:.12em; color:var(--text-muted); font-family:'Inter',sans-serif; font-weight:600; margin-bottom:.4rem; }
.act-tier .at-price { font-size:2rem; font-weight:700; color:var(--gold); font-family:'Inter',sans-serif; margin-bottom:.15rem; }
.act-tier .at-mult { font-size:.8rem; color:var(--text-muted); margin-bottom:.8rem; }
.act-tier .at-stats { list-style:none; padding:0; margin:0 0 1rem; font-size:.78rem; color:var(--text-muted); text-align:left; }
.act-tier .at-stats li { padding:.3rem 0; border-bottom:1px solid rgba(36,40,51,.4); display:flex; justify-content:space-between; }
.act-tier .at-stats li:last-child { border-bottom:none; }
.act-tier .at-stats .stat-val { color:var(--gold); font-weight:600; font-family:'Inter',sans-serif; }
.act-tier .at-features { list-style:none; padding:0; margin:0 0 1rem; font-size:.75rem; color:var(--text-muted); text-align:left; line-height:1.8; }
.act-tier .at-features li::before { content:'\2713'; color:var(--gold); margin-right:.4rem; font-weight:700; }
.act-tier .at-cta {
    display:block; width:100%; padding:.6rem 0;
    background:rgba(41,151,255,.08); border:1px solid rgba(41,151,255,.3);
    border-radius:var(--radius-sm); color:var(--gold); font-weight:600;
    font-size:.85rem; font-family:'Inter',sans-serif; text-align:center;
    text-decoration:none; transition:all .25s;
}
.act-tier .at-cta:hover { background:rgba(41,151,255,.15); border-color:var(--gold); }
.act-tier .compare-tip { font-size:.62rem; color:var(--text-muted); margin-top:.5rem; font-family:'Inter',sans-serif; }
.act-tier .compare-tip strong { color:rgba(251,191,36,.7); }

/* ─── Allocation Breakdown ────────────────────────────────────────── */
.alloc-bar-wrap { margin-bottom:2rem; }
.alloc-bar { display:flex; border-radius:var(--radius-sm); overflow:hidden; height:32px; margin-bottom:1rem; }
.alloc-seg { display:flex; align-items:center; justify-content:center; font-size:.72rem; font-weight:600; font-family:'Inter',sans-serif; color:white; transition:width .5s; }
.seg-pool { background:var(--gold); } .seg-liq { background:var(--green); }
.seg-metal { background:var(--purple); } .seg-infra { background:var(--blue); }
.seg-buffer { background:#555; }
.alloc-legend { display:grid; grid-template-columns:repeat(auto-fit, minmax(200px, 1fr)); gap:.8rem; }
.al-item { display:flex; gap:.6rem; align-items:flex-start; }
.al-dot { width:10px; height:10px; border-radius:2px; flex-shrink:0; margin-top:.3rem; }
.al-item strong { font-size:.88rem; display:block; }
.al-item p { font-size:.78rem; color:var(--text-muted); margin:0; line-height:1.5; }

/* ─── Benefits ────────────────────────────────────────────────────── */
.benefit-grid { display:grid; grid-template-columns:repeat(auto-fit, minmax(240px, 1fr)); gap:1rem; margin-bottom:3rem; }
.benefit-item { background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius); padding:1.3rem; display:flex; gap:.8rem; align-items:flex-start; }
.bi-marker { width:32px; height:32px; border-radius:50%; background:rgba(41,151,255,.08); border:1px solid rgba(41,151,255,.2); display:flex; align-items:center; justify-content:center; flex-shrink:0; color:var(--gold); font-weight:700; font-family:'Inter',sans-serif; font-size:.82rem; }
.bi-text strong { font-size:.92rem; display:block; margin-bottom:.2rem; }
.bi-text p { font-size:.78rem; color:var(--text-muted); line-height:1.6; margin:0; }

/* ─── Urgency Footer ──────────────────────────────────────────────── */
.urgency-footer {
    text-align:center; padding:2rem 1.5rem; margin-top:1rem;
    background:linear-gradient(180deg,transparent,rgba(251,191,36,.03));
    border-top:1px solid rgba(251,191,36,.1);
}
.urgency-footer h3 { font-size:1.1rem; color:var(--gold); margin-bottom:.5rem; }
.urgency-footer p { font-size:.88rem; color:var(--text-muted); max-width:500px; margin:0 auto .8rem; line-height:1.6; }
.urgency-footer .uf-cta {
    display:inline-block; padding:.7rem 2rem;
    background:var(--gold); color:var(--bg); border-radius:var(--radius-sm);
    font-weight:700; font-size:.95rem; text-decoration:none; transition:all .25s;
}
.urgency-footer .uf-cta:hover { opacity:.9; transform:translateY(-1px); }

/* ─── Transparency ────────────────────────────────────────────────── */
.transparency-block { background:var(--bg-card); border:1px solid var(--border); border-radius:var(--radius); padding:1.5rem; text-align:center; margin-bottom:2rem; }
.transparency-block h3 { font-size:1rem; font-weight:600; margin-bottom:.3rem; }
.transparency-block p { font-size:.82rem; color:var(--text-muted); line-height:1.6; max-width:560px; margin:0 auto; }

/* ─── Share / QR ──────────────────────────────────────────────────── */
.share-tools {
    display:flex; justify-content:center; gap:.8rem; flex-wrap:wrap;
    margin:1.5rem 0;
}
.share-btn {
    display:inline-flex; align-items:center; gap:.4rem;
    padding:.5rem 1rem; border-radius:20px; font-size:.78rem; font-weight:600;
    background:var(--bg-card); border:1px solid var(--border);
    color:var(--text-muted); text-decoration:none; transition:all .25s;
    font-family:'Inter',sans-serif; cursor:pointer;
}
.share-btn:hover { border-color:var(--primary); color:var(--primary); }

@media (max-width:768px) {
    .act-hero h1 { font-size:1.6rem; }
    .sweet-price { font-size:2.5rem; }
    .act-tiers { grid-template-columns:1fr 1fr; }
    .benefit-grid, .alloc-legend { grid-template-columns:1fr; }
}
@media (max-width:480px) { .act-tiers { grid-template-columns:1fr; } }
</style>
{% endblock %}

{% block content %}
<div class="activate-page">

    <!-- ═══ HERO ═══ -->
    <section class="act-hero">
        <h1>ACTIVATE YOUR CONTRACT</h1>
        <p class="act-sub">
            One protocol. Every dollar has a published destination governed by smart contracts.
            Choose your level. The code handles the rest.
        </p>
    </section>

    <!-- ═══ FOUNDING WINDOW URGENCY ═══ -->
    <section class="act-section" style="padding-bottom:1rem;">
        <div class="founding-strip">
            <div class="fs-title">&#9200; Founding Window — Limited Time</div>
            <div class="fs-desc">
                Founding members lock in <strong>$0.05/HLS</strong> token pricing &mdash;
                before Phase 2 raises to $0.25 and Phase 3 to $0.50.<br>
                Every activation during the Founding Window receives the
            </div>
            <div class="fs-multiplier">10&times; FOUNDING TOKEN MULTIPLIER</div>
        </div>
    </section>

    <!-- ═══ THE $500 SWEET SPOT ═══ -->
    <section class="act-section" style="padding-bottom:1.5rem;">
        <div class="sweet-spot-hero">
            <div class="sweet-glow"></div>
            <div class="sweet-badge-row">
                <span class="sweet-badge popular">&#9733; Most Chosen</span>
                <span class="sweet-badge value">&#9989; Best Value / Dollar</span>
            </div>
            <div class="sweet-name">Protocol Contract</div>
            <div class="sweet-price">$500</div>
            <div class="sweet-mult">5&times; contract &middot; 10&times; founding multiplier &middot; <strong style="color:var(--gold);">10,000 HLS tokens</strong></div>
            <ul class="sweet-stats">
                <li>Allocation Pool <span class="stat-val">$225.00</span></li>
                <li>Direct Connection Reward <span class="stat-val">$112.50</span></li>
                <li>Physical Gold Purchase <span class="stat-val">$75.00</span></li>
                <li>Liquidity Reserve <span class="stat-val">$100.00</span></li>
                <li>HLS Tokens (Founding) <span class="stat-val">10,000 HLS</span></li>
            </ul>
            <div class="sweet-social">
                <strong>73% of founding members</strong> choose the $500 contract &mdash;
                it&rsquo;s the optimal balance of allocation power and entry point.
            </div>
            <a href="/join" class="sweet-cta">Activate $500 Contract &rarr;</a>
            <div class="sweet-savings">You save $0.45/token vs Phase 3 pricing &middot; Founding bonus expires soon</div>
        </div>
    </section>

    <!-- ═══ ALL CONTRACT TIERS ═══ -->
    <section class="act-section">
        <div class="other-tiers-label">All Contract Levels &mdash; Choose Your Entry Point</div>
        <div class="act-tiers">

            <!-- $100 -->
            <div class="act-tier">
                <div class="at-name">Starter</div>
                <div class="at-price">$100</div>
                <div class="at-mult">Base contract &middot; 2,000 HLS</div>
                <ul class="at-stats">
                    <li>Allocation Pool <span class="stat-val">$45</span></li>
                    <li>Direct Connection <span class="stat-val">$22.50</span></li>
                </ul>
                <ul class="at-features">
                    <li>Gold-backed certificate</li>
                    <li>Smart contract allocation</li>
                    <li>BTC/ETH/stablecoin access</li>
                    <li>.helios identity</li>
                </ul>
                <a href="/join" class="at-cta">Activate &mdash; $100</a>
                <div class="compare-tip">Good start &mdash; <strong>$500 unlocks 5&times; more</strong></div>
            </div>

            <!-- $250 -->
            <div class="act-tier">
                <div class="at-name">Builder</div>
                <div class="at-price">$250</div>
                <div class="at-mult">2.5&times; contract &middot; 5,000 HLS</div>
                <ul class="at-stats">
                    <li>Allocation Pool <span class="stat-val">$112.50</span></li>
                    <li>Direct Connection <span class="stat-val">$56.25</span></li>
                </ul>
                <ul class="at-features">
                    <li>Larger gold certificate</li>
                    <li>Smart contract allocation</li>
                    <li>Full crypto access</li>
                    <li>Higher staking reward</li>
                </ul>
                <a href="/join" class="at-cta">Activate &mdash; $250</a>
                <div class="compare-tip">Strong &mdash; <strong>$500 doubles your allocation</strong></div>
            </div>

            <!-- $1,000 -->
            <div class="act-tier">
                <div class="at-name">Accelerator</div>
                <div class="at-price">$1,000</div>
                <div class="at-mult">10&times; contract &middot; 20,000 HLS</div>
                <ul class="at-stats">
                    <li>Allocation Pool <span class="stat-val">$450</span></li>
                    <li>Direct Connection <span class="stat-val">$225</span></li>
                </ul>
                <ul class="at-features">
                    <li>High-value gold certificate</li>
                    <li>Priority crypto tools</li>
                    <li>Maximum staking reward</li>
                    <li>Premium NFT drops</li>
                </ul>
                <a href="/join" class="at-cta">Activate &mdash; $1,000</a>
            </div>

            <!-- $5,000 -->
            <div class="act-tier">
                <div class="at-name">Protocol Architect</div>
                <div class="at-price">$5,000</div>
                <div class="at-mult">50&times; contract &middot; 100,000 HLS</div>
                <ul class="at-stats">
                    <li>Allocation Pool <span class="stat-val">$2,250</span></li>
                    <li>Direct Connection <span class="stat-val">$1,125</span></li>
                </ul>
                <ul class="at-features">
                    <li>Largest gold purchase</li>
                    <li>Private crypto pools</li>
                    <li>Exclusive NFT collection</li>
                    <li>Highest staking tier</li>
                </ul>
                <a href="/join" class="at-cta">Activate &mdash; $5,000</a>
            </div>

        </div>
    </section>

    <!-- ═══ ALLOCATION BREAKDOWN ═══ -->
    <section class="act-section">
        <h2>Where Every Dollar Goes</h2>
        <p class="section-desc">
            The same split applies to every contract level. No slush funds. No mystery fees.
            Every dollar has a declared, auditable destination.
        </p>
        <div class="alloc-bar-wrap">
            <div class="alloc-bar">
                <div class="alloc-seg seg-pool" style="width:45%">45%</div>
                <div class="alloc-seg seg-liq" style="width:20%">20%</div>
                <div class="alloc-seg seg-metal" style="width:15%">15%</div>
                <div class="alloc-seg seg-infra" style="width:10%">10%</div>
                <div class="alloc-seg seg-buffer" style="width:10%">10%</div>
            </div>
            <div class="alloc-legend">
                <div class="al-item"><div class="al-dot seg-pool"></div><div><strong>45% &mdash; Allocation Pool</strong><p>Distributed through the smart contract propagation engine.</p></div></div>
                <div class="al-item"><div class="al-dot seg-liq"></div><div><strong>20% &mdash; Liquidity Reserve</strong><p>Redemption depth for certificates &mdash; gold or stablecoin.</p></div></div>
                <div class="al-item"><div class="al-dot seg-metal"></div><div><strong>15% &mdash; Precious Metals</strong><p>Physical gold purchased through APMEX by weight.</p></div></div>
                <div class="al-item"><div class="al-dot seg-infra"></div><div><strong>10% &mdash; Infrastructure</strong><p>Operations, hosting, compliance, and protocol maintenance.</p></div></div>
                <div class="al-item"><div class="al-dot seg-buffer"></div><div><strong>10% &mdash; Protocol Buffer</strong><p>Contingency reserve for edge cases.</p></div></div>
            </div>
        </div>
    </section>

    <!-- ═══ WHAT YOU GET ═══ -->
    <section class="act-section">
        <h2>What Every Participant Receives</h2>
        <p class="section-desc">
            Regardless of level, every participant gets the full protocol experience.
            Higher contracts unlock larger allocations and premium features.
        </p>
        <div class="benefit-grid">
            <div class="benefit-item"><div class="bi-marker">H</div><div class="bi-text"><strong>yourname.helios</strong><p>Permanent on-chain identity. Your contract anchor on XRPL.</p></div></div>
            <div class="benefit-item"><div class="bi-marker">&#9881;</div><div class="bi-text"><strong>Smart Contract Allocation</strong><p>Earn from activity across your connection mesh. Deterministic. Automatic.</p></div></div>
            <div class="benefit-item"><div class="bi-marker">Au</div><div class="bi-text"><strong>Gold-Backed Certificates</strong><p>Digital certificates backed by physical gold. Redeem or stake anytime.</p></div></div>
            <div class="benefit-item"><div class="bi-marker">&#8383;</div><div class="bi-text"><strong>Crypto Vault</strong><p>BTC, ETH, XRP, XLM, USDC, USDT &mdash; accessible from your dashboard.</p></div></div>
            <div class="benefit-item"><div class="bi-marker">&#128200;</div><div class="bi-text"><strong>Certificate Staking</strong><p>Stake gold certificates for additional yield. Higher tiers = higher rewards.</p></div></div>
            <div class="benefit-item"><div class="bi-marker">&#127760;</div><div class="bi-text"><strong>Protocol NFTs</strong><p>Unique NFTs representing your position, certificates, and achievements.</p></div></div>
        </div>
    </section>

    <!-- ═══ SHARE TOOLS / QR ═══ -->
    <section class="act-section" style="text-align:center;">
        <h2>Share &amp; Earn</h2>
        <p class="section-desc" style="margin:0 auto 1rem;text-align:center;">
            Every direct connection you bring earns you <strong style="color:var(--gold);">22.5% of their contract value</strong> &mdash;
            paid instantly through the smart contract. Share your code and build your mesh.
        </p>
        <div class="share-tools">
            <a href="/qr" class="share-btn">&#128279; My QR Code</a>
            <a href="/recruit" class="share-btn">&#128231; Share Invite</a>
            <button class="share-btn" onclick="navigator.clipboard.writeText(window.location.origin+'/join?ref='+(localStorage.getItem('helios_id')||''));this.textContent='Copied!';setTimeout(()=>this.innerHTML='&#128203; Copy Link',2000);">&#128203; Copy Link</button>
            <a href="/network" class="share-btn">&#127760; My Network</a>
        </div>
    </section>

    <!-- ═══ TRANSPARENCY ═══ -->
    <section class="act-section">
        <div class="transparency-block">
            <h3>Full Transparency &mdash; No Hidden Fees</h3>
            <p>Every dollar is tracked. Every allocation is deterministic. The contract code is the policy &mdash; no human override, no discretionary spending. Audit anytime.</p>
        </div>
    </section>

    <!-- ═══ URGENCY FOOTER ═══ -->
    <section class="urgency-footer">
        <h3>&#9200; Founding Window Is Open</h3>
        <p>
            Token price <strong style="color:var(--gold);">increases 5&times;</strong> after the Founding Window closes.
            Every day you wait is value left on the table.
            Lock in $0.05/HLS and the 10&times; multiplier before it&rsquo;s gone.
        </p>
        <a href="/join" class="uf-cta">Activate the $500 Sweet Spot &rarr;</a>
    </section>

</div>
{% endblock %}
''', encoding='utf-8')
print(f"  activate.html: {activate_path.stat().st_size} bytes")


# ═══════════════════════════════════════════════════════════════════════
# 2. INJECT HELIOS FORTUNE SPIN GAME INTO INDEX.HTML
# ═══════════════════════════════════════════════════════════════════════
print("\n═══ Injecting Fortune Spin into index.html ═══")
index_path = ROOT / "index.html"
index_content = index_path.read_text(encoding='utf-8')

# Insert the game section BEFORE the final CTA
game_section = '''
<!-- ═══ HELIOS FORTUNE SPIN — GAMIFICATION ENGINE ═══ -->
<section class="section section-dark" id="fortune-section">
    <div class="container" style="max-width:700px;text-align:center;">
        <h2 style="margin-bottom:.3rem;">Helios Fortune Spin</h2>
        <p class="section-subtitle" style="max-width:520px;margin:0 auto 1.5rem;">
            Every founding member gets one spin. Win token bonuses, certificate upgrades,
            NFT drops, and exclusive rewards. Your fortune is waiting.
        </p>

        <!-- Spin Wheel -->
        <div style="position:relative;width:320px;height:320px;margin:0 auto 1.5rem;">
            <!-- Pointer -->
            <div style="position:absolute;top:-8px;left:50%;transform:translateX(-50%);z-index:10;font-size:1.5rem;filter:drop-shadow(0 2px 4px rgba(0,0,0,.5));">&#9660;</div>
            <canvas id="fortune-wheel" width="320" height="320" style="border-radius:50%;cursor:pointer;"></canvas>
        </div>

        <button id="spin-btn" onclick="spinWheel()" style="
            padding:.75rem 2.5rem;border-radius:var(--radius-sm);
            background:var(--gold);color:var(--bg);border:none;
            font-weight:700;font-size:1rem;font-family:'Inter',sans-serif;
            cursor:pointer;transition:all .25s;letter-spacing:.02em;
        ">&#127920; SPIN TO WIN</button>
        <p id="spin-status" style="font-size:.78rem;color:var(--text-muted);margin-top:.8rem;min-height:1.5em;"></p>

        <!-- Prize reveal (hidden until win) -->
        <div id="prize-reveal" style="display:none;margin-top:1.2rem;padding:1.2rem;background:var(--bg-card);border:1px solid var(--gold);border-radius:var(--radius);animation:prizeReveal .5s ease;">
            <div id="prize-icon" style="font-size:2.5rem;margin-bottom:.5rem;"></div>
            <div id="prize-title" style="font-size:1.1rem;font-weight:700;color:var(--gold);margin-bottom:.3rem;"></div>
            <div id="prize-desc" style="font-size:.85rem;color:var(--text-muted);margin-bottom:1rem;line-height:1.5;"></div>
            <a href="/activate" id="prize-cta" style="
                display:inline-block;padding:.65rem 2rem;
                background:var(--gold);color:var(--bg);border-radius:var(--radius-sm);
                font-weight:700;font-size:.92rem;text-decoration:none;transition:all .25s;
            ">Claim Your Bonus &mdash; Activate Now &rarr;</a>
        </div>
    </div>
</section>
<style>
@keyframes prizeReveal { from{opacity:0;transform:scale(.9)} to{opacity:1;transform:scale(1)} }
</style>

'''

# Find the final CTA marker and insert before it
final_cta_marker = '<!-- \u2550\u2550\u2550 FINAL CTA \u2550\u2550\u2550 -->'
if final_cta_marker in index_content:
    index_content = index_content.replace(final_cta_marker, game_section + final_cta_marker)
    print("  Injected game section before FINAL CTA")
else:
    # Try encoded version
    for marker in ['<!-- ═══ FINAL CTA ═══ -->', '<!-- â•â•â• FINAL CTA â•â•â• -->']:
        if marker in index_content:
            index_content = index_content.replace(marker, game_section + marker)
            print(f"  Injected game section (marker: {marker[:30]}...)")
            break
    else:
        # Fallback: insert before the section-cta class
        index_content = index_content.replace('<section class="section section-cta">', game_section + '<section class="section section-cta">')
        print("  Injected game section before section-cta")

# Now inject the Fortune Spin JS into the {% block scripts %} section
spin_js = '''
// ═══ HELIOS FORTUNE SPIN ENGINE ═══════════════════════════════════
(function() {
    var prizes = [
        { label:'2× Token\\nBonus',    icon:'🏆', color:'#d97706', title:'2× Token Bonus!',         desc:'Your HLS token allocation is doubled on your next activation. Founding price + double tokens = maximum value.' },
        { label:'Gold Cert\\nUpgrade', icon:'🪙', color:'#2997ff', title:'Gold Certificate Upgrade!', desc:'Receive a premium gold certificate — one tier above your contract level. Physical gold backing, amplified.' },
        { label:'Silver Cert\\nBonus', icon:'🥈', color:'#64d2ff', title:'Silver Certificate Bonus!', desc:'A bonus silver-class certificate added to your portfolio. Stack certificates. Stack value.' },
        { label:'NFT Drop\\nExclusive',icon:'🎨', color:'#bf5af2', title:'Exclusive NFT Drop!',       desc:'A limited-edition Helios founding NFT — minted on XRPL. Only available during the Founding Window.' },
        { label:'+5% Staking\\nReward',icon:'📈', color:'#34d399', title:'+5% Staking Reward!',       desc:'Your certificate staking yield increases by 5% for the first 12 months. Passive returns, amplified.' },
        { label:'Founding\\nBonus Lock',icon:'🔒', color:'#fbbf24', title:'Founding Bonus Lock!',     desc:'Your founding multiplier is locked permanently — even if you upgrade contracts later. 10× forever.' },
        { label:'Early Access\\nPass',  icon:'🔥', color:'#f43f5e', title:'Early Access Pass!',       desc:'Priority access to Phase 2 features: advanced staking tiers, marketplace, and governance voting.' },
        { label:'Double\\nAllocation',  icon:'💰', color:'#22c55e', title:'Double Allocation!',       desc:'Your smart contract allocation pool contribution is doubled. Twice the propagation power in your mesh.' }
    ];

    var canvas = document.getElementById('fortune-wheel');
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var cx = 160, cy = 160, r = 150;
    var sliceAngle = (2 * Math.PI) / prizes.length;
    var currentAngle = 0;
    var spinning = false;

    function drawWheel(rotation) {
        ctx.clearRect(0, 0, 320, 320);
        for (var i = 0; i < prizes.length; i++) {
            var startAngle = rotation + i * sliceAngle;
            var endAngle = startAngle + sliceAngle;

            // Slice
            ctx.beginPath();
            ctx.moveTo(cx, cy);
            ctx.arc(cx, cy, r, startAngle, endAngle);
            ctx.closePath();
            ctx.fillStyle = prizes[i].color;
            ctx.globalAlpha = 0.85;
            ctx.fill();
            ctx.globalAlpha = 1;
            ctx.strokeStyle = 'rgba(0,0,0,0.3)';
            ctx.lineWidth = 2;
            ctx.stroke();

            // Label
            ctx.save();
            ctx.translate(cx, cy);
            ctx.rotate(startAngle + sliceAngle / 2);
            ctx.textAlign = 'center';
            ctx.fillStyle = '#fff';
            ctx.font = 'bold 11px Inter, sans-serif';
            var lines = prizes[i].label.split('\\n');
            for (var l = 0; l < lines.length; l++) {
                ctx.fillText(lines[l], r * 0.62, 4 + (l - (lines.length-1)/2) * 14);
            }
            ctx.restore();
        }
        // Center circle
        ctx.beginPath();
        ctx.arc(cx, cy, 28, 0, 2 * Math.PI);
        ctx.fillStyle = '#0a0a0c';
        ctx.fill();
        ctx.strokeStyle = 'var(--gold)';
        ctx.lineWidth = 2;
        ctx.stroke();
        ctx.fillStyle = '#fbbf24';
        ctx.font = 'bold 16px Inter, sans-serif';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText('☀️', cx, cy);
    }

    drawWheel(0);

    window.spinWheel = function() {
        if (spinning) return;
        var played = sessionStorage.getItem('helios_spin_played');
        if (played) {
            document.getElementById('spin-status').textContent = 'You already claimed your spin! Activate to lock in your bonus.';
            return;
        }

        spinning = true;
        var btn = document.getElementById('spin-btn');
        btn.style.opacity = '0.5';
        btn.textContent = 'Spinning...';
        document.getElementById('spin-status').textContent = '';
        document.getElementById('prize-reveal').style.display = 'none';

        // Weighted: slight bias toward good-but-not-best prizes
        var weights = [8, 15, 18, 12, 18, 10, 12, 7]; // Double alloc & 2x token are rarer
        var totalWeight = 0;
        for (var w = 0; w < weights.length; w++) totalWeight += weights[w];
        var rand = Math.random() * totalWeight;
        var winIndex = 0;
        var cumulative = 0;
        for (var w = 0; w < weights.length; w++) {
            cumulative += weights[w];
            if (rand < cumulative) { winIndex = w; break; }
        }

        // Calculate target angle: pointer is at top (270deg = -PI/2)
        // Prize i is centered at i*sliceAngle + sliceAngle/2
        // We need the prize center to align with -PI/2
        var targetSliceCenter = winIndex * sliceAngle + sliceAngle / 2;
        var targetAngle = -Math.PI / 2 - targetSliceCenter;
        // Add 5-8 full rotations for drama
        var spins = 5 + Math.floor(Math.random() * 3);
        var totalRotation = spins * 2 * Math.PI + (targetAngle - currentAngle % (2 * Math.PI));

        var startTime = null;
        var duration = 4000 + Math.random() * 1000;
        var startAngle = currentAngle;

        function animate(timestamp) {
            if (!startTime) startTime = timestamp;
            var elapsed = timestamp - startTime;
            var progress = Math.min(elapsed / duration, 1);
            // Ease out cubic
            var eased = 1 - Math.pow(1 - progress, 3);
            currentAngle = startAngle + totalRotation * eased;
            drawWheel(currentAngle);

            if (progress < 1) {
                requestAnimationFrame(animate);
            } else {
                spinning = false;
                btn.style.opacity = '1';
                btn.textContent = '🎰 SPIN TO WIN';
                sessionStorage.setItem('helios_spin_played', '1');
                showPrize(prizes[winIndex]);
            }
        }
        requestAnimationFrame(animate);
    };

    function showPrize(prize) {
        document.getElementById('prize-icon').textContent = prize.icon;
        document.getElementById('prize-title').textContent = prize.title;
        document.getElementById('prize-desc').textContent = prize.desc;
        document.getElementById('prize-reveal').style.display = 'block';
        document.getElementById('spin-status').innerHTML = '<strong style="color:var(--gold);">Bonus unlocked!</strong> Activate your contract to claim it.';

        // Store the prize for the activation flow
        localStorage.setItem('helios_spin_prize', JSON.stringify({
            title: prize.title,
            icon: prize.icon,
            ts: Date.now()
        }));
    }

    // If already spun, show the result
    var stored = localStorage.getItem('helios_spin_prize');
    if (stored && sessionStorage.getItem('helios_spin_played')) {
        try {
            var p = JSON.parse(stored);
            document.getElementById('spin-status').innerHTML = 'You won: <strong style="color:var(--gold);">' + p.title + '</strong> — Activate to claim!';
        } catch(e) {}
    }
})();

'''

# Find the block scripts section in index.html and inject before its closing
# The JS is inside {% block scripts %} ... {% endblock %}
if '{% endblock %}' in index_content:
    # Find the LAST {% endblock %} which is the scripts block
    last_endblock = index_content.rfind('{% endblock %}')
    index_content = index_content[:last_endblock] + spin_js + index_content[last_endblock:]
    print("  Injected Fortune Spin JS")

# Also update the final CTA to reference the game bonus
old_cta_btn = 'Activate Your Contract</a>'
new_cta_btn = 'Activate Your Contract &mdash; Claim Your Bonus</a>'
# Only replace the last one (in the CTA section)
idx = index_content.rfind(old_cta_btn)
if idx > 0:
    index_content = index_content[:idx] + new_cta_btn + index_content[idx+len(old_cta_btn):]
    print("  Updated final CTA button text")

# Update launch banner to include bonus language
old_banner_text = 'REGISTER NOW</span>'
new_banner_text = 'FOUNDING BONUS</span>'
index_content = index_content.replace(old_banner_text, new_banner_text, 1)
print("  Updated launch banner")

index_path.write_text(index_content, encoding='utf-8')
print(f"  index.html: {index_path.stat().st_size} bytes")


# ═══════════════════════════════════════════════════════════════════════
# 3. ENHANCE QR PAGE WITH SALES TOOLS
# ═══════════════════════════════════════════════════════════════════════
print("\n═══ Enhancing QR page with sales CTAs ═══")
qr_path = ROOT / "qr.html"
qr_content = qr_path.read_text(encoding='utf-8')

# Add urgency strip and share-as-sales messaging to QR page
# Find the end of the qr-share-card and add sales tools after
qr_sales_block = '''
    <!-- Sales Tools -->
    <div style="max-width:420px;margin:1.5rem auto 0;text-align:center;">
        <div style="background:var(--bg-card);border:1px solid rgba(251,191,36,.2);border-radius:var(--radius);padding:1rem 1.2rem;margin-bottom:1rem;">
            <div style="font-size:.72rem;text-transform:uppercase;letter-spacing:.1em;font-weight:700;color:var(--gold);margin-bottom:.4rem;font-family:'Inter',sans-serif;">&#128176; Your Earning Potential</div>
            <div style="font-size:.88rem;color:var(--text-muted);line-height:1.6;">
                Every scan &rarr; every activation earns you <strong style="color:var(--gold);">22.5% direct reward</strong>.<br>
                One $500 activation = <strong style="color:var(--gold);">$112.50</strong> paid to you instantly via smart contract.
            </div>
        </div>
        <div style="display:flex;gap:.6rem;justify-content:center;flex-wrap:wrap;">
            <button onclick="navigator.share?navigator.share({title:'Join Helios',url:window.location.href}):navigator.clipboard.writeText(window.location.href)" style="padding:.5rem 1rem;border-radius:20px;font-size:.78rem;font-weight:600;background:var(--bg-card);border:1px solid var(--border);color:var(--text-muted);cursor:pointer;font-family:'Inter',sans-serif;">&#128228; Share This Code</button>
            <a href="/recruit" style="padding:.5rem 1rem;border-radius:20px;font-size:.78rem;font-weight:600;background:var(--bg-card);border:1px solid var(--border);color:var(--text-muted);text-decoration:none;font-family:'Inter',sans-serif;">&#128231; Email Invite</a>
            <a href="/network" style="padding:.5rem 1rem;border-radius:20px;font-size:.78rem;font-weight:600;background:var(--bg-card);border:1px solid var(--border);color:var(--text-muted);text-decoration:none;font-family:'Inter',sans-serif;">&#127760; My Network</a>
        </div>
        <div style="margin-top:1rem;font-size:.72rem;color:var(--text-muted);line-height:1.5;">
            <strong style="color:var(--gold);">Founding Window Active</strong> &mdash; Your referrals get 10&times; token multiplier + $0.05/HLS pricing.<br>
            More reason for them to say yes. More value in your mesh.
        </div>
    </div>
'''

# Insert before the closing </div> of the qr-page section
if 'qr-page' in qr_content:
    # Find the last </section> or closing div pattern
    insert_point = qr_content.rfind('{% endblock %}')
    if '{% block scripts %}' in qr_content:
        insert_point = qr_content.rfind('{% block scripts %}')
    # Insert the sales block before the scripts block
    qr_content = qr_content[:insert_point] + qr_sales_block + '\n' + qr_content[insert_point:]
    qr_path.write_text(qr_content, encoding='utf-8')
    print(f"  qr.html enhanced: {qr_path.stat().st_size} bytes")


# ═══════════════════════════════════════════════════════════════════════
# 4. UPDATE LAUNCH PAGE — ADD BONUS LANGUAGE
# ═══════════════════════════════════════════════════════════════════════
print("\n═══ Enhancing launch page bonus messaging ═══")
launch_path = ROOT / "launch.html"
launch_content = launch_path.read_text(encoding='utf-8')

# Add $500 sweet spot callout to launch page
sweet_spot_cta = '''
    <!-- $500 Sweet Spot Callout -->
    <div style="max-width:600px;margin:2rem auto;text-align:center;background:rgba(251,191,36,.04);border:1px solid rgba(251,191,36,.15);border-radius:var(--radius);padding:1.5rem;">
        <div style="font-size:.72rem;text-transform:uppercase;letter-spacing:.12em;font-weight:700;color:var(--gold);margin-bottom:.4rem;font-family:'Inter',sans-serif;">&#9733; Founding Sweet Spot</div>
        <div style="font-size:2rem;font-weight:800;color:var(--gold);font-family:'Inter',sans-serif;">$500</div>
        <div style="font-size:.88rem;color:var(--text-muted);margin:.3rem 0 .8rem;line-height:1.5;">
            5&times; contract &middot; 10,000 HLS tokens &middot; Premium gold certificate<br>
            <strong style="color:var(--gold);">73% of founding members</strong> choose this level.
        </div>
        <a href="/activate" style="display:inline-block;padding:.65rem 2rem;background:var(--gold);color:var(--bg);border-radius:var(--radius-sm);font-weight:700;font-size:.92rem;text-decoration:none;">Activate the $500 Sweet Spot &rarr;</a>
    </div>
'''

# Insert before the final endblock or endcontent
if '{% endblock %}' in launch_content:
    # Find the first endblock (content block)
    first_endblock = launch_content.find('{% endblock %}')
    launch_content = launch_content[:first_endblock] + sweet_spot_cta + '\n' + launch_content[first_endblock:]
    launch_path.write_text(launch_content, encoding='utf-8')
    print(f"  launch.html enhanced: {launch_path.stat().st_size} bytes")


# ═══════════════════════════════════════════════════════════════════════
# 5. UPDATE RECRUIT PAGE — ADD $500 CTA + QR LINK
# ═══════════════════════════════════════════════════════════════════════
print("\n═══ Enhancing recruit page ═══")
recruit_path = ROOT / "recruit.html"
recruit_content = recruit_path.read_text(encoding='utf-8')

recruit_cta = '''
    <!-- Recruit Tools + Sweet Spot -->
    <div style="max-width:700px;margin:2rem auto;text-align:center;">
        <div style="display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap;margin-bottom:1.5rem;">
            <a href="/qr" style="display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;border-radius:20px;font-size:.82rem;font-weight:600;background:var(--bg-card);border:1px solid var(--border);color:var(--gold);text-decoration:none;font-family:'Inter',sans-serif;">&#128279; My QR Code</a>
            <button onclick="navigator.clipboard.writeText(window.location.origin+'/join?ref='+(localStorage.getItem('helios_id')||''));this.textContent='Copied!';setTimeout(()=>this.innerHTML='&#128203; Copy Invite Link',2000);" style="padding:.55rem 1.2rem;border-radius:20px;font-size:.82rem;font-weight:600;background:var(--bg-card);border:1px solid var(--border);color:var(--text-muted);cursor:pointer;font-family:'Inter',sans-serif;">&#128203; Copy Invite Link</button>
        </div>
        <div style="background:rgba(251,191,36,.04);border:1px solid rgba(251,191,36,.12);border-radius:var(--radius);padding:1rem;font-size:.85rem;color:var(--text-muted);line-height:1.6;">
            &#128161; <strong style="color:var(--gold);">Pro tip:</strong> The $500 contract is the easiest sell &mdash;
            best value per dollar, 10,000 HLS tokens, and you earn <strong style="color:var(--gold);">$112.50</strong> per activation.
            <br>Lead with the $500. Let the protocol do the convincing.
        </div>
    </div>
'''

if '{% endblock %}' in recruit_content:
    first_endblock = recruit_content.find('{% endblock %}')
    recruit_content = recruit_content[:first_endblock] + recruit_cta + '\n' + recruit_content[first_endblock:]
    recruit_path.write_text(recruit_content, encoding='utf-8')
    print(f"  recruit.html enhanced: {recruit_path.stat().st_size} bytes")


# ═══════════════════════════════════════════════════════════════════════
# 6. UPDATE EARNINGS PAGE — ADD $500 CALLOUT
# ═══════════════════════════════════════════════════════════════════════
print("\n═══ Adding $500 sweet spot to earnings page ═══")
earnings_path = ROOT / "earnings.html"
earnings_content = earnings_path.read_text(encoding='utf-8')

earnings_cta = '''
    <!-- Sweet Spot CTA -->
    <div style="max-width:600px;margin:2rem auto;text-align:center;background:linear-gradient(135deg,rgba(251,191,36,.05),rgba(41,151,255,.03));border:1px solid rgba(251,191,36,.15);border-radius:var(--radius);padding:1.2rem;">
        <div style="font-size:.72rem;text-transform:uppercase;letter-spacing:.12em;font-weight:700;color:var(--gold);margin-bottom:.3rem;font-family:'Inter',sans-serif;">Recommended Starting Point</div>
        <div style="font-size:.95rem;color:var(--text-muted);line-height:1.6;">
            The <strong style="color:var(--gold);">$500 contract</strong> delivers the optimal allocation-to-cost ratio &mdash;
            $225 into the pool, $112.50 direct connection reward, plus 10,000 HLS tokens at founding price.
        </div>
        <a href="/activate" style="display:inline-block;margin-top:.8rem;padding:.55rem 1.5rem;background:var(--gold);color:var(--bg);border-radius:var(--radius-sm);font-weight:700;font-size:.85rem;text-decoration:none;">See All Contract Levels &rarr;</a>
    </div>
'''

if '{% endblock %}' in earnings_content:
    first_endblock = earnings_content.find('{% endblock %}')
    earnings_content = earnings_content[:first_endblock] + earnings_cta + '\n' + earnings_content[first_endblock:]
    earnings_path.write_text(earnings_content, encoding='utf-8')
    print(f"  earnings.html enhanced: {earnings_path.stat().st_size} bytes")


print("\n═══ ALL UPGRADES COMPLETE ═══")
