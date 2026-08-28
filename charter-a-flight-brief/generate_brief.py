#!/usr/bin/env python3
"""
Charter-A Ltd flight brief generator — military briefing format.

Usage:
    python3 generate_brief.py trip.json [output.pdf]

The JSON schema is documented in README.md; see sample-trip.json for a
worked example. Company details in the ADMIN section and footer are fixed
Charter-A Ltd branding. No operator (third-party) branding is ever printed.

Requires: reportlab  (pip install reportlab)
"""
import json
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, white

# ---- fixed Charter-A branding -------------------------------------------
COMPANY_FOOTER_1 = ("CHARTER-A LTD - HANGAR ONE, LONDON REDHILL AERODROME, "
                    "KINGSMILL LANE, REDHILL, SURREY, RH1 5JY - COMPANY NO. 7668809")
COMPANY_FOOTER_2 = "24-HOUR FLIGHT OPERATIONS: +44 20 7781 8094 - WWW.CHARTER-A.COM"
OPS_LINE = "+44 20 7781 8094  /  operations@charter-a.com"
BANNER = ("* * *  P R I V A T E   &   C O N F I D E N T I A L  —  "
          "P A S S E N G E R   B R I E F  * * *")

W, H = A4
M = 16 * mm
INK = HexColor("#111111")
OLIVE = HexColor("#3d4a1f")
GREY = HexColor("#555555")
LIGHT = HexColor("#ededed")
LH = 4.6 * mm
SEC_GAP = 3.2 * mm


