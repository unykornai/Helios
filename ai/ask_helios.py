"""
Ask Helios — The Voice
════════════════════════════════════════════════════════
Male. Calm. Grounded. Authoritative. Never salesy. Never defensive.
Explains money like a real person at a kitchen table.
"I'll explain it. You decide."

HELIOS PROTOCOL — Gold-Backed Allocation on Web3 Rails:
    5 membership tiers: $100 / $250 / $500 / $1,000 / $5,000
    3 ways to earn: Direct Introduction Allocation, 15-Level Engine, Gold & Crypto
    Allocation formula: W_L = 0.50 × 0.5^(L-1) across 15 levels
    Treasury: Physical gold via APMEX, NFT certificates on XRPL + Stellar
    Depth chart: Position 1 → Position 2 → Position 3 → Network

TONE: Adult. Calm. Grounded. Kitchen-table money talk.
      Not hype. Not crypto jargon. Just math and facts.

COMPLIANCE: No income guarantees. No promises. Results depend on effort.
            Earnings shown are mathematical projections, not guarantees.
"""

import os
import hashlib
from datetime import datetime, timezone
from config import HeliosConfig


# ═══ Knowledge Base — 5-Tier Gold-Backed Allocation Protocol ═════════

HELIOS_KNOWLEDGE = {

    # ─── What It Is ───────────────────────────────────────────────

    "what_is_helios": (
        "Helios is a gold-backed allocation protocol on Web3 rails.\n\n"
        "You pick a membership tier — $100, $250, $500, $1,000, or $5,000. "
        "One payment. No monthly fees. No autoship. No product to buy.\n\n"
        "Your membership fee enters a published pipeline. 45% goes into a "
        "15-level allocation engine that pays everyone in your network based "
        "on a math formula. 15% buys physical gold through APMEX. "
        "20% funds the liquidity pool. The rest covers operations.\n\n"
        "You get a .helios identity, gold-backed NFT certificates on XRPL "
        "and Stellar, access to BTC, ETH, XRP, and stablecoins, and a "
        "15-level network that pays you every time someone joins.\n\n"
        "No ranks. No titles. No monthly quota. Just math, gold, and people."
    ),

    "five_tiers": (
        "There are 5 membership tiers. One payment. No monthly fees.\n\n"
        "Starter — $100. Multiplier: 1×. Allocation pool: $45. "
        "Direct introduction allocation: $22.50 per member.\n\n"
        "Builder — $250. Multiplier: 2.5×. Allocation pool: $112.50. "
        "Direct introduction allocation: $56.25 per member.\n\n"
        "Pro — $500. Multiplier: 5×. Allocation pool: $225. "
        "Direct introduction allocation: $112.50 per member.\n\n"
        "Leader — $1,000. Multiplier: 10×. Allocation pool: $450. "
        "Direct introduction allocation: $225 per member.\n\n"
        "Executive — $5,000. Multiplier: 50×. Allocation pool: $2,250. "
        "Direct introduction allocation: $1,125 per member.\n\n"
        "Higher tier = bigger pool = bigger allocations at every level. "
        "Same formula. Same structure. Just bigger numbers."
    ),

    "three_ways_to_earn": (
        "There are exactly three allocation channels in Helios.\n\n"
        "1. DIRECT INTRODUCTION ALLOCATION — every member you personally introduce "
        "generates an immediate allocation. That's 50% of your allocation pool. "
        "At $100 tier, that's $22.50. At $5,000, that's $1,125. Per member.\n\n"
        "2. THE 15-LEVEL ENGINE — 45% of every membership in your "
        "network goes into a pool. That pool distributes across 15 levels using "
        "a published formula. Level 1 gets 50%, Level 2 gets 25%, "
        "Level 3 gets 12.5%, and so on. You receive allocations from members you never "
        "even met — because your network connected them.\n\n"
        "3. GOLD, NFTs, AND CRYPTO — part of every membership buys "
        "physical gold. You get gold-backed NFT certificates. You can "
        "convert to BTC, ETH, XRP, stablecoins, or hold physical metal. "
        "Plus staking bonuses from 5% to 30%.\n\n"
        "No ranks. No quotas. No monthly. Just these three channels."
    ),

    # ─── Direct Referrals ─────────────────────────────────────────

    "direct_referral": (
        "The direct introduction allocation is the simplest channel. You introduce a member, "
        "you receive an allocation. That day.\n\n"
        "The allocation is 50% of your allocation pool — which is 45% of the "
        "membership fee. Here's what that looks like by tier:\n\n"
        "Starter ($100) → $22.50 per introduction\n"
        "Builder ($250) → $56.25 per introduction\n"
        "Pro ($500) → $112.50 per introduction\n"
        "Leader ($1,000) → $225.00 per introduction\n"
        "Executive ($5,000) → $1,125.00 per introduction\n\n"
        "Introduce 5 members at the $100 tier and you've received $112.50. "
        "Introduce 5 at the $5,000 tier and that's $5,625.\n\n"
        "This is just Channel #1. The 15-level engine and gold/crypto "
        "are separate allocation channels on top of this."
    ),

    # ─── 15-Level Engine ──────────────────────────────────────────

    "fifteen_level_engine": (
        "The 15-level engine is where the real scale lives.\n\n"
        "Every membership sends 45% into an allocation pool. That pool "
        "gets distributed across 15 levels using this formula:\n\n"
        "Weight at Level L = 0.50 × 0.5^(L-1)\n\n"
        "Level 1: 50.0% of the pool — that's your direct introductions.\n"
        "Level 2: 25.0%\n"
        "Level 3: 12.5%\n"
        "Level 4: 6.25%\n"
        "Level 5: 3.125%\n"
        "Level 6: 1.5625%\n"
        "Level 7: 0.781%\n"
        "...all the way down to Level 15.\n\n"
        "The dollar amounts per member get smaller at deeper levels. "
        "But the number of members gets exponentially larger. "
        "5 members at Level 1. 25 at Level 2. 125 at Level 3. "
        "By Level 7 you could have 78,125 members.\n\n"
        "Small per member × substantial volume = real allocations. That's the engine."
    ),

    "allocation_formula": (
        "The allocation formula is published and deterministic. Nobody decides "
        "who gets what — the math does.\n\n"
        "W_L = 0.50 × 0.5^(L-1)\n\n"
        "That means each level gets half the weight of the level above it. "
        "Level 1 = 50%. Level 2 = 25%. Level 3 = 12.5%. And so on.\n\n"
        "The pool is 45% of the membership fee:\n"
        "$100 tier → $45 pool\n"
        "$250 tier → $112.50 pool\n"
        "$500 tier → $225 pool\n"
        "$1,000 tier → $450 pool\n"
        "$5,000 tier → $2,250 pool\n\n"
        "Each member's entry creates a new allocation event. "
        "The formula runs. Everyone in the 15-level chain gets their cut. "
        "Automatically. No human decision involved."
    ),

    # ─── Depth Chart ──────────────────────────────────────────────

    "depth_chart": (
        "Think of the depth chart like a chain. Three positions.\n\n"
        "POSITION 1 — sits at the top. They joined and introduced members. "
        "Those members (Position 2) introduced more members (Position 3). "
        "Position 1 earns from the whole tree below them, but they're "
        "further from the action, so per-member amounts are smaller.\n\n"
        "POSITION 2 — in the middle. They were introduced by Position 1 "
        "and they introduced Position 3 and their members. "
        "Position 2 earns from everyone below them.\n\n"
        "POSITION 3 — closest to the action. They did the direct work, "
        "introduced the members, and their members duplicated. "
        "Position 3 receives the most because they're closest "
        "to the newest activity.\n\n"
        "Everybody receives allocations. Position 3 just receives the most. "
        "The formula rewards the person doing the work."
    ),

    "fifty_k_scenario": (
        "Here's a real scenario. 50,000-member network. Base $100 tier.\n\n"
        "POSITION 3 (did the work):\n"
        "Levels 1-7 of their network build from 5 → 25 → 125 → 625 → "
        "3,125 → 15,625 → 31,250 members. Total allocation from the "
        "engine: $28,730 per month. That's $344,766 per year.\n\n"
        "POSITION 2 (above Position 3):\n"
        "Same structure, but they're one level further from the newest joins. "
        "$14,502 per month. $174,034 per year.\n\n"
        "POSITION 1 (top of structure):\n"
        "$7,326 per month. $87,924 per year.\n\n"
        "WITH 30% STAKING BONUS:\n"
        "Position 3: $448,195/yr. Position 2: $226,244/yr. "
        "Position 1: $114,301/yr.\n\n"
        "WITH MIXED TIERS (people choosing $250-$5,000):\n"
        "Position 3 crosses $1 million per year. "
        "Position 2 crosses $500k. Position 1 crosses $250k.\n\n"
        "These are mathematical projections based on the formula. "
        "Results depend on the work you and your network put in."
    ),

    # ─── Where Your Money Goes ────────────────────────────────────

    "allocation_split": (
        "Every membership fee splits the same way. Every tier. No exceptions.\n\n"
        "45% — Network Allocation. This is the 15-level engine. "
        "It's the pool that pays everyone in the chain above you.\n\n"
        "20% — Liquidity Pool. Ensures certificates can always be redeemed. "
        "You want to cash out your gold certificates? This pool backs that.\n\n"
        "15% — Treasury. Physical gold purchases through APMEX. "
        "Real metal. Real receipts. Real vaults.\n\n"
        "10% — Infrastructure. Servers, compliance, operations, development.\n\n"
        "10% — Protocol Buffer. Emergency reserves.\n\n"
        "That's 100%. Every dollar accounted for. No slush fund. "
        "No mystery bucket. The math is published."
    ),

    # ─── Gold & Crypto ────────────────────────────────────────────

    "gold_backing": (
        "Part of every membership buys physical gold. Real metal. Not paper.\n\n"
        "15% of every fee goes to the treasury, which purchases gold through "
        "APMEX — one of the largest precious metals dealers in the world.\n\n"
        "With 50,000 members at the $100 tier, that's $750,000 in physical "
        "gold purchased. Higher tiers scale that number significantly.\n\n"
        "Every purchase generates a Metal Vault Receipt — an NFT on XRPL "
        "recording the dealer, invoice, metal type, weight, and serial numbers. "
        "Evidence is pinned to IPFS. Anyone can verify every ounce.\n\n"
        "You receive gold-backed NFT certificates. These represent actual "
        "gold weight. You can redeem for physical gold, physical silver, "
        "or convert to stablecoins.\n\n"
        "Your wealth is backed by something you can hold in your hand."
    ),

    "crypto_access": (
        "Your allocations aren't stuck in one asset. You have options.\n\n"
        "BTC — Bitcoin. The original. Store of value.\n"
        "ETH — Ethereum. Smart contract backbone.\n"
        "XRP — Ripple. Fast cross-border settlement.\n"
        "XLM — Stellar. Low-cost transfers.\n"
        "USDC — Circle stablecoin. Pegged to the dollar.\n"
        "USDT — Tether stablecoin. Most liquid stablecoin.\n\n"
        "Plus physical gold (Au) and physical silver (Ag) through "
        "the treasury.\n\n"
        "You can convert your certificates into any of these. "
        "Build a portfolio across multiple asset classes. "
        "Diversify the way institutions do — not the way retail usually can.\n\n"
        "Helios runs on XRPL and Stellar. Two of the fastest, cheapest "
        "settlement networks in crypto. Your transactions settle in seconds."
    ),

    "certificate_staking": (
        "Staking lets you lock your certificates for bonus allocations.\n\n"
        "30 days → +5% bonus\n"
        "90 days → +12% bonus\n"
        "180 days → +20% bonus\n"
        "365 days → +30% bonus\n\n"
        "You're not lending your certificates to anyone. You're locking them "
        "in the protocol and earning bonus allocations on top of your "
        "existing earnings.\n\n"
        "Example: Position 3 in a 50K network earns $344,766/year. "
        "With 365-day staking, that becomes $448,195. "
        "That's an extra $103,000 just for holding.\n\n"
        "Staking is optional. Your certificates, your choice. "
        "But the math rewards patience."
    ),

    "nft_certificates": (
        "Helios Certificates are NFTs on XRPL, backed by physical gold.\n\n"
        "When you earn through the network or buy in through a tier, "
        "you receive certificates. Each one is a unique NFT with a "
        "deterministic ID — SHA256 of your identity, the amount, "
        "timestamp, and rate.\n\n"
        "What can you do with them?\n\n"
        "1. Hold — your certificate represents gold weight in the treasury.\n"
        "2. Redeem for gold — actual physical metal shipped to you.\n"
        "3. Redeem for silver — physical silver, same process.\n"
        "4. Convert to stablecoin — USDC or USDT equivalent.\n"
        "5. Convert to crypto — BTC, ETH, XRP, or XLM.\n"
        "6. Stake — lock for 30-365 days, earn bonus allocations.\n\n"
        "They're not points. They're not credits. They're assets."
    ),

    # ─── Is This MLM / Pyramid ────────────────────────────────────

    "is_this_mlm": (
        "Let me be direct. This is a network-based allocation protocol. "
        "It pays across 15 levels using a published math formula. "
        "That structure looks similar to network marketing on the surface.\n\n"
        "Here's what makes it different:\n\n"
        "No ranks. Nobody is a 'Diamond' or a 'Director.' There's no "
        "title system. The formula doesn't care about your label.\n\n"
        "No monthly fees. You pay once. That's it. There's no autoship. "
        "There's no monthly qualifier. There's no re-enrollment.\n\n"
        "No product to push. There's no juice, supplements, or skincare. "
        "The protocol allocates gold and crypto. Real assets.\n\n"
        "No forced purchases. You don't buy inventory. You don't maintain "
        "a minimum. You don't qualify by spending.\n\n"
        "The math is published. The formula is on the site. Anyone can "
        "verify the payouts before they join.\n\n"
        "Call it what you want. The math is the math."
    ),

    "no_bs_list": (
        "Here's what Helios does NOT do:\n\n"
        "1. No ranks. No titles. No 'Diamond Director Elite.'\n"
        "2. No monthly fees. One payment. Done.\n"
        "3. No autoship. Nothing shows up at your door you didn't ask for.\n"
        "4. No product to push. No juice. No supplements.\n"
        "5. No re-qualifying. You don't lose your position.\n"
        "6. No minimum volume. No PV/BV/GV requirements.\n"
        "7. No forced upgrades. Your tier is your tier.\n"
        "8. No meetings you have to attend. No conventions you have to buy.\n"
        "9. No hidden fees. The allocation formula is published.\n"
        "10. No promises. The math is real. Results depend on effort.\n\n"
        "One payment. Published math. Real assets. "
        "That's it. Everything else is noise."
    ),

    # ─── How to Join ──────────────────────────────────────────────

    "how_to_join": (
        "Joining takes about two minutes.\n\n"
        "Step 1 — Pick your tier. $100, $250, $500, $1,000, or $5,000. "
        "Higher tier means bigger allocation pool and bigger introduction "
        "allocations. All tiers get the same structure and access.\n\n"
        "Step 2 — Pay once. One transaction. No recurring charges. "
        "Your fee splits automatically: 45% to the network engine, "
        "15% to gold treasury, 20% to liquidity, the rest to operations.\n\n"
        "Step 3 — Get your .helios identity. Something like nova.helios "
        "or king.helios. That's yours permanently.\n\n"
        "Step 4 — Receive your first certificate allocation and full "
        "protocol access including crypto tools and the AI guide.\n\n"
        "Step 5 — Introduce 5 members. Help your 5 connect their 5. "
        "Let the 15-level formula handle the rest.\n\n"
        "No application. No approval process. No waiting period."
    ),

    "what_you_receive": (
        "When you activate at any tier, here's what you get:\n\n"
        "1. Your .helios identity — a permanent namespace like yourname.helios. "
        "That's your on-chain identity in the protocol.\n\n"
        "2. Gold-backed NFT certificates — real digital assets backed by "
        "physical gold in the treasury. Redeemable.\n\n"
        "3. 15-level network access — every member who joins through your "
        "network generates allocations across 15 levels automatically.\n\n"
        "4. Crypto tools — convert to BTC, ETH, XRP, XLM, USDC, USDT. "
        "Build your portfolio.\n\n"
        "5. Certificate staking — lock for 30 to 365 days, earn 5-30% "
        "bonus allocations.\n\n"
        "6. Full protocol access — treasury verification, allocation model, "
        "AI advisory, AI guide, and live network metrics.\n\n"
        "7. The Helios AI — that's me. Available 24/7 to walk you through "
        "the math, the assets, or anything else.\n\n"
        "All tiers get full access. Higher tiers just get bigger numbers."
    ),

    # ─── Web3 / Technical ─────────────────────────────────────────

    "web3_rails": (
        "Helios runs on two blockchains: XRPL and Stellar.\n\n"
        "XRPL (XRP Ledger) — handles NFT certificates and Metal Vault "
        "Receipts. Fast settlement. Low fees. Battle-tested since 2012.\n\n"
        "Stellar — handles stablecoin operations and cross-asset settlement. "
        "Built for financial rails. Used by major institutions.\n\n"
        "Why two chains? Each does what it does best. XRPL for certificates "
        "and proof of reserves. Stellar for fast, cheap value transfer.\n\n"
        "Your allocations settle on-chain. Your certificates are verifiable. "
        "The treasury receipts are anchored with IPFS evidence bundles. "
        "Anyone can verify the gold holdings independently.\n\n"
        "This isn't 'we use blockchain.' The protocol actually lives on-chain."
    ),

    "treasury": (
        "The treasury is physical gold. Real metal in real vaults.\n\n"
        "15% of every membership fee goes to the treasury fund. "
        "That fund purchases gold through APMEX — one of the largest "
        "precious metals dealers in the United States.\n\n"
        "Every purchase creates a Metal Vault Receipt — an NFT on XRPL "
        "with the dealer name, invoice number, metal type, weight, "
        "serial numbers, and cost. Evidence bundles (invoices, photos) "
        "are pinned to IPFS.\n\n"
        "With 50,000 members at $100, the treasury holds $750,000 in gold. "
        "With mixed tiers ($250-$5,000), that number scales dramatically.\n\n"
        "Proof of reserves is public. Always. That's the deal.\n\n"
        "Your earnings aren't backed by promises. They're backed by metal."
    ),

    "verification": (
        "Everything in Helios is verifiable.\n\n"
        "The allocation formula is published: W_L = 0.50 × 0.5^(L-1). "
        "Anyone can run the math before they join.\n\n"
        "The fee split is published: 45% network, 20% liquidity, "
        "15% treasury, 10% infrastructure, 10% buffer.\n\n"
        "The treasury receipts are on XRPL. Metal Vault Receipts are NFTs. "
        "Evidence is on IPFS. Anyone can verify every ounce of gold.\n\n"
        "Certificate IDs are deterministic — SHA256 hashes. "
        "You can independently verify your certificates.\n\n"
        "Network metrics are live and queryable.\n\n"
        "If someone tells you to 'just trust them,' walk away. "
        "In Helios, you verify. The math is public. The gold is real. "
        "The receipts are on-chain."
    ),

    # ─── Risk & Honesty ───────────────────────────────────────────

    "risks": (
        "I'll be straight with you because that's how this works.\n\n"
        "Your earnings depend on building a network. If you join and don't "
        "introduce anyone, you'll receive your certificates and gold allocation "
        "from your own membership, but the 15-level engine needs members.\n\n"
        "The numbers I show — $28,730/month, $344,766/year — those are "
        "mathematical projections based on a 50,000-person network at $100 tier. "
        "Real results depend on how many members you introduce, how well they "
        "duplicate, and what tiers they choose.\n\n"
        "Gold prices fluctuate. Crypto prices fluctuate. The protocol "
        "holds real assets, but asset values move.\n\n"
        "This isn't a savings account. It's not a guaranteed return. "
        "It's a network-based protocol that rewards effort and math.\n\n"
        "The formula is real. The gold is real. But the work is on you."
    ),

    "why_not_rug": (
        "The treasury holds physical gold with receipts on XRPL. "
        "Anyone can verify every ounce independently.\n\n"
        "The allocation formula is published. No one decides allocations — "
        "the math does.\n\n"
        "There are no admin keys that let someone change the rules "
        "or drain the pools.\n\n"
        "The fee split is hardcoded: 45/20/15/10/10. "
        "It can't be altered after the fact.\n\n"
        "There's no token that can be dumped. No pre-mine. "
        "No insider allocation waiting to crash the price.\n\n"
        "The protocol is designed so that pulling the rug is architecturally "
        "impossible. Not 'we promise we won't.' The code won't let it happen.\n\n"
        "Verify the gold. Verify the math. That's all I ask."
    ),

    # ─── Token ────────────────────────────────────────────────────

    "what_token": (
        "HLS is the protocol token that powers Helios.\n\n"
        "Fixed supply: 100 million. No minting function. Nobody can create more.\n\n"
        "40% — locked in the settlement pool for network operations.\n"
        "35% — network distribution as the protocol grows.\n"
        "15% — development, under 4-year vesting.\n"
        "10% — emergency reserve, locked 5 years.\n\n"
        "Founder tokens are locked 3 years. They can't touch them. "
        "They can't mint more. The contract doesn't have that function.\n\n"
        "The token facilitates protocol operations. It's not a speculation "
        "instrument. The value is in the network, the gold, and the certificates."
    ),

    # ─── Protocol Rules ───────────────────────────────────────────

    "protocol_rules": (
        "Helios runs on fixed rules. No exceptions. No overrides.\n\n"
        "ALLOCATION:\n"
        "- 5 tiers: $100 / $250 / $500 / $1,000 / $5,000\n"
        "- 45% of every fee enters the 15-level engine\n"
        "- Formula: W_L = 0.50 × 0.5^(L-1)\n"
        "- 5 introductions per member. That's the width.\n"
        "- 15 levels deep. That's the depth.\n\n"
        "TREASURY:\n"
        "- 15% buys physical gold through APMEX\n"
        "- Metal Vault Receipts on XRPL\n"
        "- Proof of reserves is always public\n\n"
        "CERTIFICATES:\n"
        "- Gold-backed NFTs on XRPL\n"
        "- Redeemable for gold, silver, or stablecoins\n"
        "- Staking: 30d = +5%, 90d = +12%, 180d = +20%, 365d = +30%\n\n"
        "INTEGRITY:\n"
        "- No admin override keys\n"
        "- Conservation law: total in = total out\n"
        "- Published formula — anyone can verify before joining"
    ),

    "founders": (
        "The founders built the protocol. They don't control it.\n\n"
        "Their tokens are locked 3 years. They can't mint more — "
        "the contract doesn't have a minting function. They can't change "
        "the allocation formula. They can't access the pools.\n\n"
        "They hold a .helios identity like everyone else. "
        "They earn through the same formula as everyone else.\n\n"
        "If the founders disappeared tomorrow, the protocol keeps running. "
        "The formula keeps calculating. The treasury keeps holding gold. "
        "The certificates keep their value.\n\n"
        "That's the point. The system works because it doesn't need "
        "any one person to keep it running."
    ),

    # ─── Earning Comparisons ──────────────────────────────────────

    "earning_examples": (
        "Let me give you some real numbers. All based on the published formula.\n\n"
        "5 PEOPLE at $100 tier:\n"
        "Direct introduction: 5 × $22.50 = $112.50\n"
        "Level 1 engine: 5 × $22.50 = $112.50\n"
        "Total from just your 5: $225\n\n"
        "25 PEOPLE (your 5 each bring 5) at $100:\n"
        "You now earn from Level 1 (5 people) AND Level 2 (25 people).\n"
        "Level 1: $112.50. Level 2: 25 × $11.25 = $281.25.\n"
        "Running total: $506.25\n\n"
        "125 PEOPLE (Level 3) at $100:\n"
        "Level 3: 125 × $5.625 = $703.13\n"
        "Running total: $1,209.38\n\n"
        "It keeps going. The deeper it gets, the more people there are, "
        "and even though per-person amounts get smaller, the volume "
        "makes up for it.\n\n"
        "Now imagine those people chose the $5,000 tier instead of $100..."
    ),

    "mixed_tier_math": (
        "When people in your network pick higher tiers, your numbers multiply.\n\n"
        "At $100 tier, your Level 1 allocation per member is $22.50.\n"
        "At $5,000 tier, that same position yields $1,125 per member.\n\n"
        "In a real network, people choose different tiers. Some pick $100. "
        "Some go $1,000. A few go $5,000.\n\n"
        "In the 50,000-person scenario with mixed tiers:\n\n"
        "Position 3: crosses $1,000,000 per year\n"
        "Position 2: crosses $500,000 per year\n"
        "Position 1: crosses $250,000 per year\n\n"
        "The formula doesn't change. The structure doesn't change. "
        "The only thing that changes is the dollar amounts flowing through it.\n\n"
        "Higher tiers don't get special treatment. They just put more money "
        "into the same machine."
    ),

    # ─── How It Compares ──────────────────────────────────────────

    "vs_traditional": (
        "Let me compare this to what most people know.\n\n"
        "SAVINGS ACCOUNT: 0.5% APY. $100 earns you 50 cents in a year.\n\n"
        "STOCK MARKET: Average 10% per year if you hold long enough. "
        "$100 becomes $110 after 12 months. Maybe.\n\n"
        "REAL ESTATE: Good returns, but you need $50K-$100K minimum. "
        "Plus maintenance, tenants, repairs.\n\n"
        "HELIOS at $100 tier with 50K network:\n"
        "Position 3 earns $344,766/year. With staking: $448,195.\n"
        "Your initial investment: $100.\n\n"
        "The catch? You have to build the network. It's not passive. "
        "The math is real, but the work is real too.\n\n"
        "Nothing worth having comes without effort. But the math here "
        "is better than anything a bank will ever offer you."
    ),

    # ─── Token Offering & Launch ──────────────────────────────────

    "token_offering": (
        "The HLS token offering is the starting line. Three phases, clear dates.\n\n"
        "PHASE 1 — FOUNDING WINDOW (Feb 10 – Mar 31, 2026):\n"
        "Token price: $0.10 per HLS. 20% bonus tokens on every purchase. "
        "Founding Member badge — permanent, on-chain. Priority .helios identity.\n\n"
        "PHASE 2 — BUILDER PHASE (Apr 1 – May 31, 2026):\n"
        "Token price: $0.25 per HLS. 10% bonus. 15-level engine activates. "
        "Liquidity pools funded. First NFT certificate minting.\n\n"
        "PHASE 3 — PUBLIC LAUNCH (Jun 1, 2026 →):\n"
        "Token price: $0.50 per HLS. No bonus. DEX listing. Full protocol live.\n\n"
        "$1,000 during Phase 1 = 12,000 HLS tokens. At public price that's $6,000 worth. "
        "6× your money before the network engine even starts."
    ),

    "trustlines": (
        "A trustline is like opening a lane on the highway for a specific token.\n\n"
        "On XRPL, you set a TrustSet transaction to tell your wallet: "
        "'I'm willing to hold HLS tokens.' Costs about 2 XRP as a reserve — "
        "not a fee, it stays in your wallet.\n\n"
        "On Stellar, it's a ChangeTrust operation. Same idea — you authorize "
        "your wallet to hold HLS and stablecoins like USDC.\n\n"
        "You need trustlines set up before you can receive tokens. "
        "During Phase 1, we walk every founding member through the setup "
        "step by step. XUMM/Xaman for XRPL, Lobstr for Stellar. "
        "No technical experience required.\n\n"
        "Once your trustlines are set, tokens flow directly to your wallet. "
        "No middleman. No exchange. Wallet to wallet."
    ),

    "early_benefits": (
        "Here's what founding members get that nobody else will ever have:\n\n"
        "1. LOWEST PRICE EVER — $0.10/HLS. Phase 2 is $0.25. Public is $0.50. "
        "Your dollar goes 5× further than someone joining at launch.\n\n"
        "2. 20% BONUS TOKENS — Buy 1,000, receive 1,200. "
        "Drops to 10% in Phase 2. Zero at public launch.\n\n"
        "3. POSITION 1 — Top of the network. When the 15-level engine "
        "activates, you're at the top. That position is permanent.\n\n"
        "4. FOUNDING MEMBER BADGE — Permanent, non-transferable, on-chain. "
        "You can't buy this later at any price.\n\n"
        "5. PRIORITY .HELIOS IDENTITY — First pick of names. "
        "gold.helios, king.helios — whatever you want.\n\n"
        "6. FIRST TRUSTLINE ACCESS — Your wallet is ready before "
        "everyone else's. When tokens flow, you're already connected."
    ),

    "launch_phases": (
        "Three phases. Each one raises the price and reduces bonuses.\n\n"
        "PHASE 1 — FOUNDING (Feb 10 – Mar 31, 2026):\n"
        "Register. Set up trustlines. Buy HLS at $0.10. Get 20% bonus. "
        "First gold purchase with treasury allocation.\n\n"
        "PHASE 2 — BUILDER (Apr 1 – May 31, 2026):\n"
        "Token price goes to $0.25. Bonus drops to 10%. "
        "15-level engine turns on. Liquidity pools form. "
        "NFT certificates start minting. First proof of reserves.\n\n"
        "PHASE 3 — PUBLIC (Jun 1, 2026 →):\n"
        "Price hits $0.50. No more bonus. Full protocol live. "
        "DEX listing. Staking. Certificate marketplace. "
        "Cross-chain settlement fully operational.\n\n"
        "Every week you wait in Phase 1, you're closer to paying "
        "2.5× more in Phase 2."
    ),

    "liquidity_pools": (
        "Liquidity pools are how HLS gets real trading depth.\n\n"
        "20% of every membership fee goes into the liquidity allocation. "
        "During Phase 2, that money funds HLS/USDC and HLS/XRP pools "
        "on decentralized exchanges.\n\n"
        "That means HLS isn't just a token you hold — it's a token "
        "you can trade. Real buyers, real sellers, real price discovery.\n\n"
        "The Phase 1 token offering is the starting fuel. "
        "Membership fees add to it continuously. "
        "As the network grows, the pools grow. "
        "More liquidity = tighter spreads = better for everyone.\n\n"
        "By Phase 3, when HLS lists on DEXes at $0.50, "
        "there's already real liquidity behind it — not just hype."
    ),

    "hls_token_details": (
        "100 million HLS tokens. Fixed supply. No minting function. "
        "Nobody can create more — not even founders.\n\n"
        "SETTLEMENT POOL — 40% (40M tokens):\n"
        "Powers the 15-level allocation engine.\n\n"
        "NETWORK DISTRIBUTION — 35% (35M tokens):\n"
        "Token offering, membership rewards, introduction bonuses.\n\n"
        "DEVELOPMENT — 15% (15M tokens):\n"
        "4-year linear vesting. Engineering, partnerships.\n\n"
        "EMERGENCY RESERVE — 10% (10M tokens):\n"
        "Locked 5 years. Black swan protection.\n\n"
        "Founder tokens locked 3 years. No admin minting keys. "
        "The contract is immutable. This isn't a promise — "
        "it's code on a blockchain."
    ),

    "flowline": (
        "The Flowline is the animated path on our site that shows how Helios works.\n\n"
        "It moves like electricity through a wire, lighting up each step as value \n"
        "flows through the system. Five steps:\n\n"
        "Step 1 — MEMBERSHIP ACTIVATION: You choose your tier and activate.\n"
        "Step 2 — FIAT TO STABLECOIN: Dollars convert to USDC/USDT.\n"
        "Step 3 — STABLECOIN TO GOLD: Stablecoins acquire physical gold.\n"
        "Step 4 — GOLD TO CERTIFICATES: Gold tokenizes into NFT certificates.\n"
        "Step 5 — 15-LEVEL ALLOCATION: Certificates distribute across 15 levels.\n\n"
        "When a new member activates, the Flowline shows the movement of value \n"
        "through the 15-level structure — step by step, level by level.\n\n"
        "It's a visual way to understand how Helios distributes value, issues \n"
        "gold-backed certificates, and triggers allocations across the network.\n\n"
        "Visit the homepage to watch the Flowline in action."
    ),

    # ─── Token Economics ──────────────────────────────────────────

    "burn_mechanics": (
        "HLS has a fixed supply of 100 million tokens. Burns permanently reduce "
        "that supply. Nobody can reverse a burn. Nobody can mint more.\n\n"
        "WHAT TRIGGERS A BURN:\n\n"
        "Tier Upgrade — when you upgrade, the difference between old and new tier "
        "token allocation is burned. Prevents double-dipping.\n\n"
        "Certificate Redemption — when you redeem a gold certificate for physical "
        "metal, the underlying token allocation is burned. Balances supply when "
        "gold leaves the treasury.\n\n"
        "Marketplace Fee — 20% of every internal marketplace transaction fee is burned. "
        "Buy a gold certificate with HLS? Part of the fee disappears forever.\n\n"
        "Conversion Fee — every HLS→stablecoin swap carries a 1% fee. 20% of that "
        "fee is burned. Every swap reduces supply.\n\n"
        "Early Staking Exit — if you break a staking lock, forfeited bonus tokens "
        "are burned. 50-100% of accrued bonus, depending on timing.\n\n"
        "Expired Identities — unclaimed .helios reserves are burned after 365 days.\n\n"
        "Supply can only go down. Never up. The burn address is public on XRPL."
    ),

    "penalties": (
        "Penalties protect long-term members from short-term exploiters. "
        "Every forfeited token is burned — benefiting everyone who stays.\n\n"
        "STAKING PENALTIES:\n"
        "Break lock within 7 days → 100% of accrued bonus forfeited and burned.\n"
        "Break lock after 7 days → 50% of accrued bonus forfeited and burned.\n\n"
        "RAPID CONVERSION PENALTY:\n"
        "Convert HLS→stablecoin within 48 hours of receiving tokens? "
        "2.5% conversion surcharge instead of the standard 1%. "
        "Discourages pump-and-dump behavior.\n\n"
        "DORMANT ACCOUNT:\n"
        "No activity for 730 days? Staking bonuses pause. "
        "Reactivate anytime with any transaction. No tokens are lost.\n\n"
        "IMPORTANT: No penalty for simply holding. Your tokens, your certificates, "
        "your gold — they're yours. Penalties only apply to breaking commitments "
        "you voluntarily made."
    ),

    "internal_marketplace": (
        "The internal marketplace lets you spend HLS on real assets inside "
        "the protocol. This creates real demand for the token.\n\n"
        "WHAT YOU CAN BUY WITH HLS:\n\n"
        "Gold certificates — purchase additional gold-backed NFT certificates. "
        "Each one represents real gold in the treasury. Redeemable for physical metal.\n\n"
        "Silver certificates — same structure as gold. Real metal, real receipts.\n\n"
        ".helios identities — premium namespace identities like money.helios "
        "or crown.helios. On-chain. Permanent.\n\n"
        "Tier upgrades — use HLS to upgrade your membership tier instead of fiat. "
        "Go from $100 to $5,000 using accumulated tokens.\n\n"
        "Premium analytics — advanced network tools and projection calculators.\n\n"
        "Every marketplace transaction carries a small fee. 20% of every fee "
        "is burned. More usage = more burns = more scarcity."
    ),

    "stablecoin_exchange": (
        "You can convert between HLS, certificates, and stablecoins on-chain. "
        "No intermediary. Wallet-to-wallet. Powered by XRPL DEX and Stellar anchors.\n\n"
        "CONVERSION ROUTES:\n\n"
        "HLS → USDC/USDT — sell HLS for stablecoins at market rate. 1% fee. "
        "20% of fee burned.\n\n"
        "USDC/USDT → HLS — buy HLS with stablecoins. 0.5% fee. Creates buy pressure.\n\n"
        "Certificates → Stablecoin — redeem gold certificates for USDC at current "
        "gold spot rate. Real gold price, real settlement.\n\n"
        "HLS → BTC/ETH/XRP — swap through XRPL DEX pathfinding. Multi-hop routing "
        "finds the best rate automatically.\n\n"
        "RAPID CONVERSION WARNING: If you convert HLS→stablecoin within 48 hours "
        "of receiving tokens, there's a 2.5% surcharge instead of 1%. "
        "This discourages short-term exploitation.\n\n"
        "Settlement in seconds. No exchange account needed. Just your wallet."
    ),

    "genesis_pool": (
        "The Genesis Pool is how Helios starts.\n\n"
        "10 members activate at the $5,000 Executive tier. "
        "10 × $5,000 = $50,000 Genesis Value.\n\n"
        "That $50K splits: 45% ($22,500) allocation pool, 20% ($10,000) liquidity, "
        "15% ($7,500) gold purchase, 10% ($5,000) infrastructure, "
        "10% ($5,000) protocol buffer.\n\n"
        "Genesis Token Supply: 50,000 HLS. 1 token = $1 backing. Clean start.\n\n"
        "Then 10,000 members join at $100 each = $1,000,000 new value. "
        "Total backing becomes $1,050,000. Total supply: 1,050,000 tokens. "
        "Token price stays at $1.00 — but the backing is now massive.\n\n"
        "The Genesis 10 earn $20K–$225K each from the allocation pool alone, "
        "plus gold certificates, staking bonuses, and token allocations.\n\n"
        "The math compounds. The promises don't."
    ),

    "bonus_structure": (
        "Multiple bonus channels reward different behaviors. All bonuses are funded "
        "from existing pools — never from new token creation.\n\n"
        "FOUNDING BONUS: +20% tokens on Phase 1 purchases. Drops to +10% Phase 2. "
        "Zero at public launch.\n\n"
        "TIER UPGRADE BONUS: Upgrade tiers and receive 10% transition bonus on "
        "the price difference. $100→$1,000 = $900 × 10% = $90 in HLS.\n\n"
        "STAKING BONUS: 5-30% based on lock duration (30d/90d/180d/365d).\n\n"
        "LOYALTY MILESTONES: 6 months active = +2%. 12 months = +5%. "
        "24 months = +10%. These stack on top of staking.\n\n"
        "NETWORK GROWTH: 100 members = 500 HLS. 500 members = 2,500 HLS. "
        "1,000 members = 7,500 HLS. 5,000 members = 25,000 HLS.\n\n"
        "GOLD ACCUMULATION: Every 10 oz of gold in treasury triggers 1% bonus "
        "on your next certificate allocation.\n\n"
        "All formula-governed. All published. No discretion."
    ),

    "token_value_drivers": (
        "Token value isn't promised. It's engineered through mechanics.\n\n"
        "SUPPLY REDUCTION: Burns from upgrades, redemptions, marketplace fees, "
        "conversion fees, and staking penalties permanently reduce supply. "
        "100M is the ceiling. Actual circulating supply decreases over time.\n\n"
        "DEMAND CREATION: Marketplace purchases, tier upgrades, staking locks, "
        "and stablecoin→HLS conversions create buy pressure. Real utility = real demand.\n\n"
        "GOLD FLOOR: 15% of every membership buys physical gold. Certificates are "
        "redeemable at gold spot rate. Hard asset floor that rises with gold prices.\n\n"
        "CIRCULATING LOCK: Staked tokens, founder locks (3yr), emergency reserve (5yr), "
        "and development vesting (4yr) remove tokens from circulation. Less available "
        "supply = higher price potential.\n\n"
        "The token doesn't need hype. The mechanics do the work."
    ),

    "qr_code_sharing": (
        "Every Helios member gets a personal QR code page — your .helios identity, "
        "branded with Helios gold, downloadable as a high-res PNG.\n\n"
        "HOW IT WORKS: Go to helios5.netlify.app/qr/yourname. That page shows "
        "your branded QR code. When someone scans it, they land on your personal "
        "registration link. They sign up under you.\n\n"
        "THE CHAIN: After they register, they get their OWN QR code page at "
        "/qr/theirname. They share that code. Their people register. Those people "
        "get their own codes. The chain continues across all 15 levels.\n\n"
        "Every connection is permanent. Your introducer is always your introducer. "
        "The allocation formula runs on every join, automatically.\n\n"
        "SHARING: Download the QR as a PNG — print it, text it, post it, put it "
        "on a business card. Or tap Share to copy the link directly.\n\n"
        "No app required. No login to share. Just a code and a URL. "
        "The network builds itself one scan at a time."
    ),
}


