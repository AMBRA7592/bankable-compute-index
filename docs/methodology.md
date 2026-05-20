# Methodology

## Definition

Bankable compute is powered, permitted, networked accelerator capacity with a credible delivery date and a contract profile strong enough to support external financing.

The constraint is not one-dimensional. A facility with GPUs but no firm power is not bankable. A powered shell without HBM-backed accelerator allocation is not bankable. A campus with chips and power but weak customer contracts may be speculative merchant exposure, not infrastructure finance.

## Four quality grades

The methodology distinguishes four binary quality grades that apply across the scorecard. A high score on a given line requires the corresponding "good" side of each relevant grade.

| Grade | Good side | Weak side |
|---|---|---|
| 1. **Powered vs promised** | Energised, with firm interconnection rights | Announced capacity without delivered power |
| 2. **Priority access vs generic** | Allocation at the top of a constrained hierarchy | Generic waitlist or unstated priority |
| 3. **Contract-backed vs speculative** | Take-or-pay or prepaid contracts with creditworthy counterparties | Merchant exposure or thin contractual support |
| 4. **Refreshable vs stranded** | Credible hardware-refresh path; redeployment optionality | Asset obsolescence before debt amortisation |

These four grades map to the six scorecard lines as follows:

- **Power deliverability** → primarily *powered vs promised*
- **Accelerator access** → primarily *priority access vs generic* and *refreshable vs stranded*
- **HBM and advanced packaging** → primarily *refreshable vs stranded*
- **Sites and networks** → primarily *powered vs promised* and *priority access vs generic*
- **Creditworthy offtake** → primarily *contract-backed vs speculative*
- **Operating talent** → cross-cutting; affects refresh execution and priority management

A region or project scoring well on all four grades across all six lines is unambiguously bankable. A region scoring well on some grades and poorly on others is partially bankable and the gaps must be named.

## Six scorecard lines

1. **Power deliverability.** Firm, timely, price-competitive power for high-density loads; interconnection queue position; transformer and substation availability; dispatchable or flexible supply mix.
2. **Accelerator access.** Packaged GPUs or custom ASICs available by date, not merely wafer capacity or purchase intent; usable cluster count per capita and per unit of industrial output.
3. **HBM and advanced packaging.** High-bandwidth memory supply; advanced packaging throughput (CoWoS-class and successors); module integration; bottleneck visibility across generations.
4. **Sites and networks.** Permitted data-centre campuses with cooling, fiber, security, cloud interconnection, compliance and realistic commissioning schedules.
5. **Creditworthy offtake.** Take-or-pay contracts, public-sector anchor demand, industrial access commitments, prepayments, and customer-credit depth sufficient to support project finance.
6. **Operating talent.** Semiconductor, power-electronics, data-centre, grid, RF, networking, cloud-SRE and project-finance operating capability; permitting teams and regulatory execution capacity. *Operating talent is the most subjective scorecard line; defensible proxies include count of licensed grid operators, semiconductor engineering output, and depth of independent data-centre operators.*

## Scoring principle

Each indicator receives:

- `score`: integer 0-5 (0 = no evidence of capacity, 5 = strong observed capacity)
- `confidence`: `observed`, `estimated`, or `missing`
- `source_id`: linked to an entry in `data/sources.yaml`
- `as_of_date`: date of the underlying observation
- `notes`: short caveat or context

A region can score highly only where the evidence is both strong and current. **Missing public data is recorded explicitly as `missing` rather than silently inferred.** This is the v0.1 posture: better to show absence of evidence than to fabricate confidence.

When `confidence = missing`, the `score` field is left empty. When `confidence = observed` or `estimated`, the `score` must be an integer 0-5.

## Update cadence

The Index is versioned. Each minor version (v0.2, v0.3...) reflects substantive methodological or data updates documented in release notes. The `notes/monthly-monitor.md` file tracks new market-structure events, financing transactions, physical constraints and policy moves that may inform the next version.

## What this methodology does not claim

- It does not claim to be a complete ranking of national or regional AI capacity.
- It does not claim that the four quality grades are exhaustive; they are the v0.1 conceptual cut.
- It does not claim to substitute for project-level due diligence. Scoring a region on these six lines is a starting point, not a complete assessment of any specific facility, transaction or contract.
- It does not provide investment advice.

The methodology is a public reference layer, designed to be inspectable, citable and improvable. Disagreement with the weighting or definitions is a feature, not a bug.
