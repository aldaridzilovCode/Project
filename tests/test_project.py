import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

import pandas as pd

from database import get_engine


def test_database_connection():

    engine = get_engine()

    assert engine is not None


def test_stocks_table_exists():

    engine = get_engine()

    df = pd.read_sql(
        "SELECT * FROM stocks LIMIT 5",
        engine
    )

    assert len(df) > 0


def test_indicators_table_exists():

    engine = get_engine()

    df = pd.read_sql(
        "SELECT * FROM stocks_indicators LIMIT 5",
        engine
    )

    assert len(df) > 0


def test_ticker_column_exists():

    engine = get_engine()

    df = pd.read_sql(
        "SELECT * FROM stocks LIMIT 1",
        engine
    )

    assert "ticker" in df.columns


def test_close_column_exists():

    engine = get_engine()

    df = pd.read_sql(
        "SELECT * FROM stocks LIMIT 1",
        engine
    )

    assert "Close" in df.columns


def test_ma20_exists():

    engine = get_engine()

    df = pd.read_sql(
        "SELECT * FROM stocks_indicators LIMIT 100",
        engine
    )

    assert "MA20" in df.columns


def test_ma50_exists():

    engine = get_engine()

    df = pd.read_sql(
        "SELECT * FROM stocks_indicators LIMIT 100",
        engine
    )

    assert "MA50" in df.columns


def test_rsi_exists():

    engine = get_engine()

    df = pd.read_sql(
        "SELECT * FROM stocks_indicators LIMIT 100",
        engine
    )

    assert "RSI" in df.columns


def test_macd_exists():

    engine = get_engine()

    df = pd.read_sql(
        "SELECT * FROM stocks_indicators LIMIT 100",
        engine
    )

    assert "MACD" in df.columns


def test_tickers_count():

    engine = get_engine()

    df = pd.read_sql(
        "SELECT * FROM stocks",
        engine
    )

    assert len(df["ticker"].unique()) == 5