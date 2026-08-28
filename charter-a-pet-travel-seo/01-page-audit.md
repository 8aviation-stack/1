# SEO Audit — charter-a.com/private-jet-charter/pet-travel/

**Project:** Improve the pet travel page and the charter-a.com domain's pet-flight topical authority.
**Date:** 28 August 2026 (v2 — verified against full live page source supplied by the owner; the v1 caveats are resolved)

---

## 1. What the page is today (verified)

| Element | Current state |
|---|---|
| URL | `/private-jet-charter/pet-travel/` (good: sits under the commercial /private-jet-charter/ hub) |
| Title tag | `Private Jet Pet Flights Charter-A Ltd` |
| Meta description | Auto-generated from page copy, ~300 chars, cut off mid-sentence: "…guide you through the pet" |
| H1 | `Private Jet Pet Flights` — immediately followed by an **H2 with identical text** |
| Heading structure | H1 → duplicate H2 → then jumps to **H5s** ("Flying your pet into the UK.", "Flying your pet into Europe…"). No keyword-bearing H2/H3s |
| Schema | BreadcrumbList, WebPage, WebSite + **two conflicting Organization blocks** (AIOSEO: tel +441737823733; a second HFCM-injected block: tel +44 20 7781 8094, different email/logo). **No Service or FAQPage schema** |
| Freshness | datePublished 2014, **dateModified 2022-09-22** — four years stale, and the copy still carries "COVID19 safe travel flights / Deep cleaned aircraft" bullets |
| AIOSEO | **Focus keyphrase is empty**; headline score 46 |
| CTA | One inline text link ("private jet quote" → /contact). No prominent quote CTA on the page itself |
| Hero image | `dog-on-private-jet-scaled.gif` — a 2560px **GIF** as the LCP element (heavy; convert to WebP/JPG) |

## 2. Critical issues (verified)

### 2.1 The site's own internal links crown the WRONG pet page
This is now the single biggest finding. On every page of the site:

- The main nav item **"Pets on private jets"** links to `/pet-flights/` — not this page.
- The site-wide footer banner **"FLY WITH YOUR PET"** button links to `/pet-flights/` — not this page.

So the domain's entire internal link equity for pet queries flows to `/pet-flights/`, while `/private-jet-charter/pet-travel/` (the page in the commercial hub, the one this project targets) is orphaned apart from breadcrumbs. Google is being told `/pet-flights/` is the pillar.

**Fix:** point both the nav item and the footer button at `/private-jet-charter/pet-travel/`, then **301 `/pet-flights/` → `/private-jet-charter/pet-travel/`** (AIOSEO Pro → Redirects). Also retitle `/private-jet-dogs/` as a gallery and keep `/can-i-take-my-dog-on-a-private-jet/` as a long-tail Q&A post, both linking to the pillar with the anchor *pet friendly private jet charter*.

### 2.2 Title tag and meta description
- Title `Private Jet Pet Flights Charter-A Ltd`: no separator before the brand, and "pet flights" is not the money term — the whole market titles on **pet friendly private jet charter** (VistaJet, K9 Jets, Mercury, Global Charter, PrivateFly). No UK signal either. (The ▷/► symbols seen in SERPs live in image `title` attributes and other pages' titles — e.g. every image on this page is titled "… ► Charter-A Ltd" — worth cleaning up site-wide, but the live page title itself is symbol-free.)
- Meta description is an auto-truncated copy dump ending mid-sentence. Write a real one (~155 chars) with the keyword and a reason to click.
- **Recommended title:** `Pet Friendly Private Jet Charter | Fly With Your Dog in the Cabin | Charter-A`
- Set the AIOSEO focus keyphrase to `pet friendly private jet charter` (currently empty).

### 2.3 Duplicate H1/H2 and broken heading hierarchy
The banner renders the H1 and then repeats the identical text as an H2; the body then uses H5s for its two real sections. Replace with the H2/H3 structure in `03-pet-travel-page-content.html` — every heading there carries a query ("Flying pets into the UK", "What does it cost…", FAQ questions).

### 2.4 Copy quality and accuracy
Verified issues in the live text:
- Typos/broken fragments: "The rules for flying your **per** by private jet**]**", "your off out of the airport" (→ you're), "…and your pets.**Benefits** of flying…" (a heading collapsed into a paragraph, no space).
- "COVID19" bullets date the page to 2020.
- Rabies timing is phrased as "22 days before entering the UK" — GOV.UK's rule is a **21-day wait after vaccination** before travel; say it the official way.
- The EU section states an AHC must contain "confirmation of a serological test for rabies antibodies" — a rabies titre test is **not** required for GB→EU travel; it applies only to certain third-country routes. Overstating it will scare off bookers. (The later "may be required depending on your destination" line is the correct framing.)
- What the page gets right and should keep: AHC and GB pet health certificate both mentioned, tapeworm 24–120h with praziquantel, the Finland/Ireland/NI/Norway/Malta tapeworm exemption, good GOV.UK/DEFRA external links, decent image alt text.

### 2.5 Missing content and conversion elements
Confirmed absent from the live page: FAQ section + FAQPage schema, Service schema, named UK pet-arrival airports (Biggin Hill, Farnborough, Luton, Oxford, Manchester), any pricing guidance, route examples, and a visible quote CTA. All included in the replacement copy (file 03).

### 2.6 Technical/site-level flags (seen in page source)
- **Two Google Tag Manager containers** fire on every page (GTM-KFHZWX and GTM-W9G7JP) — likely double-counting analytics; consolidate to one.
- **Two different `google-site-verification` codes** and two Organization schemas with conflicting phone numbers/emails — keep one of each, matching the real NAP.
- A **"404 redirect to homepage" plugin** is active and reports ~50K redirects this month (733K all-time). Blanket-redirecting 404s to the homepage creates soft-404s that Google ignores or penalises, and it hides real broken-link problems. Review the 404 log, add targeted 301s for URLs with equity, and let genuine junk return 404/410.
- `og:type` is `activity` (non-standard) — use `website` (or `article` on posts).
- Republish the page after the content update so `dateModified` finally moves off 2022.

## 3. Priority order
1. Publish the rewritten pillar content + new title/meta/focus keyphrase (file 03) — republishing also refreshes dateModified.
2. **Repoint the nav item and footer "FLY WITH YOUR PET" button to `/private-jet-charter/pet-travel/`**, then 301 `/pet-flights/` to it.
3. Publish the UK-inbound supporting article (file 04) and interlink.
4. Add FAQPage + Service schema (in file 03); remove the duplicate Organization snippet.
5. Replace the GIF hero with WebP/JPG; strip ► from image title attributes.
6. Consolidate GTM containers and verification codes; review the 404-redirect plugin's behaviour.
