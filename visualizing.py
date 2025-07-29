import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('cleaned_intraday.csv', index_col=0)
df.index = pd.to_datetime(df.index)

# --- Plot 1: Close Price Line Chart ---
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['close'], label='Close Price', color='blue')
plt.title('Close Price Over Time')
plt.xlabel('Time')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

# --- Plot 2: OHLC Line Chart ---
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['open'], label='Open', color='green')
plt.plot(df.index, df['high'], label='High', color='red')
plt.plot(df.index, df['low'], label='Low', color='orange')
plt.plot(df.index, df['close'], label='Close', color='blue')
plt.title('OHLC Prices Over Time')
plt.xlabel('Time')
plt.ylabel('Price (USD)')
plt.legend()
plt.grid(True)
plt.show()

# --- Plot 3: Candlestick Chart ---
fig = go.Figure(data=[go.Candlestick(
    x=df.index,
    open=df['open'],
    high=df['high'],
    low=df['low'],
    close=df['close']
)])
fig.update_layout(title='Candlestick Chart', xaxis_title='Time', yaxis_title='Price (USD)')
fig.show()

# --- Plot 4: Volume Line Chart ---
plt.figure(figsize=(12, 4))
plt.plot(df.index, df['volume'], label='Volume', color='purple')
plt.title('Volume Over Time')
plt.xlabel('Time')
plt.ylabel('Volume')
plt.legend()
plt.grid(True)
plt.show()

# --- Plot 5: Histogram of Close Price ---
plt.figure(figsize=(10, 5))
plt.hist(df['close'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Close Prices')
plt.xlabel('Close Price')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# --- Plot 6: Histogram of Volume ---
plt.figure(figsize=(10, 5))
plt.hist(df['volume'], bins=20, color='lightgreen', edgecolor='black')
plt.title('Histogram of Volumes')
plt.xlabel('Volume')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# --- Plot 7: Heatmap (Correlation Matrix) ---
plt.figure(figsize=(8, 6))
corr = df[['open', 'high', 'low', 'close', 'volume']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap')
plt.show()

# --- Plot 8: Boxplot for Close Price ---
plt.figure(figsize=(8, 6))
sns.boxplot(y=df['close'])
plt.title('Boxplot of Close Prices')
plt.ylabel('Close Price')
plt.show()

# --- Plot 9: Pairplot ---
sns.pairplot(df[['open', 'high', 'low', 'close', 'volume']])
plt.suptitle('Pairplot of OHLC and Volume', y=1.02)     