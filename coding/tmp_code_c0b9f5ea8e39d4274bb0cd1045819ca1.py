import yfinance as yf
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime

# Fetch the data
btc = yf.download('BTC-USD', start='2024-01-01', end='2024-11-19')
eth = yf.download('ETH-USD', start='2024-01-01', end='2024-11-19')
sol = yf.download('SOL-USD', start='2024-01-01', end='2024-11-19')

# Calculate the gains
btc['Gain'] = btc['Close'].pct_change()
eth['Gain'] = eth['Close'].pct_change()
sol['Gain'] = sol['Close'].pct_change()

# Create a DataFrame
data = pd.DataFrame({'BTC': btc['Gain'], 'ETH': eth['Gain'], 'SOL': sol['Gain']})

# Create a correlation matrix
corr_matrix = data.corr()

# Set the style to dark
sns.set_style('dark')

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')

# Save the figure
plt.savefig('ytd_stock_gains.png')

# Show the plot
plt.show()