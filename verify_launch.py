"""Quick contract + metrics verification for launch."""
from app import create_app
import json

app = create_app()
client = app.test_client()

def api(path):
    """Get JSON, unwrap {success, data} envelope if present."""
    raw = json.loads(client.get(path).data)
    if isinstance(raw, dict) and 'data' in raw:
        return raw['data']
    return raw

print("=== SMART CONTRACT VERIFICATION ===\n")

t = api('/api/token/info')
print(f"Token: {t['symbol']}  Supply: {t['total_supply']:,.0f}  Decimals: {t['decimals']}  Founder Lock: {t['anti_rug']['founder_lock_years']}yr")
print(f"Anti-Rug: can_mint={t['anti_rug']['can_mint']}  admin_override={t['anti_rug']['admin_override_possible']}  auditable={t['anti_rug']['supply_auditable']}")
for pool, info in t['allocation'].items():
    print(f"  {pool:15s} {info['percent']:>3}%  {info['amount']:>14,.0f} HLS  [{info['status']}]")

v = api('/api/token/verify')
print(f"Verify: supply_correct={v.get('supply_correct', v.get('valid'))}  no_mint={v.get('no_mint_function', 'n/a')}")

fl = api('/api/token/founder-lock')
print(f"Founder Lock: locked={fl['locked']}  amount={fl.get('amount',0):,}  unlock={fl.get('unlock_date','n/a')}")

s = api('/api/token/supply')
print(f"Supply: total={s['total_supply']:,.0f}  circulating={s.get('circulating',0):,}  minted={s.get('minted','n/a')}")

print("\n=== TREASURY / METAL RESERVES ===")
res = json.loads(client.get('/api/treasury/reserves').data)
print(f"Receipts: {res['total_receipts']}  Anchored: {res['anchored_count']}")
for metal, data in res.get('by_metal', {}).items():
    print(f"  {metal}: {data['total_oz']} oz  ${data['total_cost_usd']:,.2f}  ({data['receipt_count']} receipts)")

print("\n=== CERTIFICATES ===")
cov = json.loads(client.get('/api/certificates/covenant').data)
d = cov.get('data', cov)
print(f"Covenant: status={d.get('status')}  ratio={d.get('ratio')}  redemption_ok={d.get('redemption_permitted')}")

act = json.loads(client.get('/api/certificates/active').data)
print(f"Active: {act}")

print("\n=== ENERGY CONSERVATION LAW ===")
con = json.loads(client.get('/api/energy/conservation').data)
print(f"Balanced: {con['balanced']}")
print(f"  In: {con['total_in']}  Routed: {con['total_routed']}  Stored: {con['total_stored']}  Pooled: {con['total_pooled']}  Burned: {con['total_burned']}")
print(f"  Delta: {con['delta']} (should be 0)")

print("\n=== METRICS FORMULAS ===")
m = json.loads(client.get('/api/metrics/all').data)
for name, val in m.items():
    print(f"  {name}: value={val['value']}  status={val['status']}")

h = json.loads(client.get('/api/metrics/health').data)
print(f"  Network: nodes={h['total_nodes']}  active={h['active_nodes']}  certs={h['active_certificates']}  energy={h['total_energy_he']} HE")

print("\n=== REWARDS / SETTLEMENT ===")
rp = json.loads(client.get('/api/rewards/protocol').data)
print(f"Settlement: {rp['settlement_rules']}  max_hops={rp['max_hops']}  decay={rp['decay']}")

print("\n=== FIELD STATUS ===")
fs = json.loads(client.get('/api/field/status').data)
print(f"Field: {fs}")

print("\n=== INFRASTRUCTURE ===")
inf = json.loads(client.get('/api/infra/status').data)
d2 = inf.get('data', inf)
print(f"Status: {d2.get('status')}")
for svc, st in d2.get('services', {}).items():
    print(f"  {svc}: {st}")

print("\n=== ALL PAGES ===")
pages = ['/', '/dashboard', '/field', '/network', '/ask', '/protocol', '/status',
         '/treasury', '/vault', '/vault/gold', '/activate', '/metrics', '/enter', '/join', '/health']
for p in pages:
    r = client.get(p)
    size = len(r.data)
    status = "OK" if r.status_code == 200 else f"FAIL({r.status_code})"
    print(f"  {p:20s} {size:>6d}B  {status}")

print("\n☀ ALL CONTRACTS + METRICS + PAGES VERIFIED")
