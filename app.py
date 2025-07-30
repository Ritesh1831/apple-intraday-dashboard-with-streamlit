import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
from datetime import datetime

st.set_page_config(
    page_title="aapl-intraday-dashboard",
    layout="wide"
)

st.title("Apple Inc. Intraday Dashboard")

st.sidebar.title("Controls")

refresh_interval = st.sidebar.slider("Auto-refresh interval (sec)", 10, 300, 60)
st.sidebar.write(f"Data refreshes every {refresh_interval} seconds")

symbol = "AAPL"

@st.cache_data(ttl=refresh_interval)
def load_data(symbol):
    df = pd.read_csv('AAPL.csv', index_col=0)
    df.index = pd.to_datetime(df.index)
    return df

df = load_data(symbol)

# --- Page selector ---
page = st.sidebar.radio("Go to", ["Price & Volume Charts", "Distribution & Correlation"])

# --- Page 1 ---
if page == "Price & Volume Charts":
    st.header(f"📈 Price & Volume Analysis for {symbol}")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Close Price Over Time")
        fig1, ax1 = plt.subplots(figsize=(12, 5))
        ax1.plot(df.index, df['close'], color='blue')
        ax1.set_xlabel("Time")
        ax1.set_ylabel("Price (USD)")
        ax1.grid(True)
        st.pyplot(fig1, use_container_width=True)

    with col2:
        st.subheader("OHLC Prices Over Time")
        fig2, ax2 = plt.subplots(figsize=(12, 5))
        ax2.plot(df.index, df['open'], label='Open', color='green')
        ax2.plot(df.index, df['high'], label='High', color='red')
        ax2.plot(df.index, df['low'], label='Low', color='orange')
        ax2.plot(df.index, df['close'], label='Close', color='blue')
        ax2.set_xlabel("Time")
        ax2.set_ylabel("Price (USD)")
        ax2.legend()
        ax2.grid(True)
        st.pyplot(fig2, use_container_width=True)

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Candlestick Chart")
        fig3 = go.Figure(data=[go.Candlestick(
            x=df.index,
            open=df['open'],
            high=df['high'],
            low=df['low'],
            close=df['close']
        )])
        fig3.update_layout(xaxis_title='Time', yaxis_title='Price (USD)')
        st.plotly_chart(fig3, use_container_width=True)

    with col4:
        st.subheader("Volume Over Time")
        fig4, ax4 = plt.subplots(figsize=(12, 5))
        ax4.plot(df.index, df['volume'], color='purple')
        ax4.set_xlabel("Time")
        ax4.set_ylabel("Volume")
        ax4.grid(True)
        st.pyplot(fig4, use_container_width=True)

# --- Page 2 ---
else:
    st.header(f"📊 Distribution & Correlation for {symbol}")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Histogram of Close Prices")
        fig5, ax5 = plt.subplots(figsize=(12, 5))
        ax5.hist(df['close'], bins=20, color='skyblue', edgecolor='black')
        ax5.set_xlabel("Close Price")
        ax5.set_ylabel("Frequency")
        st.pyplot(fig5, use_container_width=True)

    with col2:
        st.subheader("Histogram of Volumes")
        fig6, ax6 = plt.subplots(figsize=(12, 5))
        ax6.hist(df['volume'], bins=20, color='lightgreen', edgecolor='black')
        ax6.set_xlabel("Volume")
        ax6.set_ylabel("Frequency")
        st.pyplot(fig6, use_container_width=True)

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Correlation Heatmap")
        fig7, ax7 = plt.subplots(figsize=(12, 5))
        corr = df[['open', 'high', 'low', 'close', 'volume']].corr()
        sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax7)
        st.pyplot(fig7, use_container_width=True)

    with col4:
        st.subheader("Close Price with 20-period Moving Average")
        fig8, ax8 = plt.subplots(figsize=(12, 5))
        ax8.plot(df.index, df['close'], label='Close Price', color='blue')
        ax8.plot(df.index, df['close'].rolling(window=20).mean(), label='20-Period MA', color='red')
        ax8.set_xlabel("Time")
        ax8.set_ylabel("Price (USD)")
        ax8.legend()
        ax8.grid(True)
        st.pyplot(fig8, use_container_width=True)