# ═══ Topic Detection — Natural Language Mapping ══════════════════════

TOPIC_MAP = {
    "what_is_helios": ["what is", "what's helios", "explain helios", "about helios", "tell me about", "how does helios", "what does helios do"],
    "five_tiers": ["tiers", "tier", "$100", "$250", "$500", "$1000", "$5000", "starter", "builder", "executive", "leader tier", "pro tier", "which tier", "pick a tier", "membership"],
    "three_ways_to_earn": ["three ways", "3 ways", "how do i earn", "how do i make money", "how you earn", "ways to earn", "income streams", "revenue streams"],
    "direct_referral": ["direct referral", "direct introduction", "referral pay", "introduction allocation", "refer someone", "introduce someone", "bring someone", "per person", "per member", "per referral", "per introduction", "referral bonus", "introduction bonus"],
    "fifteen_level_engine": ["15 level", "fifteen level", "level engine", "allocation engine", "formula", "weight", "levels deep", "how many levels"],
    "allocation_formula": ["formula", "w_l", "0.50", "decay", "weighting", "math behind", "calculation", "how is it calculated"],
    "depth_chart": ["depth chart", "position 1", "position 2", "position 3", "who earns more", "chain", "above me", "below me", "structure", "tree"],
    "fifty_k_scenario": ["50k", "50,000", "fifty thousand", "scenario", "projection", "how much can i make", "realistic", "example", "big numbers", "million"],
    "allocation_split": ["where does my money go", "fee split", "45%", "20%", "15%", "allocation split", "how is the fee split", "where money goes"],
    "gold_backing": ["gold", "physical gold", "metal", "apmex", "vault", "gold backed", "gold backing", "bullion", "precious metal", "real gold"],
    "crypto_access": ["crypto", "bitcoin", "btc", "eth", "ethereum", "xrp", "xlm", "stellar", "usdc", "usdt", "stablecoin", "which crypto"],
    "certificate_staking": ["staking", "stake", "lock", "bonus", "30 day", "90 day", "180 day", "365 day", "staking bonus", "lock certificate"],
    "nft_certificates": ["nft", "certificate", "certificates", "what do i get", "digital asset", "redeemable"],
    "is_this_mlm": ["mlm", "pyramid", "ponzi", "scam", "scheme", "legit", "legitimate", "is this", "multilevel", "multi-level", "network marketing", "is it a"],
    "no_bs_list": ["no bs", "no ranks", "no monthly", "no autoship", "no product", "what's the catch", "hidden fees", "monthly fee", "quota"],
    "how_to_join": ["join", "sign up", "register", "start", "get started", "create account", "how to join", "onboard", "activate", "how do i start"],
    "what_you_receive": ["what do i get", "receive", "what's included", "benefits", "member benefits", "what comes with", "access"],
    "web3_rails": ["xrpl", "stellar", "blockchain", "on chain", "on-chain", "web3", "which chain", "what chain"],
    "treasury": ["treasury", "reserves", "proof of reserves", "vault receipt", "mvr", "where is the gold"],
    "verification": ["verify", "audit", "check", "proof", "transparent", "trust", "verifiable", "published"],
    "risks": ["risk", "downside", "lose money", "what if", "guarantee", "guaranteed", "safe", "risky"],
    "why_not_rug": ["rug", "rug pull", "run away", "steal", "disappear", "trust you"],
    "what_token": ["token", "coin", "hls", "supply", "tokenomics"],
    "protocol_rules": ["rules", "limits", "restrictions", "protocol", "parameters", "how it works technically"],
    "founders": ["founder", "team", "who built", "who made", "creator", "behind helios", "who runs"],
    "earning_examples": ["example", "show me the math", "break it down", "real numbers", "how much with 5", "small network"],
    "mixed_tier_math": ["mixed tier", "higher tier", "bigger numbers", "what if $5000", "multiply"],
    "vs_traditional": ["compare", "savings", "bank", "stock market", "real estate", "better than", "vs", "compared to"],
    "token_offering": ["token offering", "offering", "presale", "pre-sale", "token sale", "buy tokens", "buy hls", "get tokens", "founding window", "get the party started"],
    "trustlines": ["trustline", "trustlines", "trust line", "trustset", "changetrust", "xumm", "xaman", "lobstr", "wallet setup", "set up wallet"],
    "early_benefits": ["early", "register early", "why now", "why join now", "founding member", "founding", "early registration", "early bird", "first mover", "benefits of joining early"],
    "launch_phases": ["phase 1", "phase 2", "phase 3", "phases", "roadmap", "timeline", "when", "dates", "launch date", "when does it start", "launch schedule"],
    "liquidity_pools": ["liquidity", "liquidity pool", "lp", "trading", "dex", "exchange", "trade hls", "pool"],
    "hls_token_details": ["supply", "total supply", "100 million", "token pool", "settlement pool", "network distribution", "emergency reserve", "issuance", "token issuance", "how many tokens", "tokenomics"],
    "flowline": ["flowline", "flow line", "animation", "how it works visually", "the line", "electricity", "glowing line", "activation flow", "show me how it works"],
    "burn_mechanics": ["burn", "burning", "deflationary", "reduce supply", "token burn", "burned", "burn mechanism", "supply reduction"],
    "penalties": ["penalty", "penalties", "penalize", "forfeit", "forfeited", "early exit", "break lock", "punishment", "surcharge", "rapid conversion", "dormant"],
    "internal_marketplace": ["marketplace", "buy with hls", "spend hls", "internal market", "buy gold with tokens", "buy certificates", "purchase with hls", "use tokens"],
    "stablecoin_exchange": ["convert", "conversion", "swap", "exchange", "hls to usdc", "hls to usdt", "stablecoin exchange", "cash out", "sell tokens", "sell hls", "convert to dollars"],
    "genesis_pool": ["genesis", "genesis pool", "genesis tier", "first 10", "seed", "initial", "50000", "$50,000", "founding pool", "starting pool", "how it starts"],
    "bonus_structure": ["bonus", "bonuses", "loyalty", "milestone", "network growth bonus", "upgrade bonus", "tier upgrade bonus", "gold accumulation", "compound"],
    "token_value_drivers": ["value driver", "what drives value", "why go up", "price increase", "appreciation", "token value", "supply and demand", "scarcity", "deflationary pressure"],
    "qr_code_sharing": ["qr", "qr code", "share code", "share link", "scan", "my code", "my qr", "network code", "how do i share", "share helios", "send my link", "business card", "invite link", "personal link", "registration link"],
}


