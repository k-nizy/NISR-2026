# 02 — Track Selection

**Status: not decided** — the team reviews this page and picks one before the Canvas declaration.

## The three tracks

### Track 1 — Agricultural Productivity 🌾
Solutions on irrigation, soil conservation, post-harvest storage, processing/value addition, or export market access — informed by NISR agriculture / food-security / climate data.

- *Strength:* Rich, well-published NISR data (SAS, EICV, ASYB); easy to demonstrate national impact.
- *Risk:* Popular track — differentiation comes from the model/UX, not the topic.

### Track 2 — Financial Inclusion & Poverty Reduction 💰
Solutions on financial exclusion, poverty dynamics, or the impact of social protection programs (e.g., Vision Umurenge) — informed by NISR poverty / income / financial-access data.

- *Strength:* FINScope + EICV give unusually deep financial-access microdata; strong policy story.
- *Risk:* Sensitive microdata access can be restricted; scope can balloon.

### Track 3 — Open Innovation 🚀
Any sector (health, education, agriculture, finance, transport…) aligned with **NST2 or Vision 2050** priorities. Least constrained, but still needs explicit national-priority alignment — **not a free-for-all**.

- *Strength:* Freedom to play to the team's ML strengths; less competition on the obvious datasets.
- *Risk:* Judges expect a clearly argued NST2/Vision 2050 linkage; weaker alignment = weaker score.

## Decision matrix (fill in 1–5 and total)

| Criterion | Weight | T1 Agriculture | T2 Financial | T3 Open |
|---|---|---|---|---|
| Data accessibility (NISR microdata available) | ×3 | 5 | 4 | 3 |
| Team skill fit (ML pipeline strength) | ×3 | 4 | 4 | 4 |
| Novelty vs other teams | ×2 | 2 | 3 | 4 |
| Clear NST2/V2050 alignment story | ×2 | 5 | 5 | 4 |
| Feasible in hackathon timeframe | ×2 | 4 | 3 | 5 |
| **Total** | | **49** | **46** | **47** |

## Example project angles per track

| Track | Example angle | NISR datasets to start with |
|---|---|---|
| 1 | Predict district-level post-harvest loss risk; recommend storage investment | SAS 2024 agri module, ASYB, CFSVA |
| 2 | District financial-exclusion index + targeting model for social protection | FINScope 2024, EICV5 poverty module, BNR access data |
| 3 | School-to-work transition predictor for Rwandan youth (education + labour) | EICV5 labour module, LFS 2024, NISR education stats |

**Decision:** Track 1 — Agricultural Productivity — agreed by both members on 2026-10-06
