"""gs-quant standalone timeseries demo.

Runs Goldman Sachs' gs-quant timeseries analytics on a synthetic price
series — no Marquee access, no credentials, no network calls to Goldman.

What this uses (all pure pandas-Series math, verified offline in
gs-quant 2.2.5): returns (simple and log), rolling annualised volatility,
moving average, exponential moving average, max drawdown, rolling mean/std,
beta and correlation vs a benchmark, variance of returns, Bollinger bands,
RSI, MACD, annualised return.

Deliberately NOT used — these need Marquee in 2.2.5 and are out of scope:
  - realized_volatility() takes a Marquee Asset, not a Series.
  - standard_deviation(), skewness(), kurtosis(), sortino_ratio(),
    calmar_ratio(), downside_risk() take Marquee report/benchmark ids.
  - log_return() is a logging helper in this module, not a returns
    function — log returns come from returns(..., type=Returns.LOGARITHMIC).
  - There is no gs_quant.backtest module in 2.2.5.

Data: geometric Brownian motion, 252 business days, fixed seed 42.
Nothing is downloaded; nothing leaves the machine.

Run from the repo root after `pip install -r requirements.txt`:
    python examples/gs_quant_timeseries_demo.py
"""

import numpy as np
import pandas as pd
from gs_quant.timeseries import (
    annualize,
    beta,
    bollinger_bands,
    correlation,
    exponential_moving_average,
    macd,
    max_drawdown,
    mean,
    moving_average,
    relative_strength_index,
    returns,
    std,
    var,
    volatility,
)
from gs_quant.timeseries.helper import Returns

SEED = 42
BENCH_SEED = 7
DAYS = 252
START_PRICE = 100.0
MU = 0.0005
SIGMA = 0.01


def build_series(seed: int, mu: float, sigma: float) -> pd.Series:
    rng = np.random.default_rng(seed)
    shocks = rng.normal(mu, sigma, DAYS)
    prices = START_PRICE * np.exp(np.cumsum(shocks))
    index = pd.bdate_range("2026-01-01", periods=DAYS)
    return pd.Series(prices, index=index)


def main() -> None:
    prices = build_series(SEED, MU, SIGMA)
    bench = build_series(BENCH_SEED, 0.0004, 0.008)

    simple = returns(prices)
    log = returns(prices, type=Returns.LOGARITHMIC)
    vol21 = volatility(prices, 21)
    ma20 = moving_average(prices, 20)
    ema = exponential_moving_average(prices, 0.9)
    dd63 = max_drawdown(prices, 63)
    roll_mean = mean(prices)
    roll_std = std(prices)
    b = beta(prices, bench)
    corr = correlation(prices, bench)
    ret_var = var(simple)
    bands = bollinger_bands(prices, 20)
    rsi = relative_strength_index(prices, 14)
    macd_s = macd(prices)
    ann_ret = annualize(simple)

    print("gs-quant timeseries demo — synthetic GBM, 252 business days, seed 42")
    print(f"last price: {prices.iloc[-1]:.2f}  "
          f"(start {START_PRICE:.2f}, total return {prices.iloc[-1] / START_PRICE - 1:.2%})")
    print(f"simple return (last day): {simple.iloc[-1]:.4%}")
    print(f"log return (last day): {log.iloc[-1]:.4%}")
    print(f"annualised return (last): {ann_ret.iloc[-1]:.2%}")
    print(f"rolling 21d annualised vol (last): {vol21.iloc[-1]:.2f}%  (mean {vol21.mean():.2f}%)")
    print(f"20d moving average (last): {ma20.iloc[-1]:.2f}")
    print(f"exponential moving average (last): {ema.iloc[-1]:.2f}")
    print(f"63d max drawdown (last): {dd63.iloc[-1]:.2%}  (worst {dd63.min():.2%})")
    print(f"rolling mean / std of price (last): {roll_mean.iloc[-1]:.2f} / {roll_std.iloc[-1]:.2f}")
    print(f"beta vs benchmark (last): {b.iloc[-1]:.3f}")
    print(f"correlation vs benchmark (last): {corr.iloc[-1]:.3f}")
    print(f"variance of daily returns (last): {ret_var.iloc[-1]:.6f}")
    print(f"Bollinger bands 20d (last): lower {bands.iloc[-1, 0]:.2f} / upper {bands.iloc[-1, 1]:.2f}")
    print(f"RSI 14 (last): {float(rsi.iloc[-1]):.1f}")
    print(f"MACD (last): {float(macd_s.iloc[-1]):.4f}")
    print("OK — all functions ran locally on synthetic data, no Marquee calls.")


if __name__ == "__main__":
    main()
