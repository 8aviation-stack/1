---
name: flight-brief
description: Generate a Charter-A Ltd passenger flight brief PDF in the company's standard military-briefing format. Use whenever the user uploads a PAX information sheet / trip sheet (any operator's PDF) or asks for a flight brief, passenger brief, or flight schedule for a Charter-A trip.
---

# Charter-A Flight Brief

Produce the standard Charter-A Ltd flight brief using the saved template at
`charter-a-flight-brief/generate_brief.py` (repo root). Never redesign the layout —
the format is fixed company style.

## Steps

1. **Extract trip data** from whatever the user provided (usually an operator's PAX
   information PDF — extract text with pypdf; `pip install pypdf cffi` if missing).
2. **Build a trip JSON** in a scratch directory (never inside the repo), following
   `charter-a-flight-brief/sample-trip.json`. Pre-wrap `situation`/`mission` lines to
   ~78 chars. DTG format: `ddHHMML MMM yy` (e.g. `291915L AUG 26`).
3. **Strip all third-party operator branding**: no operator names, logos, or operator
   flight numbers/callsigns (e.g. an ICAO-prefix flight number like `SXN22` identifies
   the operator — omit it and use the Charter-A trip number as the reference). Keep
   handling agents (FBOs) — they are not the operator.
4. **Generate**: `pip install reportlab` if needed, then
   `python3 charter-a-flight-brief/generate_brief.py <scratch>/trip.json <scratch>/Charter-A_Flight_Brief_Trip-<n>.pdf`
5. **Verify** by rendering a page image (`pdftoppm -jpeg`) and reading it — check no
   text overflows columns and no operator reference slipped through.
6. **Deliver** the PDF to the user with SendUserFile.

## Hard rules

- Filled trip JSONs and generated PDFs contain passenger PII (passports, DoB):
  **never commit them to git** — scratch directory only.
- Facts only: never invent times, contacts, or requirements not present in the
  source document (advisory phrasing like "arrive in good time" is fine).
- Charter-A branding, ops phone, address and company number are hardcoded in the
  script — do not vary them in the JSON.