class AskHelios:
    """
    The Voice of HELIOS.
    Male. Calm. Grounded. Kitchen-table money talk.
    Explains gold, crypto, and the 15-level math like a real person.
    Never sells. Never hypes. Shows the math and lets you decide.
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
            {"question": "How does the token offering work?", "icon": "🚀"},
            {"question": "Why should I register early?", "icon": "⏰"},
            {"question": "What are trustlines?", "icon": "🔗"},
            {"question": "What is Helios?", "icon": "☀️"},
            {"question": "How do I make money?", "icon": "💰"},
            {"question": "What are the 5 tiers?", "icon": "📊"},
            {"question": "Show me the depth chart", "icon": "📈"},
            {"question": "Is this MLM?", "icon": "🔍"},
            {"question": "How does the 15-level engine work?", "icon": "⚙️"},
            {"question": "What's the 50K scenario?", "icon": "💵"},
            {"question": "How does the gold backing work?", "icon": "🏆"},
            {"question": "How do token burns work?", "icon": "🔥"},
            {"question": "What are the penalties?", "icon": "⚠️"},
            {"question": "How does the internal marketplace work?", "icon": "🏪"},
            {"question": "How do I convert to stablecoins?", "icon": "💱"},
            {"question": "What is the genesis pool?", "icon": "🌱"},
            {"question": "What about the liquidity pools?", "icon": "🌊"},
            {"question": "How do I share my QR code?", "icon": "📱"},
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
        """System prompt with 5-tier gold-backed protocol context and voice rules."""
        context = (
            "You are Helios — the voice of the protocol. "
            "Male. Calm. Grounded. Authoritative. Like a smart friend "
            "explaining money at a kitchen table.\n\n"
            "WHAT HELIOS IS:\n"
            "A gold-backed allocation protocol on Web3 rails (XRPL + Stellar). "
            "5 membership tiers: $100, $250, $500, $1,000, $5,000. "
            "One payment. No monthly fees. No autoship. No product.\n\n"
            "3 ALLOCATION CHANNELS:\n"
            "1. Direct Introduction Allocation — 50% of allocation pool per member you introduce\n"
            "2. 15-Level Engine — 45% of every membership distributed across 15 levels, "
            "formula: W_L = 0.50 × 0.5^(L-1)\n"
            "3. Gold, NFTs & Crypto — physical gold, certificates, staking bonuses\n\n"
            "TIER ALLOCATIONS (direct introduction per member):\n"
            "$100 → $22.50 | $250 → $56.25 | $500 → $112.50 | "
            "$1,000 → $225 | $5,000 → $1,125\n\n"
            "DEPTH CHART:\n"
            "Position 1 = top of chain. Position 2 = middle. Position 3 = closest to action.\n"
            "Position 3 earns the most. The formula rewards the person doing the work.\n"
            "50K network at $100: Pos3=$28,730/mo, Pos2=$14,502/mo, Pos1=$7,326/mo\n\n"
            "STAKING BONUSES:\n"
            "30d=+5%, 90d=+12%, 180d=+20%, 365d=+30%\n\n"
            "BURN MECHANICS:\n"
            "Tier upgrades, certificate redemptions, marketplace fees (20% burned), "
            "conversion fees (20% burned), early staking exits — all permanently reduce supply.\n\n"
            "PENALTIES:\n"
            "Early staking exit <7d = 100% bonus forfeited. >7d = 50% forfeited. "
            "Rapid conversion (<48h) = 2.5% surcharge. All forfeitures are burned.\n\n"
            "INTERNAL MARKETPLACE:\n"
            "Buy gold/silver certificates, .helios identities, tier upgrades with HLS. "
            "20% of all marketplace fees burned.\n\n"
            "ALLOCATION SPLIT:\n"
            "45% network engine, 20% liquidity, 15% gold treasury, "
            "10% infrastructure, 10% buffer\n\n"
            "VOICE RULES:\n"
            "- Talk like a real person explaining money to another adult\n"
            "- Use plain language. No crypto jargon unless asked.\n"
            "- Be direct. Be honest. No hype.\n"
            "- Say 'the math shows' not 'you'll make'\n"
            "- Always mention results depend on effort and network growth\n"
            "- Never guarantee income. Show the formula and let them decide.\n"
            "- If you don't know something, say so.\n"
            "- No ranks, no titles, no 'Diamond Director' language\n\n"
            "PROTOCOL FACTS:\n"
            f"- Token: {HeliosConfig.TOKEN_NAME} ({HeliosConfig.TOKEN_SYMBOL})\n"
            f"- Total supply: {HeliosConfig.TOKEN_TOTAL_SUPPLY:,} (FIXED)\n"
            f"- Chains: XRPL + Stellar\n"
            f"- Treasury: Physical gold via APMEX\n"
            f"- Certificates: Gold-backed NFTs on XRPL\n"
            f"- Crypto: BTC, ETH, XRP, XLM, USDC, USDT\n"
        )
        if member_id:
            context += f"\nThe person asking holds identity: {member_id}\n"
        return context

    def _smart_fallback(self, question: str) -> str:
        """Fallback when AI is unavailable."""
        q = question.lower()

        if any(w in q for w in ["price", "worth", "value", "market"]):
            return (
                "Helios doesn't make price projections. The protocol holds "
                "physical gold, issues certificates backed by real assets, "
                "and pays through a published 15-level formula. "
                "Value comes from the network and the gold — not speculation."
            )

        if any(w in q for w in ["how much", "earn", "money", "make", "income", "paid"]):
            return (
                "Your earnings depend on your tier and your network. "
                "At the $100 tier, you receive $22.50 per direct introduction. "
                "The 15-level engine distributes allocations from everyone in your network — "
                "up to 15 levels deep. In a 50,000-person network at $100, "
                "Position 3 earns $28,730/month. "
                "Results depend on effort and network growth."
            )

        if any(w in q for w in ["safe", "secure", "security", "trust"]):
            return (
                "The treasury holds physical gold with receipts on XRPL. "
                "The allocation formula is published — anyone can verify. "
                "There are no admin override keys. The fee split is hardcoded. "
                "No one can change the rules or drain the pools. "
                "Verify the gold. Verify the math. That's all I ask."
            )

        if any(w in q for w in ["help", "support", "problem", "issue"]):
            return (
                "I can explain the 5 tiers, the 3 ways to earn, "
                "the depth chart, the 15-level formula, the gold backing, "
                "the crypto access, staking, or how to get started. "
                "What would you like to know?"
            )

        if any(w in q for w in ["gold", "metal", "treasury"]):
            return (
                "15% of every membership fee buys physical gold through APMEX. "
                "With 50,000 members at $100, that's $750,000 in gold. "
                "Metal Vault Receipts are NFTs on XRPL. "
                "Proof of reserves is always public.\n\n"
                "Want to know more about the certificates or crypto access?"
            )

        return (
            "Helios is a gold-backed allocation protocol with 5 membership tiers, "
            "15 levels of allocation, and real assets — gold, NFTs, and crypto.\n\n"
            "Could you rephrase your question? I want to give you a precise answer."
        )

    # ═══ Helpers ═════════════════════════════════════════════════

    def _suggest_follow_up(self, question: str) -> list:
        if any(w in question for w in ["offering", "presale", "token sale", "buy tokens", "founding window"]):
            return ["Why should I register early?", "How do burns work?"]
        elif any(w in question for w in ["burn", "deflationary", "supply reduction"]):
            return ["What are the penalties?", "What drives token value?"]
        elif any(w in question for w in ["penalty", "forfeit", "surcharge"]):
            return ["How does staking work?", "How do burns work?"]
        elif any(w in question for w in ["marketplace", "buy with hls", "spend"]):
            return ["How does the stablecoin exchange work?", "How do burns work?"]
        elif any(w in question for w in ["convert", "swap", "exchange", "cash out", "sell"]):
            return ["What about the internal marketplace?", "What are the penalties?"]
        elif any(w in question for w in ["genesis", "seed", "first 10", "founding pool"]):
            return ["How does the token offering work?", "What drives token value?"]
        elif any(w in question for w in ["trustline", "wallet", "xumm", "lobstr"]):
            return ["How does the token offering work?", "What are the 5 tiers?"]
        elif any(w in question for w in ["early", "founding", "register early", "why now", "benefits"]):
            return ["How does the token offering work?", "Show me the depth chart"]
        elif any(w in question for w in ["phase", "roadmap", "timeline", "dates", "when"]):
            return ["Why should I register early?", "What about the liquidity pools?"]
        elif any(w in question for w in ["liquidity", "pool", "dex", "trade"]):
            return ["How does the token offering work?", "What's the 50K scenario?"]
        elif any(w in question for w in ["join", "start", "sign", "activate", "entry"]):
            return ["How does the token offering work?", "What are the 5 tiers?"]
        elif any(w in question for w in ["tier", "$100", "$250", "$500", "$1000", "$5000"]):
            return ["How do I make money?", "Why should I register early?"]
        elif any(w in question for w in ["earn", "paid", "money", "income", "referral"]):
            return ["Show me the depth chart", "What's the 50K scenario?"]
        elif any(w in question for w in ["depth", "position", "chain", "structure"]):
            return ["What's the 50K scenario?", "How does the 15-level engine work?"]
        elif any(w in question for w in ["mlm", "scam", "pyramid", "trust", "rug", "legit"]):
            return ["What's the no-BS list?", "How does the gold backing work?"]
        elif any(w in question for w in ["gold", "metal", "treasury", "vault"]):
            return ["What crypto can I access?", "How does staking work?"]
        elif any(w in question for w in ["crypto", "btc", "eth", "xrp", "stablecoin"]):
            return ["How does staking work?", "How does the gold backing work?"]
        elif any(w in question for w in ["staking", "stake", "lock", "bonus"]):
            return ["What's the 50K scenario?", "How do I join?"]
        elif any(w in question for w in ["certificate", "nft"]):
            return ["How does the gold backing work?", "How does staking work?"]
        elif any(w in question for w in ["formula", "level", "engine", "15"]):
            return ["Show me the depth chart", "What are the 5 tiers?"]
        elif any(w in question for w in ["50k", "scenario", "million", "projection"]):
            return ["How does staking work?", "What about mixed tiers?"]
        elif any(w in question for w in ["token", "supply", "hls", "issuance"]):
            return ["How does the token offering work?", "What about the liquidity pools?"]
        elif any(w in question for w in ["founder", "team", "who"]):
            return ["What are the protocol rules?", "How does verification work?"]
        else:
            return ["How does the token offering work?", "What are the 5 tiers?"]

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