class Brief:
    def __init__(self, c):
        self.c = c
        self.y = 0

    def new_page(self, d, first=False):
        c = self.c
        if not first:
            self._footer()
            c.showPage()
        y = H - 12 * mm
        c.setFillColor(INK)
        c.setFont("Courier-Bold", 8)
        c.drawCentredString(W / 2, y, BANNER)
        y -= 7 * mm
        c.setFillColor(INK)
        c.rect(M, y - 15 * mm, W - 2 * M, 15 * mm, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Courier-Bold", 20)
        c.drawString(M + 5 * mm, y - 9.5 * mm, "CHARTER-A LTD")
        c.setFont("Courier-Bold", 10)
        c.drawRightString(W - M - 5 * mm, y - 6 * mm, "FLIGHT OPERATIONS BRIEF")
        c.setFont("Courier", 9)
        c.drawRightString(W - M - 5 * mm, y - 11.5 * mm, d.get("subtitle", "PASSENGER TRANSFER").upper())
        y -= 15 * mm
        c.setFillColor(OLIVE)
        c.rect(M, y - 6.5 * mm, W - 2 * M, 6.5 * mm, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Courier-Bold", 9)
        c.drawString(M + 5 * mm, y - 4.6 * mm, f"REF: TRIP {d['trip_number']}")
        c.drawCentredString(W / 2, y - 4.6 * mm, f"DTG: {d['dtg']}")
        c.drawRightString(W - M - 5 * mm, y - 4.6 * mm, f"ISSUED: {d['issued']}")
        self.y = y - 11 * mm

    def _footer(self):
        c = self.c
        c.setStrokeColor(INK)
        c.setLineWidth(1.2)
        c.line(M, 24 * mm, W - M, 24 * mm)
        c.setFillColor(GREY)
        c.setFont("Courier", 7.5)
        c.drawCentredString(W / 2, 20 * mm, COMPANY_FOOTER_1)
        c.drawCentredString(W / 2, 16.5 * mm, COMPANY_FOOTER_2)
        c.setFillColor(INK)
        c.setFont("Courier-Bold", 8)
        c.drawCentredString(W / 2, 11 * mm, BANNER)

    def need(self, h, d):
        if self.y - h < 30 * mm:
            self.new_page(d)

    def section(self, title, d):
        self.need(14 * mm, d)
        c = self.c
        c.setFillColor(INK)
        c.rect(M, self.y - 5.6 * mm, W - 2 * M, 5.6 * mm, fill=1, stroke=0)
        c.setFillColor(white)
        c.setFont("Courier-Bold", 10)
        c.drawString(M + 2.5 * mm, self.y - 4.0 * mm, title)
        self.y -= 5.6 * mm + 2.6 * mm

    def kv(self, key, val, bold_val=False, keyw=42 * mm):
        c = self.c
        c.setFillColor(GREY)
        c.setFont("Courier-Bold", 9)
        c.drawString(M + 2.5 * mm, self.y, key)
        c.setFillColor(INK)
        c.setFont("Courier-Bold" if bold_val else "Courier", 9.5)
        c.drawString(M + 2.5 * mm + keyw, self.y, str(val))
        self.y -= LH

    def line(self, text, font="Courier", size=9.5, color=INK):
        c = self.c
        c.setFillColor(color)
        c.setFont(font, size)
        c.drawString(M + 2.5 * mm, self.y, text)
        self.y -= LH

    def gap(self, h=SEC_GAP):
        self.y -= h


def build(d, out):
    c = canvas.Canvas(out, pagesize=A4)
    c.setTitle(f"CHARTER-A LTD — FLIGHT BRIEF TRIP {d['trip_number']}")
    b = Brief(c)
    b.new_page(d, first=True)

    # 1. SITUATION
    b.section("1. SITUATION", d)
    for ln in d.get("situation", ["Private passenger transfer tasked by CHARTER-A LTD operations.",
                                  "All timings LOCAL."]):
        b.line(ln)
    b.gap()

    # 2. MISSION
    b.section("2. MISSION", d)
    for ln in d["mission"]:
        b.line(ln, font="Courier-Bold", size=9.5)
    b.gap()

    # 3. EXECUTION — TIMINGS
    b.section("3. EXECUTION — TIMINGS", d)
    b.need(6 * mm + LH * (len(d["timings"]) + 2), d)
    c.setFillColor(LIGHT)
    c.rect(M + 2.5 * mm, b.y - 1.4 * mm, W - 2 * M - 5 * mm, 5.4 * mm, fill=1, stroke=0)
    c.setFillColor(GREY)
    c.setFont("Courier-Bold", 8.5)
    cols = [(4, "SERIAL"), (24, "EVENT"), (78, "LOCATION"), (136, "TIME (L)"), (158, "REMARKS")]
    for x, t in cols:
        c.drawString(M + x * mm, b.y, t)
    b.y -= LH + 1 * mm
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i, row in enumerate(d["timings"]):
        c.setFillColor(INK)
        c.setFont("Courier", 9)
        c.drawString(M + 4 * mm, b.y, f"({letters[i]})")
        c.drawString(M + 24 * mm, b.y, row["event"])
        c.drawString(M + 78 * mm, b.y, row["location"])
        c.setFont("Courier-Bold", 9)
        c.drawString(M + 136 * mm, b.y, row["time"])
        c.setFont("Courier", 9)
        c.drawString(M + 158 * mm, b.y, row.get("remarks", ""))
        b.y -= LH
    b.y -= 1 * mm
    for ln in d.get("execution_notes", []):
        b.line(ln, font="Courier-Bold", size=9)
    b.gap()

    # 4. AIRCRAFT
    b.section("4. AIRCRAFT", d)
    b.kv("TYPE:", d["aircraft"]["type"].upper(), bold_val=True)
    b.kv("REGISTRATION:", d["aircraft"]["registration"].upper(), bold_val=True)
    b.kv("CREW:", d["aircraft"].get("crew_note", "SEE SERIAL 5"))
    b.gap()

    # 5. PERSONNEL
    b.section("5. PERSONNEL", d)
    b.line(f"PAX MANIFEST — {d.get('manifest_label', '').upper()}".rstrip(" —") + ":",
           font="Courier-Bold", size=9)
    for i, p in enumerate(d["passengers"], 1):
        b.need(LH * 4, d)
        b.kv(f"  PAX {i}:", p["name"].upper(), bold_val=True)
        if p.get("dob"):
            b.kv("  DOB:", p["dob"])
        if p.get("passport"):
            b.kv("  PASSPORT:", p["passport"])
    b.y -= 1.5 * mm
    b.line("CREW:", font="Courier-Bold", size=9)
    for role, name in d["crew"]:
        b.kv(f"  {role.upper()}:", name.upper(), bold_val=True)
    b.gap()

    # 6. GROUND HANDLING
    b.section("6. GROUND HANDLING — RV POINT", d)
    h = d["handling"]
    b.kv("HANDLING AGENT:", h["agent"].upper(), bold_val=True)
    if h.get("telephone"):
        b.kv("TELEPHONE:", h["telephone"])
    if h.get("email"):
        b.kv("EMAIL:", h["email"])
    b.y -= 1 * mm
    for ln in d.get("delay_action", [
            "ACTION ON DELAY: contact any crew member or the handling agent above at the",
            "earliest opportunity. The aircraft will be held where operationally possible."]):
        b.line(ln, size=9)
    b.gap()

    # 7. COMMAND & SIGNAL
    b.section("7. COMMAND & SIGNAL — ADMIN", d)
    b.kv("TASKING AUTHORITY:", "CHARTER-A LTD FLIGHT OPERATIONS", bold_val=True)
    b.kv("OPS (24 HR):", OPS_LINE, bold_val=True)
    if d.get("requested"):
        b.kv("TRIP REQUESTED:", d["requested"])
    if d.get("amended"):
        b.kv("LAST AMENDED:", d["amended"])
    if d.get("authorised_by"):
        b.kv("AUTHORISED BY:", d["authorised_by"].upper())

    b._footer()
    c.save()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    with open(sys.argv[1]) as f:
        data = json.load(f)
    out = sys.argv[2] if len(sys.argv) > 2 else f"Charter-A_Flight_Brief_Trip-{data['trip_number']}.pdf"
    build(data, out)
    print("written", out)
