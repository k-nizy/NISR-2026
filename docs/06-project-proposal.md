# 06 — Project Proposal (working draft)

> **Track: 1 — Agricultural Productivity.** All three tracks are scoped below so the team can compare and commit. Once a track is chosen, mark it here — it becomes the foundation of the ML Pipeline project.

## 1. Problem statements (one per track)

### Track 1 — Agricultural Productivity
**Problem:** Rwandan farmers lose a significant share of harvests after harvest due to inadequate storage and poorly timed market decisions, and districts lack a forward-looking view of *where* post-harvest losses will concentrate next season.

**Proposed solution:** A district/season-level **post-harvest loss risk model** that combines NISR agriculture data (SAS) with food-security and climate indicators, and outputs (a) a risk score per district and (b) simple "what to do" recommendations — where to position storage, when to sell vs store.

- **Target users:** district agricultural officers, cooperatives, MAY/NISR planners
- **NST2/V2050 linkage:** agriculture productivity & food-security priorities

### Track 2 — Financial Inclusion & Poverty Reduction
**Problem:** Financial exclusion in Rwanda is unevenly distributed across districts and demographics, yet social-protection budgets are allocated without fine-grained, data-driven targeting of where exclusion and poverty dynamics overlap.

**Proposed solution:** A **district financial-exclusion index + social-protection targeting dashboard**: fuse FINScope/EICV financial-access and poverty data, compute an exclusion index per district and demographic segment, and highlight where programs (e.g., VUP) would have the highest marginal impact.

- **Target users:** MINVAF/LODA planners, financial-sector policymakers, researchers
- **NST2/V2050 linkage:** poverty reduction, universal financial inclusion

### Track 3 — Open Innovation
**Problem:** Rwandan youth face a messy school-to-work transition; students and policymakers lack a data-driven view of which study paths and districts lead to employment, and which skills gaps matter most.

**Proposed solution:** A **school-to-work transition explorer**: model employment outcomes by education path, district, and demographics using EICV/LFS data; surface predicted employment probability + top skills gaps; visualise by district to guide both students and policy.

- **Target users:** students, education planners, labour-market policymakers
- **NST2/V2050 linkage:** human capital development, youth employment (NST2 priority)

## 2. NISR & companion data sources

| Source | What it gives | Used by |
|---|---|---|
| **NISR SAS** (Seasonal Agricultural Survey) | crop production, agri practices, inputs | Track 1 |
| **CFSVA** (Comprehensive Food Security & Vulnerability Analysis) | food security, vulnerability by district | Track 1 |
| **EICV** (Integrated Household Living Conditions Survey) | poverty, income, consumption, labour, education, financial behaviour | Tracks 2, 3 |
| **FINScope Rwanda** | financial inclusion/access microdata | Track 2 |
| **NISR LFS** (Labour Force Survey) | employment, unemployment, informal work | Track 3 |
| **ASYB** (Annual Statistical Yearbook) + statistics.gov.rw indicators API | cross-sector official indicators | all |
| Climate/open data (e.g., rainfall via open climate APIs) | optional enrichment | Track 1 |

All three tracks **require NISR data**; other open datasets are optional additions.

## 3. ML pipeline sketch (carry-forward into ML Pipeline course)

```
data/raw  ──► ingest (download NISR microdata, document provenance)
        ──► clean & validate (schemas, district code harmonisation)
        ──► features (district-level aggregates, indices)
        ──► model (baseline: ridge/forest; iterate: gradient boosting)
        ──► evaluate ( district-level CV, baseline comparison)
        ──► serve (dashboard / simple API)
        ──► docs (method notes, data dictionary, decisions log)
```

## 4. Success criteria (for the hackathon submission, 30 Oct 2026)

- Working **GitHub repo** (this one) with reproducible pipeline
- **Deployed app** (dashboard) demonstrating the solution
- **Documentation**: problem, data sources, method, results, limitations
- Clear, explicit NISR data usage and NST2/V2050 alignment

## 5. Immediate next actions

1. Both members score the decision matrix in [02-track-selection.md](02-track-selection.md)
2. Pick the track → mark it here and in the Canvas group
3. Team name finalised → used on NISR form
4. Canvas declaration → Loom-recorded registration → Canvas submission
5. Create `data/`, `notebooks/`, `src/` folders and start the EDA notebook for the chosen track
