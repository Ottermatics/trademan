"""Top-level package for trademan."""

__author__ = """Kevin Russell"""
__email__ = "kevin@ottermatics.com"
__version__ = "0.1.0"

from .data import get_tickers, get_ticker_perf
from .portfolio import make_portfolio, plot_portfolio

__all__ = ["get_tickers", "get_ticker_perf", "make_portfolio", "plot_portfolio"]
