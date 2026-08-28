# SEO Audit — charter-a.com/private-jet-charter/pet-travel/

**Project:** Improve the pet travel page and the charter-a.com domain's pet-flight topical authority.
**Date:** 28 August 2026
**Method note:** charter-a.com is blocked by this session's network egress proxy, so this audit was built from search-engine-indexed data (titles, descriptions, indexed copy) rather than a live crawl. Findings marked ⚠ should be re-verified against the live page before acting.

---

## 1. What the page is today

| Element | Current state |
|---|---|
| URL | `/private-jet-charter/pet-travel/` (good: sits under the commercial /private-jet-charter/ hub) |
| Title tag | `Private Jet Pet Flight ▷ Dogs ▷ Cats ▷ Charter-A Ltd` |
| Core message | Pets fly in the cabin, never the hold — jets, helicopters and air taxis |
| Compliance copy | EU pet passport (or GB-issued before 1 Jan 2021); DEFRA-approved airport needed for UK arrivals; microchip + rabies + 21 days for EU entry |
| Structured data | ⚠ None detected in indexed data (no FAQPage / Service schema) |

## 2. Critical issues

### 2.1 Title tag is the weakest link
`Private Jet Pet Flight ▷ Dogs ▷ Cats ▷ Charter-A Ltd`

- **"Pet flight" is not the money term.** Every major competitor titles on *pet friendly private jet charter* (VistaJet, K9 Jets, Mercury Jets, Global Charter, Atlas, Charter Wind). That phrase carries the transactional "charter" modifier — the searcher ready to book.
- **▷ symbols** read as dated/spammy, waste pixel width, and depress CTR against clean competitor titles. Google frequently rewrites titles containing them, so you lose control of the SERP snippet.
- No location signal (UK/London) despite UK arrivals being the page's strongest differentiator.

**Recommended:** `Pet Friendly Private Jet Charter | Fly With Your Dog in the Cabin | Charter-A`
(If too long for the CMS: `Pet Friendly Private Jet Charter UK | Charter-A Ltd`)

### 2.2 Keyword cannibalization — four pages compete for the same terms
Indexed pet pages on the domain:

| URL | Indexed title | Role today |
|---|---|---|
| `/private-jet-charter/pet-travel/` | Private Jet Pet Flight ▷ Dogs ▷ Cats | Service page (this project's target) |
| `/pet-flights/` | Pet Flights by Private Jet: Charter-A Ltd — Travel in 2025 | Near-duplicate service/blog page |
| `/private-jet-dogs/` | Pet-Friendly Private Jets: Fly with Your Dog / dog flight gallery | Gallery/showcase |
| `/can-i-take-my-dog-on-a-private-jet/` | Can I take my dog on a private jet? | Q&A blog post |

Google has four candidate pages for "pet + private jet" queries and no clear signal which one to rank. **Fix (in order of impact):**

1. Crown `/private-jet-charter/pet-travel/` as the single **pillar money page** (the deliverable in `03-pet-travel-page-content.html`).
2. `/pet-flights/` — 301 redirect to the pillar, **or** strip its commercial copy and rewrite as a niche supporting piece. Its "Travel in 2025" title is also a stale-freshness signal in 2026.
3. `/private-jet-dogs/` — keep as a photo gallery (great trust content), but retitle to "Dogs on Board: Charter-A Pet Flight Gallery", remove competing commercial copy, and link up to the pillar with the anchor *pet friendly private jet charter*.
4. `/can-i-take-my-dog-on-a-private-jet/` — keep as a long-tail question post; add a prominent link to the pillar in the first paragraph and align its internal links.
5. New supporting article "Flying Pets into the UK by Private Jet" (deliverable `04-…`) links to the pillar with exact-match anchor, building a hub-and-spoke cluster instead of four rivals.

### 2.3 Compliance content is thin and partly outdated ⚠
The indexed copy leads with the EU pet passport ("issued in GB before 1 January 2021") and stops there. Missing, and expected by both users and Google for this query class:

- The **Animal Health Certificate (AHC)** route — the standard post-Brexit document for GB-based pets travelling to the EU and back.
- The **GB pet health certificate** for entries from non-EU countries.
- The **tapeworm rule for dogs**: vet-administered praziquantel treatment **24 hours to 5 days (120 hours)** before arrival in GB.
- The **21-day wait** after rabies vaccination stated for GB entry (currently only framed for the EU direction).
- Named **arrival airports for pets by private charter** (e.g. Biggin Hill — with the SkyPets reception team Charter-A already uses — Farnborough, Luton, Oxford, Manchester). Naming them wins the "which UK airports accept pets private jet" long tail no one owns well.
- Note to monitor: the 2025 UK–EU SPS agreement is expected to reintroduce UK pet passports; when implemented the page that updates fastest wins the news-driven searches.

### 2.4 Structure and conversion gaps
- **No FAQ section / FAQPage schema** — competitors win People-Also-Ask real estate here.
- **No Service schema** tying the page to the organisation.
- **No pricing guidance section** — "how much does it cost to fly a dog by private jet" is a high-intent query the page never answers, even in ranges.
- **No route examples** (London–Nice, London–Dubai, US–UK relocations) to catch route-modified searches.
- ⚠ Verify on the live page: single clear CTA above the fold, image `alt` text using pet keywords, and internal links from the site's highest-authority pages (homepage, /private-jet-charter/) into this page with descriptive anchors.

## 3. Domain-level quick wins
- Add a "Pet Friendly Charter" link to the main navigation or the /private-jet-charter/ hub — the money page currently relies on deep discovery.
- Destination pages (Nice, Cannes, Faro, Geneva…) should each carry one line + link: "Travelling with a dog? See our pet friendly private jet charter service."
- Refresh "Travel in 2025"-style titles across the domain; they now signal staleness.
- Biggin Hill airport page already mentions SkyPets — cross-link it to the pillar both ways.

## 4. Priority order
1. Rewrite title/meta + publish expanded pillar content (file 03).
2. Resolve cannibalization (301 `/pet-flights/`, retitle gallery, realign internal links).
3. Publish the UK-inbound article (file 04) and interlink.
4. Add FAQPage + Service schema (included in file 03).
5. Domain-wide internal links from destination pages.
