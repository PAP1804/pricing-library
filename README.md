# pricing-library

The pricing library for the Financial Engineering & Quant Trading track — the FE mastery gate (Tier 2).

## What it must do

Price, with tests:

- **European and American options**
- **Barrier and Asian exotics**
- **Interest-rate swaps**
- **Greeks** for all of the above
- **Vol-surface calibration**

Built with QuantLib or from scratch — either way, the tests are the proof. The library is the pricing core the later builds call: the backtester prices through it, the vol-surface backtester calibrates through it, and the paper-trading system executes through it.

## Repo standard

- README states the method, the results with numbers after realistic costs, how to run it in one command, and the failure modes / when it breaks.
- Pinned dependencies, fixed seeds, tests with CI. A pricing function without a test does not ship.
- Public or synthetic data only — no employer code or data, ever. No secrets, no credentials, no brokerage account details.
- A build ships at its phase exit gate, not before: the gate is the code review.

## Track

Part of the zero-to-top-3% quant trading curriculum. Foundations and paper labs live in `quant-foundations-labs`; each flagship build has its own repo (created when its phase starts).
