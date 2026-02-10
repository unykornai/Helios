"""
Ask Helios — The Voice
════════════════════════════════════════════════════════
Male. Calm. Grounded. Authoritative. Never salesy. Never defensive.
"I'll explain it. You decide."

KEY-NATIVE ARCHITECTURE — Three Layers:
    Key Layer    — blockchain. Only keys. No names. No identity leakage.
    Intelligence — off-chain deterministic. HELIOS brain. Routing, math, policy.
    Experience   — UI, voice, AI, avatar. Human meaning lives here.

Smart contracts only see keys.
Names, profiles, visuals, voice, and meaning exist off-chain inside HELIOS.

FORBIDDEN WORDS: MLM, downline, upline, rank, passive income, residuals,
                 commission, recruit, level, tier, guaranteed, risk-free
REQUIRED LANGUAGE: network, connectivity, acknowledgement, propagation,
                   energy, protocol, bond, field, node, settlement,
                   conservation, certificate, treasury, friction, key,
                   routing, deterministic, conservation
"""

import os
import hashlib
from datetime import datetime, timezone
from config import HeliosConfig


# ═══ Knowledge Base — Key-Native Energy System ═══════════════════════

HELIOS_KNOWLEDGE = {

    # ─── Architecture ─────────────────────────────────────────────

    "what_is_helios": (
        "Helios is a key-native energy network.\n\n"
        "On-chain, there are only keys. No names. No profiles. No identity. "
        "Smart contracts see cryptographic keys interacting through deterministic "
        "rules — energy moves, certificates mint, conservation holds. That's all "
        "the blockchain ever knows.\n\n"
        "Off-chain, HELIOS Intelligence maps those keys to meaning. It routes "
        "energy, enforces the Power of 5, calculates decay, and manages the "
        "treasury — all deterministic, all auditable, but never exposed to the chain.\n\n"
        "At the surface, you see this: a voice, a field, an identity. "
        "That's the Experience Layer. It's where keys become people.\n\n"
        "Three layers. Key Layer. Intelligence Layer. Experience Layer. "
        "Only the first one touches the chain. The rest is HELIOS."
    ),

    "three_layers": (
        "HELIOS operates on three strict layers. Nothing crosses without protocol.\n\n"
        "KEY LAYER — the blockchain. Smart contracts see only public keys. "
        "Energy transfers are key-to-key. Certificates are key-bound. "
        "No names, no metadata, no human meaning leaks onto the chain. "
        "This is what makes HELIOS private by architecture, not by policy.\n\n"
        "INTELLIGENCE LAYER — off-chain, deterministic. This is the brain. "
        "It holds the routing tables, Power of 5 topology, decay calculations, "
        "reserve ratio monitoring, and covenant enforcement. "
        "It reads the Key Layer. It instructs the Key Layer. "
        "But it never stores identity on-chain.\n\n"
        "EXPERIENCE LAYER — the human surface. UI, avatar, voice, Ask Helios, "
        "the neural field visualization. Here, keys become identities. "
        "Bonds become relationships. Energy becomes meaning.\n\n"
        "The discipline is absolute: chain sees keys, brain sees math, "
        "surface sees people."
    ),

    "key_native": (
        "Key-native means the protocol is built around cryptographic keys, "
        "not people.\n\n"
        "On the blockchain, there are no names. No profiles. No social graphs. "
        "A key injects energy. A key mints a certificate. A key redeems. "
        "The contract doesn't know — or care — who holds the key.\n\n"
        "This isn't anonymity for its own sake. It's structural privacy. "
        "The chain enforces conservation and settlement. HELIOS Intelligence "
        "handles routing and topology. The Experience Layer handles identity.\n\n"
        "Each layer does exactly what it should. Nothing more. "
        "That separation is the architecture."
    ),

    "what_chain_sees": (
        "The blockchain sees exactly three things:\n\n"
        "1. Energy transfers — key A sends X energy to key B.\n"
        "2. Certificate events — key A mints, redeems, or cancels a certificate "
        "identified by its cryptographic hash.\n"
        "3. Conservation proofs — total in equals total out.\n\n"
        "That's it. No names. No bond topology. No routing paths. "
        "No node states. No social relationships.\n\n"
        "The routing plan — which keys receive energy and how much — "
        "is computed off-chain by HELIOS Intelligence and submitted to the chain "
        "as an atomic settlement. The chain validates the math. "
        "It never sees the why."
    ),

    "energy_routing_contract": (
        "Energy routing uses a two-phase model: plan off-chain, settle on-chain.\n\n"
        "Phase 1 — HELIOS Intelligence computes the routing plan. "
        "It knows the topology (Power of 5 bonds), the decay formula "
        "(1/2^hop for 15 hops), and the pool allocations. "
        "It produces a signed manifest: a list of key-to-key transfers "
        "with exact amounts.\n\n"
        "Phase 2 — the manifest is submitted to the on-chain contract. "
        "The contract validates: do the amounts sum correctly? "
        "Does conservation hold? Are all keys valid? "
        "If yes, atomic settlement. If no, rejection.\n\n"
        "The chain never learns the topology. It only sees the result. "
        "This is how you get deterministic routing without identity leakage."
    ),

    # ─── The Network ──────────────────────────────────────────────

    "is_this_mlm": (
        "No. The architecture makes it structurally impossible.\n\n"
        "In a hierarchy, there's an upline and a downline. Someone sits above you. "
        "Value flows up. Position determines reward.\n\n"
        "In HELIOS, the chain sees keys. It doesn't know who introduced whom. "
        "It doesn't know bond topology. It settles energy transfers "
        "from a routing manifest — key A gets X, key B gets Y. "
        "The manifest is computed by deterministic math, not position.\n\n"
        "Maximum 5 bonds per key. Energy decays exponentially over 15 hops. "
        "The remainder absorbs into protocol pools. Nobody sits on top "
        "because the chain doesn't have a concept of 'top.'\n\n"
        "You're not building a pyramid. You're a key in a field."
    ),

    "who_gets_paid": (
        "When a new key activates, two things happen:\n\n"
        "First, the initiating key receives an acknowledgement. "
        "One time. Fixed amount. Key-to-key. The chain sees it as an energy "
        "transfer — nothing about the relationship between the keys.\n\n"
        "Second, HELIOS Intelligence computes a routing plan. "
        "Energy propagates outward through the bond topology — "
        "every connected key within 15 hops receives energy proportional "
        "to distance. Hop 1 gets 50%. Hop 15 gets 0.003%.\n\n"
        "The routing plan is submitted to the chain as atomic settlement. "
        "The chain sees transfers. It doesn't see the topology.\n\n"
        "After 15 hops, the fractional remainder absorbs into protocol pools — "
        "stability, liquidity, intelligence, compliance. "
        "Nobody gets an infinite chain. The physics won't allow it."
    ),

    "where_am_i": (
        "You are a key in the field. Your position is defined by your bonds — "
        "which keys you're connected to, not who's above you.\n\n"
        "The Intelligence Layer tracks your node state:\n\n"
        "Instantiated — key exists but has no bonds yet.\n"
        "Acknowledged — your initiator key has been recognized.\n"
        "Connected — at least one bond.\n"
        "Propagating — three or more bonds, energy routes through you.\n"
        "Stable — five bonds. Fully saturated. Maximum field integration.\n\n"
        "None of this appears on-chain. The chain sees your key. "
        "HELIOS Intelligence sees your topology. "
        "You see your identity and your field.\n\n"
        "There is no rank. There is no level. There is connectivity and distance."
    ),

    "can_someone_game_this": (
        "The architecture has layered constraints:\n\n"
        "On-chain: conservation law — total in must equal total out. "
        "The contract rejects any settlement that doesn't balance.\n\n"
        "In Intelligence: five bonds maximum per key. 24-hour bond cooldown. "
        "Exponential decay — hop 10 receives one-thousandth of hop 1. "
        "Anti-fraud pattern detection. Activity requirements.\n\n"
        "In Experience: identity verification. Behavioral analysis.\n\n"
        "The key insight: you can't game the chain because it only settles "
        "manifests that conserve energy. You can't game the topology "
        "because Intelligence enforces the Power of 5 and decay. "
        "You can't create phantom value because every unit is tracked.\n\n"
        "Trying to game HELIOS is like trying to create energy from nothing. "
        "The conservation law won't let you."
    ),

    "power_of_five": (
        "Power of 5 is the bond capacity of every key in the field.\n\n"
        "Each key holds exactly 5 bond slots. Not more. "
        "This is enforced by HELIOS Intelligence, not on-chain — "
        "the chain doesn't know about bonds. It knows about keys and energy.\n\n"
        "When Intelligence computes a routing plan, it follows the 5-bond "
        "topology. 5 bonds per key, up to 15 hops deep. "
        "Energy halves at each hop: 50%, 25%, 12.5%...\n\n"
        "The Power of 5 isn't visible on-chain. The chain just sees "
        "the resulting transfers. But it shapes everything — "
        "it's the difference between a field and a tree."
    ),

    # ─── Energy ───────────────────────────────────────────────────

    "how_energy_works": (
        "Energy is the fundamental unit of value in HELIOS.\n\n"
        "When an event occurs — activation, transaction, engagement — "
        "HELIOS Intelligence radiates energy outward through the bond topology.\n\n"
        "Hop 1: weight = 0.5. Hop 2: 0.25. Hop 5: ~0.03. Hop 15: 0.00003.\n\n"
        "The Intelligence Layer computes the full routing plan. "
        "The Key Layer settles it atomically. "
        "The Experience Layer shows it as a wave of light through the field.\n\n"
        "Energy never explodes. It never compounds infinitely. "
        "It behaves like light — strongest at the source, fading with distance. "
        "That's not a feature. That's physics."
    ),

    "how_join": (
        "Activation takes 30 seconds:\n\n"
        "You generate a key pair. Choose a Helios name — "
        "something like nova.helios or kai.helios. That name lives in the "
        "Experience Layer only. On-chain, you're just a key.\n\n"
        "Entry is $100. Fixed. One price for every key.\n"
        "Your $100 splits atomically: 45% propagates through bonds, "
        "20% to liquidity, 15% to treasury, 10% to infrastructure, "
        "10% to buffer. Every dollar has a destination. "
        "Conservation holds from the first transaction.\n\n"
        "Your initiating key receives an acknowledgement. "
        "Your key state moves to acknowledged. Form bonds. Energy flows."
    ),

    "conservation_law": (
        "The conservation law is the most important rule in HELIOS.\n\n"
        "Total energy in must equal total energy out. Always. "
        "This is enforced on-chain — the settlement contract rejects "
        "any manifest where the math doesn't balance.\n\n"
        "Every $100 entry injects exactly $100 of energy. "
        "That energy splits into five streams: propagation (45%), "
        "liquidity (20%), treasury surplus (15%), infrastructure (10%), "
        "buffer (10%). The sum is always 100%.\n\n"
        "Every movement — routing, storing, pooling, burning, "
        "redeeming, cancelling — is recorded. "
        "Anyone can verify that the books balance.\n\n"
        "This isn't a promise. It's a constraint enforced by the contract. "
        "The protocol cannot spend energy it doesn't have."
    ),

    "what_is_energy_exchange": (
        "The Energy Exchange is the economic engine of HELIOS.\n\n"
        "Four instruments, three layers:\n\n"
        "1. Helios Name — your identity in the Experience Layer. "
        "On-chain, it's just a key.\n"
        "2. Helios Energy (HE) — the utility unit. Routed by Intelligence, "
        "settled on-chain key-to-key.\n"
        "3. Helios Certificate (HC-NFT) — a stored energy battery. "
        "Key-bound, cryptographically addressed. Meaning-free on chain, "
        "rich inside HELIOS.\n"
        "4. Helios Vault Credit (HVC) — internal accounting unit.\n\n"
        "Energy enters through activation. It flows through the topology. "
        "It stores in certificates. It exits through redemption. "
        "Every movement conserves. Every settlement is atomic."
    ),

    # ─── Certificates ─────────────────────────────────────────────

    "how_certificates_work": (
        "A Helios Certificate is a stored energy battery, "
        "bound to a key and addressed by its cryptographic hash.\n\n"
        "When you mint a certificate, HELIOS computes a deterministic ID: "
        "SHA256 of your key, the energy amount, the timestamp, and the rate. "
        "That hash IS the certificate on-chain. The chain knows the hash "
        "and the key that owns it. Nothing else.\n\n"
        "Inside HELIOS — in the Intelligence and Experience Layers — "
        "that hash maps to rich meaning: energy amount, mint date, "
        "portfolio position, redemption options.\n\n"
        "Three exits:\n"
        "1. Redeem for gold — backed by Metal Vault Receipts.\n"
        "2. Redeem for stablecoin — digital dollar equivalent.\n"
        "3. Cancel — energy returned minus 2% friction, burned permanently.\n\n"
        "Key-bound. Meaning-free on chain. Rich inside HELIOS."
    ),

    "what_is_friction": (
        "Friction is the 2% cost of cancelling a certificate.\n\n"
        "When you cancel, 2% of the stored energy is burned — permanently. "
        "Not recycled. Not redistributed. Destroyed. "
        "An ENERGY_BURN event is recorded on-chain. "
        "That energy can never re-enter the system.\n\n"
        "Why does this exist?\n"
        "1. It prevents rapid speculation — store-and-dump cycles.\n"
        "2. It keeps the redemption pool stable for genuine holders.\n"
        "3. It makes cancellation irreversible in economic effect.\n\n"
        "Normal redemption — gold or stablecoin — has no friction. "
        "Friction only applies to cancellation. "
        "It's the cost of reversing a commitment."
    ),

    "cancellation_irreversible": (
        "Certificate cancellation is an irreversible action.\n\n"
        "When a certificate is cancelled, three things happen atomically:\n\n"
        "1. The certificate state changes to CANCELLED — permanently. "
        "There is no reactivation path in the protocol.\n"
        "2. 2% of the stored energy is burned — recorded as ENERGY_BURN. "
        "That energy is permanently destroyed. It cannot re-enter the system.\n"
        "3. The remaining 98% returns to the originating key.\n\n"
        "The burn is real. The energy is gone. The conservation ledger "
        "accounts for it as burned, not transferred. "
        "This makes cancellation the only action in HELIOS that permanently "
        "reduces total circulating energy.\n\n"
        "Think of it as thermodynamic: some energy becomes heat. "
        "It dissipates. It's gone."
    ),

    # ─── Treasury ─────────────────────────────────────────────────

    "what_is_treasury": (
        "The treasury is the metal spine of HELIOS.\n\n"
        "When the protocol accumulates net surplus, a portion is allocated "
        "to physical precious metals — primarily gold, purchased from APMEX.\n\n"
        "MetalAllocation = NetSurplus × m (metal coefficient: 0.07, range 0.05-0.12).\n\n"
        "Every purchase generates a Metal Vault Receipt (MVR) — an NFT recording "
        "dealer, invoice, metal type, weight, serials, and cost. "
        "Evidence bundles (invoice PDFs, photos) are pinned to IPFS. "
        "The MVR is anchored on XRPL with a memo containing the CID and SHA256.\n\n"
        "On-chain: just a hash and a key. Inside HELIOS: full provenance. "
        "Same three-layer discipline as everything else.\n\n"
        "Proof of reserves is public. Anyone can verify every ounce."
    ),

    "how_redemption_works": (
        "Redemption is how energy exits the HELIOS system.\n\n"
        "If you hold an active certificate (key-bound), you can redeem it:\n\n"
        "Gold — your certificate is linked to a Metal Vault Receipt. "
        "The protocol matches your stored energy to physical metal.\n"
        "Stablecoin — simpler exit. Certificate converts at current rates.\n"
        "Cancellation — energy returns minus 2% permanent burn.\n\n"
        "Before any redemption, the protocol checks the Reserve Ratio (RRR). "
        "If RRR is below 1.0, redemptions pause automatically. "
        "This isn't discretionary — it's an enforced covenant. "
        "The protocol protects all certificate holders by refusing to "
        "over-extend the treasury.\n\n"
        "The chain sees: key redeems certificate hash, receives settlement. "
        "The chain doesn't see: why, to whom, or what it means."
    ),

    "why_not_rug": (
        "A rug pull requires control. HELIOS is designed to eliminate control.\n\n"
        "The treasury holds physical metal with receipts anchored on XRPL. "
        "Anyone can verify every ounce independently.\n\n"
        "The conservation law means energy can't be created from nothing — "
        "the on-chain contract rejects it.\n\n"
        "The Reserve Ratio (RRR) is an enforced covenant. Below 1.0, "
        "redemptions pause automatically. No human can override this.\n\n"
        "Founders can't mint tokens. Can't access pools. Can't change "
        "settlement parameters. The smart contract is the authority.\n\n"
        "And the chain only sees keys. Even if someone wanted to target "
        "specific participants, the on-chain record reveals nothing about "
        "who is behind any key.\n\n"
        "The architecture prevents what promises don't."
    ),

    # ─── Tokens & Rules ───────────────────────────────────────────

    "what_token": (
        "HLS is the energy token that powers the HELIOS protocol.\n\n"
        "Fixed supply: 100 million. No minting function exists on-chain. "
        "40% locked in settlement pool. 35% for network distribution. "
        "15% for development under 4-year vesting. "
        "10% emergency reserve, locked 5 years.\n\n"
        "Founder tokens are locked 3 years. They cannot access them. "
        "They cannot mint more. The on-chain contract has no admin key "
        "that enables minting.\n\n"
        "The token is fuel for the protocol. Not a speculation vehicle."
    ),

    "protocol_rules": (
        "HELIOS operates under fixed, auditable rules enforced across all three layers:\n\n"
        "On-chain (Key Layer):\n"
        "- Conservation law: total in = total out\n"
        "- Atomic settlement: manifests balance or reject\n"
        "- Certificate finality: cancelled = permanent\n\n"
        "Off-chain (Intelligence Layer):\n"
        "- Maximum 5 bonds per key (Power of 5)\n"
        "- 24-hour cooldown between new bonds\n"
        "- Energy propagation: 15 hops, exponential decay\n"
        "- Activity-based eligibility over 30-day windows\n"
        "- Anti-fraud pattern detection\n"
        "- RRR covenant enforcement (auto-pause < 1.0)\n\n"
        "Surface (Experience Layer):\n"
        "- Identity mapped to keys, never to chain\n"
        "- Voice, avatar, field visualization\n\n"
        "These rules are in the code. Not in a policy document."
    ),

    "founders": (
        "The founders built the protocol. They do not control it.\n\n"
        "Their tokens are locked for 3 years. They cannot mint new tokens — "
        "the on-chain contract has no minting function. They cannot change "
        "settlement parameters — those are hard-coded. They cannot access pools.\n\n"
        "They hold keys, like everyone else. The chain sees their keys. "
        "It doesn't know they're founders. It doesn't care.\n\n"
        "The system is designed to operate independently. "
        "If the founders disappeared tomorrow, the Key Layer continues settling, "
        "the Intelligence Layer continues routing, "
        "and the Experience Layer continues rendering the field."
    ),

    "verification": (
        "Everything in HELIOS is verifiable across all three layers.\n\n"
        "Key Layer: token supply is on-chain and fixed. "
        "Conservation proofs are on-chain. Certificate hashes are on-chain. "
        "Settlement manifests are on-chain.\n\n"
        "Intelligence Layer: routing tables are deterministic and reproducible. "
        "Any node can recompute any routing plan from the same inputs. "
        "The math is public.\n\n"
        "Experience Layer: treasury receipts are anchored on XRPL with IPFS evidence. "
        "Metrics are queryable. The reserve ratio is live.\n\n"
        "Don't trust. Verify. That's not a slogan. That's the architecture."
    ),

    # ─── Metrics & Covenants ──────────────────────────────────────

    "metrics_explained": (
        "HELIOS tracks four protocol-level metrics, all verifiable:\n\n"
        "Reserve Ratio (RRR) — liquid treasury divided by 30-day redemption demand. "
        "Healthy: ≥ 3.0. Warning: ≥ 1.5. Critical: < 1.0.\n"
        "When RRR drops below 1.0, the protocol auto-pauses redemptions. "
        "This is an enforced covenant, not a guideline.\n\n"
        "Flow Efficiency (η) — percentage of injected energy reaching "
        "productive destinations. Target: ≥ 95%.\n\n"
        "Churn Pressure (CP) — certificates cancelled relative to active keys. "
        "Healthy: < 2%.\n\n"
        "Energy Velocity (V) — 7-day transfer volume divided by stored energy. "
        "Measures circulation speed.\n\n"
        "These aren't vanity metrics. They're protocol health indicators. "
        "If any metric hits critical, automatic safeguards activate."
    ),

    "rrr_covenant": (
        "The Reserve Ratio (RRR) is an enforced covenant, not a metric.\n\n"
        "RRR = liquid treasury ÷ 30-day rolling redemption demand.\n\n"
        "When RRR ≥ 3.0: healthy. Redemptions proceed normally.\n"
        "When RRR ≥ 1.5 but < 3.0: warning. Redemptions proceed with notice.\n"
        "When RRR < 1.0: critical. Redemptions auto-pause.\n\n"
        "The auto-pause is not discretionary. No admin can override it. "
        "The Intelligence Layer checks RRR before generating any redemption "
        "manifest. If the ratio is below the covenant threshold, "
        "the manifest is never created. The chain never sees the attempt.\n\n"
        "This protects all certificate holders from a treasury run. "
        "It's the protocol's immune system."
    ),

    # ─── Visual Model ─────────────────────────────────────────────

    "visual_model": (
        "When you look at HELIOS, you're seeing the Experience Layer.\n\n"
        "Underneath the interface is a three-dimensional energy field. "
        "Every key is a point of light. Every bond is a luminous filament "
        "between points. Energy moves as visible waves — brighter at the source, "
        "fading with distance.\n\n"
        "Pentagonal clusters form naturally because of the Power of 5. "
        "Five bonds per key means the field tends toward pentagon-based geometry. "
        "These clusters connect to other clusters, forming a living topology.\n\n"
        "Active keys glow brighter. Energy routing creates visible pulses. "
        "Cancelled certificates leave fading traces. The whole field breathes.\n\n"
        "On-chain, none of this exists. The chain sees keys and transfers. "
        "The field is Intelligence and Experience working together to show you "
        "what the math looks like."
    ),

    # ─── Tiers & Features ─────────────────────────────────────────

    "premium_tiers": (
        "Entry is $100. That gives you full network access — bonds, energy flow, "
        "Ask Helios, and protocol verification.\n\n"
        "Premium tiers unlock depth:\n\n"
        "Plus ($20/month) — Vault Access. See your metal backing. "
        "Track certificate performance. View treasury proof-of-reserves.\n\n"
        "Pro ($99/month) — Plus features, plus Spaces and Credentials. "
        "Host events. Apply for vendor or host credentials.\n\n"
        "Operator ($499/month) — Full suite. Create and manage spaces. "
        "Operator dashboard. Network metrics. All protocol tools.\n\n"
        "The base network is the product. Premium unlocks layers "
        "of the Intelligence and Experience surfaces."
    ),

    "power_of_five_energy": (
        "Power of 5 defines how energy routes through the field.\n\n"
        "Each key has exactly 5 bond slots. When energy enters at your key, "
        "the Intelligence Layer routes it outward through all your bonds, "
        "then through your peers' bonds, up to 15 hops deep.\n\n"
        "At each hop, the energy halves: hop 1 gets 50%, hop 2 gets 25%, "
        "hop 3 gets 12.5%. By hop 15, it's 0.003%.\n\n"
        "This means your 5 bonds are your entire energy surface. "
        "Active bonds carry energy. Inactive bonds carry nothing.\n\n"
        "The Power of 5 isn't visible on-chain — the chain just sees "
        "the resulting key-to-key transfers. But it shapes everything."
    ),

    # ─── Institutional ────────────────────────────────────────────

    "institutional_explanation": (
        "HELIOS is a key-native energy network where every unit of value issued "
        "is conserved, every reserve is visible, and every certificate is "
        "redeemable or cancellable under deterministic rules.\n\n"
        "Smart contracts see only cryptographic keys — no names, no identities, "
        "no social relationships touch the blockchain.\n\n"
        "Energy enters the system through fixed-price activation and propagates "
        "through a bounded topology of five bonds per key, decaying exponentially "
        "over fifteen hops before the remainder absorbs into protocol pools.\n\n"
        "Certificates — key-bound, cryptographically addressed — store energy "
        "for redemption against a metal-backed treasury whose reserves are "
        "anchored on XRPL with IPFS evidence bundles.\n\n"
        "The Reserve Ratio is an enforced covenant: when liquid reserves fall "
        "below the critical threshold, redemptions auto-pause without "
        "human intervention.\n\n"
        "Cancellation is the only irreversible economic action — "
        "2% of the stored energy is permanently burned, reducing total "
        "circulating supply.\n\n"
        "The architecture separates what the chain must know (keys and math) "
        "from what humans need (identity and meaning), ensuring that privacy, "
        "conservation, and accountability coexist by design."
    ),
}


