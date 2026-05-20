# Bankable Compute Index

**Version 0.1 — A public, source-backed framework for assessing the bankability of AI compute capacity.**

## Thesis

The scarce unit in AI infrastructure is not data, generic GPU supply, or even installed compute. It is *bankable compute*: powered, permitted, networked AI capacity with a credible delivery date and a customer contract strong enough to support external financing.

The Index distinguishes four quality grades of capacity:

- **Powered vs promised** — Is the megawatt actually energised, or only announced?
- **Priority access vs generic** — Does the buyer sit at the top of an allocation hierarchy, or merely on a waitlist?
- **Contract-backed vs speculative** — Is the revenue claim creditworthy and term-defined, or merchant exposure?
- **Refreshable vs stranded** — Is there a credible hardware-refresh path, or will the asset be obsolete before debt amortises?

## What this is (and isn't)

This is a **methodology**, not a ranking. v0.1 ships an inspectable framework with explicit confidence grades and visible missing data. The goal is not to claim perfect measurement accuracy. The goal is to make the underwriting framework legible, citable, and improvable by others.

This is **not** investment advice, a credit rating, or a substitute for primary due diligence. It is a public reference layer.

## Repository structure

```
docs/methodology.md            Definitions, scoring rules, four quality grades
schema/scorecard.yaml          Indicator schema (six scoring lines, fields)
data/sources.yaml              Primary-source ledger with stable IDs and dates
data/regions.csv               Region-by-indicator panel (v0.1: skeleton with missing flags)
notes/monthly-monitor.md       Template for tracking new events
site/index.html                Static landing page (Vercel-deployable)
scripts/validate.py            Schema validator (run locally or in CI)
.github/workflows/validate.yml GitHub Action: validates schema on push and PR
```

## The six scorecard lines

1. **Power deliverability** — Firm, timely, price-competitive power for high-density loads.
2. **Accelerator access** — Packaged GPUs or custom ASICs available by date, not merely wafer capacity or purchase intent.
3. **HBM and advanced packaging** — High-bandwidth memory supply and CoWoS-class packaging throughput.
4. **Sites and networks** — Permitted campuses with cooling, fiber, security, cloud interconnection, realistic commissioning schedules.
5. **Creditworthy offtake** — Take-or-pay contracts, public-sector anchor demand, prepayments, customer-credit depth sufficient to support project finance.
6. **Operating talent** — Semiconductor, power-electronics, grid, data-centre, networking and project-finance operating capability.

See `docs/methodology.md` for scoring rules and the mapping from these six lines to the four quality grades above.

## Audience

- **Infrastructure investors** can use it as an underwriting checklist for AI capacity projects.
- **Finance ministries and development banks** can argue with the methodology and adapt it to sovereign assessment.
- **Editors, analysts and newsletter writers** can cite it as a source-backed reference layer.
- **Researchers** can contribute better data, propose indicator refinements, or fork the framework.

## How to cite

Recommended citation:

> Brandes, Amadeus. *Bankable Compute Index*, version 0.1, May 2026.
> Available at [repository URL].

A machine-readable citation is provided in `CITATION.cff`.

## Contributing

This is v0.1. Contributions welcome via pull request, especially:

- Filling in missing-flagged cells in `data/regions.csv` with sourced evidence
- Proposing refinements to indicator definitions in `schema/scorecard.yaml`
- Adding entries to the monthly monitor as new financing or policy events occur
- Suggesting additional regions for the panel

Schema integrity is enforced by `scripts/validate.py`, which runs automatically on every push via GitHub Actions.

## Licensing

This work is licensed under [Creative Commons Attribution 4.0 International (CC-BY-4.0)](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt the methodology and data, with attribution. See `LICENSE`.

The schema validator script in `scripts/` is also separately available under the MIT License for embedding in derivative tools.

## Status

**v0.1 — May 2026.** Initial public release. The region panel is intentionally sparse; populating it transparently with sourced evidence is the work of v0.2 and beyond. The four-grade quality framework and six-line scorecard are the v0.1 conceptual contribution.

## Author

Amadeus Brandes, independent researcher.
