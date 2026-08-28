# Charter-A Ltd Flight Brief Generator

Produces the standard Charter-A passenger flight brief — single-page (auto-paginating)
A4 PDF in military briefing format, with numbered serials:

1. SITUATION · 2. MISSION · 3. EXECUTION — TIMINGS · 4. AIRCRAFT ·
5. PERSONNEL · 6. GROUND HANDLING — RV POINT · 7. COMMAND & SIGNAL — ADMIN

Charter-A branding (header, 24-hr ops line, Redhill address, company number) is fixed
in the script. **No third-party operator branding is ever printed** — do not include
operator names, logos or operator flight designators (e.g. an operator's ICAO callsign
prefix) in the JSON fields.

## Usage

```bash
pip install reportlab   # once
python3 generate_brief.py trip.json                 # writes Charter-A_Flight_Brief_Trip-<n>.pdf
python3 generate_brief.py trip.json my-output.pdf
```

Copy `sample-trip.json`, fill in the trip. Field notes:

| Field | Notes |
|---|---|
| `trip_number` | Charter-A trip reference — used as the document REF |
| `dtg` | Departure date-time group, e.g. `291915L AUG 26` (ddHHMM + L for local) |
| `issued` | Issue date, e.g. `28 AUG 26` |
| `subtitle` | Header strap, e.g. `ROTARY WING / PASSENGER TRANSFER` or `FIXED WING / PASSENGER TRANSFER` |
| `situation` / `mission` | Arrays of pre-wrapped lines (~78 chars max each) |
| `timings` | One row per event; serials (a), (b)… are added automatically. Multi-leg trips: add WHEELS UP/DOWN rows per leg |
| `passengers` | `dob` and `passport` optional per pax |
| `crew` | Array of `[role, name]` pairs |
| `delay_action` | Optional override of the standard delay instruction lines |

## Privacy rule

Filled `trip.json` files and generated PDFs contain passenger PII (passports, DoB).
**Never commit them to this repository.** Work in a scratch directory; only this
template, the README and the dummy `sample-trip.json` belong in git.
