import pandas as pd
import yfinance as yf

from database import get_engine


TICKERS = [
    "AAPL",
    "MSFT",
    "NVDA",
    "AMZN",
    "GOOGL"
]


def main():

    all_data = []

    for ticker in TICKERS:

        print(f"Загрузка {ticker}")

        df = yf.download(
            ticker,
            start="2023-01-01",
            progress=False,
            auto_adjust=True
        )

        df = df.reset_index()

        # если yfinance вернул MultiIndex
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = [col[0] for col in df.columns]

        df["ticker"] = ticker

        all_data.append(df)

    result = pd.concat(
        all_data,
        ignore_index=True
    )

    engine = get_engine()

    result.to_sql(
        "stocks",
        engine,
        if_exists="replace",
        index=False
    )

    print("Данные сохранены")


if __name__ == "__main__":
    main()