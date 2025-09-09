# Trademan

[![PyPI version](https://badge.fury.io/py/trademan.svg)](https://badge.fury.io/py/trademan)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://ottermatics.github.io/trademan/)

A Python library and CLI tool for gathering market data and generating optimal portfolios using modern portfolio theory.

## Features

- 📊 **Market Data Collection**: Automated downloading and caching of S&P 500 and ETF data via yfinance
- 🎯 **Portfolio Optimization**: Multiple optimization strategies (Sharpe ratio, minimum volatility, etc.)
- 📈 **Visualization**: Generate beautiful portfolio allocation charts
- 🚀 **CLI Interface**: Easy-to-use command-line tools for quick analysis
- 🐍 **Python API**: Full programmatic access for custom workflows
- 💾 **Smart Caching**: Intelligent data caching to minimize API calls

## Installation

Install from PyPI:
```bash
pip install trademan
```

Install from source:
```bash
pip install git+https://github.com/ottermatics/trademan.git
```

## Quick Start

### CLI Usage

1. **Download Market Data**:
```bash
market_dl  # Downloads S&P 500 and ETF data
```

2. **Generate a Portfolio**:
```bash
# Create a Sharpe-optimized portfolio with $10,000 allocation
trademan -cls stocks -alloc 10000 -opt sharpe

# Minimum volatility ETF portfolio  
trademan -cls etfs -opt min_volatility -alloc 100000 -in QQQ,SPY,VTI
```

### Python API

```python
import trademan

# Get stock data for specific tickers
data = trademan.get_tickers(['AAPL', 'MSFT', 'GOOGL'])

# Create optimized portfolio
weights = trademan.make_portfolio(
    data, 
    opt='sharpe',           # Optimization method
    risk='ledoit_wolf',     # Risk model  
    allocate_amount=10000   # Dollar amount
)

# Visualize the portfolio
fig, ax = trademan.plot_portfolio(weights)
```

## CLI Options

| Option | Description | Default |
|--------|-------------|---------|
| `-cls` | Asset class: `etfs`, `stocks`, `all` | `all` |
| `-opt` | Optimization: `sharpe`, `min_volatility`, `eff_return`, `eff_risk` | `sharpe` |
| `-risk` | Risk model: `covariance`, `ledoit_wolf` | `ledoit_wolf` |
| `-alloc` | Amount to allocate (shows share counts) | None |
| `-gamma` | Weight regularization (higher = more diversified) | 2 |
| `-in` | Include specific tickers (comma-separated) | None |
| `-ex` | Exclude specific tickers (comma-separated) | None |
| `-min-wght` | Minimum weight threshold for assets | 0.01 |
| `-max-wght` | Maximum weight limit per asset | None |

## Configuration

Set environment variables to customize data storage:

```bash
export TRADEMAN_DATA_DIR="/path/to/data"      # Market data cache
export TRADEMAN_MEDIA_DIR="/path/to/charts"   # Generated charts
```

## Examples

### 1. Best Performing S&P 500 Stocks
Create a portfolio favoring established companies with cycle penalties:

```bash
trademan -cls stocks -gamma 1 -alloc 10000 -cycl-err 10 -max-wght 0.2
```

![Stocks Portfolio](./media/Stocks.png)

### 2. Low Volatility ETF Portfolio
Generate a conservative ETF allocation:

```bash
trademan -cls etfs -gamma 0.1 -alloc 100000 \
  -in QQQ,SCHG,VGT,SLV,VIG,SPY,VOO,VUG,IAU,PAVE \
  -opt min_volatility
```

![ETF Portfolio](./media/ETFS_Min_Volatility.png)

## How It Works

1. **Data Collection**: Downloads historical price data using yfinance
2. **Risk Modeling**: Calculates covariance matrices with Ledoit-Wolf shrinkage
3. **Return Estimation**: Uses mean historical returns with optional adjustments
4. **Optimization**: Applies modern portfolio theory via PyPortfolioOpt
5. **Allocation**: Converts weights to discrete share quantities
6. **Visualization**: Creates publication-ready portfolio charts

## Dependencies

- **PyPortfolioOpt**: Portfolio optimization algorithms
- **yfinance**: Market data source
- **pandas/numpy**: Data manipulation
- **matplotlib**: Visualization
- **diskcache**: Data caching
- **scikit-learn**: Additional analytics

## Development

Install development dependencies:
```bash
pip install -e .[dev]
```

Run tests:
```bash
pytest
```

## License

MIT License - see [LICENSE](LICENSE) for details.

## Contributing

Contributions welcome! Please read [CONTRIBUTING.rst](CONTRIBUTING.rst) for guidelines.