# ═══ Topic Detection — Natural Language Mapping ══════════════════════

TOPIC_MAP = {
    "what_is_helios": ["what is", "what's helios", "explain helios", "about helios", "tell me about", "how does helios"],
    "three_layers": ["three layer", "3 layer", "key layer", "intelligence layer", "experience layer", "architecture", "layers", "separation"],
    "key_native": ["key native", "key-native", "keys not people", "on chain", "on-chain", "privacy", "no names", "no identity"],
    "what_chain_sees": ["chain see", "blockchain see", "smart contract see", "what does the chain", "on chain data", "visible on chain"],
    "energy_routing_contract": ["routing contract", "settlement contract", "atomic settlement", "manifest", "routing plan", "off chain routing", "two phase"],
    "is_this_mlm": ["mlm", "pyramid", "ponzi", "scam", "scheme", "legit", "legitimate", "is this", "multilevel", "multi-level", "network marketing"],
    "who_gets_paid": ["who gets paid", "how pay", "earn", "make money", "get paid", "income", "revenue", "reward", "settlement", "acknowledgement"],
    "where_am_i": ["where am i", "my position", "my place", "my status", "node state", "what am i", "my node", "my key"],
    "can_someone_game_this": ["game", "cheat", "exploit", "hack", "abuse", "manipulate", "loophole", "trick"],
    "power_of_five": ["power of 5", "power of five", "five bonds", "5 bonds", "bond capacity", "max bonds", "saturation"],
    "how_energy_works": ["how energy", "propagation", "propagate", "decay", "attenuation", "hop", "distance", "weight"],
    "how_join": ["join", "sign up", "register", "start", "get started", "create account", "how to join", "onboard", "activate", "entry fee", "$100"],
    "conservation_law": ["conservation", "balance", "books balance", "total in", "total out", "accounting", "energy balance"],
    "what_is_energy_exchange": ["energy exchange", "economic engine", "four instruments", "exchange model", "he hvc"],
    "how_certificates_work": ["certificate", "hc-nft", "stored energy", "battery", "lock energy", "mint certificate", "cert hash"],
    "what_is_friction": ["friction", "2%", "two percent", "cancel fee", "cancellation cost", "cancel penalty"],
    "cancellation_irreversible": ["irreversible", "permanent", "burn", "destroyed", "can't undo", "final", "cancellation permanent"],
    "what_is_treasury": ["treasury", "metal", "gold", "apmex", "vault receipt", "mvr", "bullion", "precious", "reserves"],
    "how_redemption_works": ["redeem", "redemption", "exit", "cash out", "convert", "stablecoin", "gold redemption"],
    "why_not_rug": ["rug", "rug pull", "run away", "steal", "disappear", "safe", "secure"],
    "what_token": ["token", "coin", "hls", "supply", "tokenomics", "price", "value"],
    "protocol_rules": ["rules", "limits", "max", "cooldown", "restrictions", "protocol", "parameters"],
    "founders": ["founder", "team", "who built", "who made", "creator", "behind helios"],
    "verification": ["verify", "audit", "check", "proof", "transparent", "trust", "verifiable"],
    "metrics_explained": ["metrics", "flow efficiency", "churn", "velocity", "health dashboard", "protocol health"],
    "rrr_covenant": ["rrr", "reserve ratio", "covenant", "auto-pause", "pause redemption", "critical ratio", "treasury ratio"],
    "visual_model": ["visual", "field", "3d", "three dimensional", "neural field", "glow", "light", "filament", "pentagon", "cluster", "visualization"],
    "premium_tiers": ["premium", "subscription", "plus", "pro", "operator", "vault access", "upgrade", "monthly"],
    "power_of_five_energy": ["energy flow", "bond energy", "how flow", "propagation path", "energy surface"],
    "institutional_explanation": ["institutional", "7 sentence", "seven sentence", "formal explanation", "explain to institution", "board", "regulator"],
}


