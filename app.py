import pandas as pd
import streamlit as st
import plotly.graph_objects as go

from database import get_engine

st.set_page_config(
    page_title="Инвестиционный анализ",
    layout="wide"
)

engine = get_engine()

df = pd.read_sql(
    "SELECT * FROM stocks_indicators",
    engine
)

st.title(
    "Система анализа инвестиционных инструментов"
)

# список тикеров
tickers = sorted(
    df["ticker"].unique()
)

ticker = st.sidebar.selectbox(
    "Выберите тикер",
    tickers
)

# фильтрация по выбранному тикеру
stock = df[
    df["ticker"] == ticker
].copy()

# преобразование даты
stock["Date"] = pd.to_datetime(
    stock["Date"]
)

tab1, tab2, tab3 = st.tabs(
    [
        "Котировки",
        "Индикаторы",
        "Статистика"
    ]
)

# -------------------
# Вкладка Котировки
# -------------------

with tab1:

    st.subheader(
        f"Цена акции {ticker}"
    )

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=stock["Date"],
            y=stock["Close"],
            name="Цена"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=stock["Date"],
            y=stock["MA20"],
            name="MA20"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=stock["Date"],
            y=stock["MA50"],
            name="MA50"
        )
    )

    fig.update_layout(
        height=600
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# -------------------
# Вкладка Индикаторы
# -------------------

with tab2:

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("RSI")

        fig_rsi = go.Figure()

        fig_rsi.add_trace(
            go.Scatter(
                x=stock["Date"],
                y=stock["RSI"],
                name="RSI"
            )
        )

        fig_rsi.update_layout(
            height=400
        )

        st.plotly_chart(
            fig_rsi,
            use_container_width=True
        )

    with col2:

        st.subheader("MACD")

        fig_macd = go.Figure()

        fig_macd.add_trace(
            go.Scatter(
                x=stock["Date"],
                y=stock["MACD"],
                name="MACD"
            )
        )

        fig_macd.add_trace(
            go.Scatter(
                x=stock["Date"],
                y=stock["MACD_SIGNAL"],
                name="Signal"
            )
        )

        fig_macd.update_layout(
            height=400
        )

        st.plotly_chart(
            fig_macd,
            use_container_width=True
        )

# -------------------
# Вкладка Статистика
# -------------------

with tab3:

    st.subheader(
        "Основные показатели"
    )

    latest = stock.iloc[-1]

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Цена",
        f"{latest['Close']:.2f}"
    )

    c2.metric(
        "MA20",
        f"{latest['MA20']:.2f}"
    )

    c3.metric(
        "RSI",
        f"{latest['RSI']:.2f}"
    )

    c4.metric(
        "MACD",
        f"{latest['MACD']:.2f}"
    )

    st.subheader(
        "Последние записи"
    )

    st.dataframe(
        stock.tail(20),
        use_container_width=True
    )