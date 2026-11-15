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

## gs-quant (standalone timeseries)

Goldman Sachs' open-source Python toolkit for quantitative finance
([goldmansachs/gs-quant](https://github.com/goldmansachs/gs-quant), Apache-2.0),
installed as `gs-quant==2.2.5` in `requirements.txt` (Python 3.10+).

What works here: the standalone `gs_quant.timeseries` functions, pure
pandas-Series math on local data — returns (simple and log), rolling
annualised volatility, moving/exp averages, max drawdown, beta, correlation,
Bollinger bands, RSI, MACD. Demo: `examples/gs_quant_timeseries_demo.py`
(synthetic geometric Brownian motion, 252 business days, seed 42).

The credential gate: the Marquee-backed pricing, risk, and data endpoints
need a Goldman Sachs institutional client id/secret, which this repo does
not have — they are never called, and no credential lives in this repo.
Functions that take Marquee objects (`realized_volatility`,
`standard_deviation`, `skewness`, `kurtosis`, `sortino_ratio`,
`calmar_ratio`, `downside_risk`) are not used. There is no
`gs_quant.backtest` module in 2.2.5. gs-quant is a reference and a
timeseries utility here, not the pricing core — the pricers in "What it
must do" are built from scratch (or QuantLib) with tests.

Run it:

```bash
pip install -r requirements.txt
python examples/gs_quant_timeseries_demo.py
```

## Track

Part of the zero-to-top-3% quant trading curriculum. Foundations and paper labs live in `quant-foundations-labs`; each flagship build has its own repo (created when its phase starts).
