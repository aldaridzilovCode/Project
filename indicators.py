import pandas as pd
import ta

from database import get_engine


def calculate_indicators():

    engine = get_engine()

    df = pd.read_sql(
        "SELECT * FROM stocks",
        engine
    )

    result = []

    for ticker in df["ticker"].unique():

        print(f"Обработка {ticker}")

        stock = df[df["ticker"] == ticker].copy()

        stock["MA20"] = (
            stock["Close"]
            .rolling(window=20)
            .mean()
        )

        stock["MA50"] = (
            stock["Close"]
            .rolling(window=50)
            .mean()
        )

        stock["RSI"] = ta.momentum.RSIIndicator(
            close=stock["Close"],
            window=14
        ).rsi()

        macd = ta.trend.MACD(
            close=stock["Close"]
        )

        stock["MACD"] = macd.macd()
        stock["MACD_SIGNAL"] = macd.macd_signal()

        result.append(stock)

    result = pd.concat(
        result,
        ignore_index=True
    )

    result.to_sql(
        "stocks_indicators",
        engine,
        if_exists="replace",
        index=False
    )

    print("Индикаторы рассчитаны успешно")


if __name__ == "__main__":
    calculate_indicators()