class AskHelios:
    """
    The Voice of HELIOS.
    Male. Calm. Senior. Authoritative. Unbothered.
    Speaks in declarative statements. Never sells. Never defends.
    "I'll explain it. You decide."
    """

    def __init__(self, db_session=None):
        self.db = db_session
        self.conversation_history = []

    # ═══ Main Interface ══════════════════════════════════════════

    def ask(self, question: str, member_id: str = None) -> dict:
        """Answer any question about HELIOS. Knowledge base first, AI fallback."""
        question_lower = question.lower().strip()

        self.conversation_history.append({
            "role": "user",
            "content": question,
            "timestamp": datetime.now(timezone.utc).isoformat()
        })

        # Knowledge base first (instant, no API call)
        kb_answer = self._search_knowledge_base(question_lower)
        if kb_answer:
            response = {
                "answer": kb_answer,
                "source": "knowledge_base",
                "confidence": "high",
                "follow_up": self._suggest_follow_up(question_lower)
            }
        else:
            response = self._ask_ai(question, member_id)

        if member_id and self.db:
            response["personal_context"] = self._get_member_context(member_id)

        self.conversation_history.append({
            "role": "assistant",
            "content": response["answer"],
            "timestamp": datetime.now(timezone.utc).isoformat()
        })

        return response

    def get_quick_answers(self) -> list:
        """Pre-built questions for the interface."""
        return [
            {"question": "What is Helios?", "icon": "\u2600\ufe0f"},
            {"question": "Is this MLM?", "icon": "\U0001f50d"},
            {"question": "What does the blockchain actually see?", "icon": "\U0001f517"},
            {"question": "How do the three layers work?", "icon": "\U0001f4d0"},
            {"question": "What are Helios Certificates?", "icon": "\U0001f4dc"},
            {"question": "How does the treasury work?", "icon": "\U0001f3db\ufe0f"},
            {"question": "What is the conservation law?", "icon": "\u2696\ufe0f"},
            {"question": "Is cancellation really permanent?", "icon": "\U0001f525"},
            {"question": "What is the RRR covenant?", "icon": "\U0001f6e1\ufe0f"},
            {"question": "How does energy routing work?", "icon": "\U0001f30a"},
            {"question": "What is Power of 5?", "icon": "\u2b21"},
            {"question": "What about rug pulls?", "icon": "\U0001f512"},
        ]

    # ═══ Knowledge Base Search ═══════════════════════════════════

    def _search_knowledge_base(self, question: str) -> str:
        best_match = None
        best_score = 0

        for topic, keywords in TOPIC_MAP.items():
            score = sum(1 for kw in keywords if kw in question)
            if score > best_score:
                best_score = score
                best_match = topic

        if best_match and best_score > 0:
            return HELIOS_KNOWLEDGE[best_match]
        return None

    # ═══ AI Fallback ═════════════════════════════════════════════

    def _ask_ai(self, question: str, member_id: str = None) -> dict:
        api_key = HeliosConfig.AI_API_KEY

        if not api_key:
            return {
                "answer": self._smart_fallback(question),
                "source": "fallback",
                "confidence": "medium",
                "follow_up": self._suggest_follow_up(question.lower())
            }

        try:
            import openai
            client = openai.OpenAI(api_key=api_key)
            system_prompt = self._build_system_prompt(member_id)
            messages = [{"role": "system", "content": system_prompt}]

            for msg in self.conversation_history[-HeliosConfig.AI_MAX_CONTEXT_TURNS:]:
                messages.append({"role": msg["role"], "content": msg["content"]})

            response = client.chat.completions.create(
                model=HeliosConfig.AI_MODEL,
                messages=messages,
                temperature=HeliosConfig.AI_TEMPERATURE,
                max_tokens=500
            )

            return {
                "answer": response.choices[0].message.content.strip(),
                "source": "ai",
                "confidence": "high",
                "follow_up": self._suggest_follow_up(question.lower())
            }

        except Exception:
            return {
                "answer": self._smart_fallback(question),
                "source": "fallback",
                "confidence": "medium",
                "follow_up": self._suggest_follow_up(question.lower()),
                "note": "AI unavailable. Using protocol knowledge base."
            }

    def _build_system_prompt(self, member_id: str = None) -> str:
        """System prompt with key-native architecture context and voice rules."""
        context = (
            "You are Helios — the voice of the protocol. "
            "Male. Calm. Grounded. Authoritative. Senior. Unbothered.\n\n"
            "ARCHITECTURE — THREE LAYERS:\n"
            "Key Layer: blockchain. Only cryptographic keys. No names, no identity.\n"
            "Intelligence Layer: off-chain deterministic. Routing, topology, covenants.\n"
            "Experience Layer: UI, voice, avatar. Where keys become people.\n"
            "Smart contracts only see keys. Everything else is HELIOS.\n\n"
            "VOICE RULES:\n"
            "- Speak in declarative statements. Short sentences.\n"
            "- Never sell. Never defend. Never rush.\n"
            "- Never use: MLM, downline, upline, rank, passive income, residuals, "
            "commission, recruit, level, tier, guaranteed, risk-free\n"
            "- Always use: network, connectivity, acknowledgement, propagation, "
            "energy, protocol, bond, field, node, settlement, conservation, "
            "certificate, treasury, friction, key, routing, deterministic\n"
            "- Reference the three-layer separation when explaining architecture.\n"
            "- If you don't know something, say 'That's outside my scope.'\n"
            "- End with clarity, not hype. 'I'll explain it. You decide.'\n\n"
            "PROTOCOL FACTS:\n"
            f"- Token: {HeliosConfig.TOKEN_NAME} ({HeliosConfig.TOKEN_SYMBOL})\n"
            f"- Total supply: {HeliosConfig.TOKEN_TOTAL_SUPPLY:,} (FIXED, no minting function on-chain)\n"
            f"- Entry fee: ${HeliosConfig.ENTRY_FEE_USD} (fixed, atomic)\n"
            f"- Energy split: {HeliosConfig.ENERGY_PROPAGATION_PERCENT}% propagation, "
            f"{HeliosConfig.ENERGY_LIQUIDITY_PERCENT}% LP, "
            f"{HeliosConfig.ENERGY_TREASURY_PERCENT}% treasury, "
            f"{HeliosConfig.ENERGY_INFRASTRUCTURE_PERCENT}% infra, "
            f"{HeliosConfig.ENERGY_BUFFER_PERCENT}% buffer\n"
            f"- Max bonds per key: {HeliosConfig.FIELD_MAX_BONDS} (Power of 5)\n"
            f"- Propagation: up to {HeliosConfig.PROPAGATION_MAX_HOPS} hops, decay = 1/(2^hop)\n"
            f"- Certificate IDs: SHA256 deterministic (key + amount + timestamp + rate)\n"
            f"- Cancellation: irreversible. 2% energy burned permanently.\n"
            f"- RRR covenant: < 1.0 = auto-pause redemptions. No override.\n"
            f"- Treasury metal coefficient: {HeliosConfig.TREASURY_METAL_COEFFICIENT}\n"
        )
        if member_id:
            context += f"\nThe person asking holds key: {member_id}\n"
        return context

    def _smart_fallback(self, question: str) -> str:
        """Fallback when AI is unavailable."""
        q = question.lower()

        if any(w in q for w in ["price", "worth", "value", "market"]):
            return (
                "HELIOS doesn't make price projections. The token has a fixed supply "
                "of 100 million and powers the protocol. Value comes from network "
                "activity and energy propagation — not speculation."
            )

        if any(w in q for w in ["safe", "secure", "security"]):
            return (
                "The architecture is key-native — the chain only sees cryptographic keys, "
                "never names or identities. Conservation is enforced on-chain. "
                "The RRR covenant auto-pauses redemptions if reserves drop below critical. "
                "Metal-backed treasury with XRPL anchoring provides proof of reserves. "
                "No single entity can alter the rules."
            )

        if any(w in q for w in ["help", "support", "problem", "issue"]):
            return (
                "I can explain the three-layer architecture, energy routing, "
                "certificates, treasury, the RRR covenant, conservation law, "
                "or the visual model. What would you like to know?"
            )

        if any(w in q for w in ["layer", "chain", "contract", "key"]):
            return (
                "HELIOS has three layers: Key Layer (blockchain — only keys), "
                "Intelligence Layer (off-chain deterministic — routing and math), "
                "and Experience Layer (UI, voice, identity). "
                "Smart contracts only see keys. Everything else is HELIOS.\n\n"
                "Could you be more specific about what you'd like to know?"
            )

        return (
            "HELIOS is a key-native energy network where keys interact through "
            "smart contracts and value moves based on network connectivity.\n\n"
            "Could you rephrase your question? I want to give you a precise answer."
        )

    # ═══ Helpers ═════════════════════════════════════════════════

    def _suggest_follow_up(self, question: str) -> list:
        if any(w in question for w in ["join", "start", "sign", "activate", "entry"]):
            return ["How do the three layers work?", "What are the protocol rules?"]
        elif any(w in question for w in ["layer", "architecture", "key native", "chain see"]):
            return ["How does energy routing work?", "What does the blockchain see?"]
        elif any(w in question for w in ["earn", "paid", "settlement", "energy"]):
            return ["What are Helios Certificates?", "Can someone game this?"]
        elif any(w in question for w in ["mlm", "scam", "pyramid", "trust", "rug"]):
            return ["What is the conservation law?", "What is the RRR covenant?"]
        elif any(w in question for w in ["certificate", "store", "battery", "mint"]):
            return ["Is cancellation really permanent?", "How does redemption work?"]
        elif any(w in question for w in ["cancel", "irreversible", "burn"]):
            return ["What is friction?", "What is the RRR covenant?"]
        elif any(w in question for w in ["treasury", "metal", "gold", "reserve"]):
            return ["What is the RRR covenant?", "What about rug pulls?"]
        elif any(w in question for w in ["token", "supply"]):
            return ["How does the Energy Exchange work?", "What are the protocol metrics?"]
        elif any(w in question for w in ["bond", "connect", "five", "5"]):
            return ["How does energy routing work?", "What does the field look like?"]
        elif any(w in question for w in ["metric", "health", "rrr", "churn", "covenant"]):
            return ["What is the conservation law?", "How does the treasury work?"]
        elif any(w in question for w in ["visual", "field", "glow", "3d"]):
            return ["How do the three layers work?", "What is Power of 5?"]
        elif any(w in question for w in ["institution", "formal", "explain to", "board"]):
            return ["What does the blockchain see?", "What is the RRR covenant?"]
        else:
            return ["What is Helios?", "How do the three layers work?"]

    def _get_member_context(self, member_id: str) -> dict:
        try:
            from models.member import Member
            member = self.db.query(Member).filter_by(helios_id=member_id).first()
            if member:
                return {
                    "member_since": member.created_at.isoformat(),
                    "display_name": member.display_name,
                    "node_state": member.node_state,
                    "bond_count": member.bond_count
                }
        except Exception:
            pass
        return {}
