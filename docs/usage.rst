=====
Usage
=====

Command Line Interface
======================

Trademan provides two main CLI commands:

Data Collection
---------------

Download market data for S&P 500 stocks and ETFs::

    market_dl

This downloads and caches stock data using yfinance, storing it in a location customizable via the ``TRADEMAN_DATA_DIR`` environment variable.

Portfolio Optimization
----------------------

Generate optimized portfolios::

    trademan [OPTIONS]

Key options include:

* ``-cls {etfs,stocks,all}``: Choose asset class (default: all)
* ``-opt {sharpe,min_volatility,eff_return,eff_risk}``: Optimization method (default: sharpe)  
* ``-risk {covariance,ledoit_wolf}``: Risk model (default: ledoit_wolf)
* ``-alloc AMOUNT``: Money to allocate (shows share quantities)
* ``-gamma GAMMA``: Weight regularization parameter
* ``-in TICKERS``: Include specific tickers (comma-separated)
* ``-ex TICKERS``: Exclude specific tickers (comma-separated)

Examples::

    # Best performing S&P 500 stocks with $10,000 allocation
    trademan -cls stocks -gamma 1 -alloc 10000 -cycl-err 10 -max-wght 0.2

    # Minimum volatility ETF portfolio  
    trademan -cls etfs -opt min_volatility -alloc 100000 -in QQQ,SPY,VTI

Python API
==========

Basic usage in Python::

    import trademan
    
    # Get stock data
    data = trademan.get_tickers(['AAPL', 'MSFT', 'GOOGL'])
    
    # Create optimized portfolio
    weights = trademan.make_portfolio(data, opt='sharpe', allocate_amount=10000)
    
    # Plot portfolio
    fig, ax = trademan.plot_portfolio(weights)

Configuration
=============

Environment Variables
--------------------

* ``TRADEMAN_DATA_DIR``: Directory for cached market data (default: temp/trademan/data)
* ``TRADEMAN_MEDIA_DIR``: Directory for generated charts (default: temp/trademan/media)

Data Caching
------------

Market data is cached using diskcache:

* Performance data: 5 days
* Company info: 30 days
* Failed tickers are tracked to avoid repeated API calls
