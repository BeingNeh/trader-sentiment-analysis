import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Ensure output directory exists
output_dir = '/home/ubuntu/output'
os.makedirs(output_dir, exist_ok=True)

print("Starting data loading and preprocessing...")

# Load datasets
fg_df = pd.read_csv('/home/ubuntu/Downloads/fear_greed_index.csv')
trader_df = pd.read_csv('/home/ubuntu/Downloads/historical_data.csv')

# --- Part A: Data preparation ---
fg_df['date'] = pd.to_datetime(fg_df['date'])
trader_df['datetime'] = pd.to_datetime(trader_df['Timestamp IST'], format='%d-%m-%Y %H:%M', errors='coerce')
trader_df['date'] = trader_df['datetime'].dt.date
trader_df['date'] = pd.to_datetime(trader_df['date'])

merged_df = pd.merge(trader_df, fg_df[['date', 'value', 'classification']], on='date', how='inner')

def simplify_sentiment(c):
    if 'Fear' in c: return 'Fear'
    if 'Greed' in c: return 'Greed'
    return 'Neutral'
merged_df['sentiment_simple'] = merged_df['classification'].apply(simplify_sentiment)

# --- Part B: Core Analysis ---
# Performance and Behavior by Sentiment
perf_by_sentiment = merged_df.groupby('sentiment_simple')['Closed PnL'].agg(['mean', 'std']).reset_index()
def calc_win_rate(x):
    trades = x[x != 0]
    return (trades > 0).sum() / len(trades) if len(trades) > 0 else 0
win_rates_by_sentiment = merged_df.groupby('sentiment_simple')['Closed PnL'].apply(calc_win_rate).reset_index(name='win_rate')
avg_trade_size_sentiment = merged_df.groupby('sentiment_simple')['Size USD'].mean().reset_index()

# --- Bonus: Clustering Traders into Behavioral Archetypes ---
print("\nPerforming Bonus Task: Trader Clustering...")

# Aggregate features per trader for clustering
trader_features = merged_df.groupby('Account').agg({
    'Closed PnL': ['sum', 'mean'],
    'Size USD': 'mean',
    'Account': 'count',
    'Side': lambda x: (x == 'BUY').sum() / len(x)
})
trader_features.columns = ['total_pnl', 'avg_pnl', 'avg_size', 'trade_count', 'long_ratio']
trader_features = trader_features.reset_index()

# Normalize features for clustering
scaler = StandardScaler()
features_to_scale = ['total_pnl', 'avg_size', 'trade_count', 'long_ratio']
scaled_features = scaler.fit_transform(trader_features[features_to_scale])

# Apply K-Means Clustering (3 clusters for archetypes)
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
trader_features['cluster'] = kmeans.fit_predict(scaled_features)

# Map clusters to human-readable archetypes based on their characteristics
cluster_summary = trader_features.groupby('cluster').mean(numeric_only=True)

def map_archetype(row):
    # This is a simplified mapping logic based on typical cluster results
    if row['avg_size'] > cluster_summary['avg_size'].mean() and row['total_pnl'] > 0:
        return "Whale Winners"
    elif row['trade_count'] > cluster_summary['trade_count'].mean():
        return "High-Frequency Scalpers"
    else:
        return "Selective Retail"

trader_features['archetype'] = trader_features.apply(map_archetype, axis=1)
trader_features.to_csv(os.path.join(output_dir, 'trader_archetypes.csv'), index=False)

# --- Visualizations ---
print("Generating visualizations...")
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# 1. Win Rate by Sentiment
sns.barplot(ax=axes[0, 0], data=win_rates_by_sentiment, x='sentiment_simple', y='win_rate', palette='viridis')
axes[0, 0].set_title('Win Rate by Market Sentiment')
axes[0, 0].set_ylim(0.8, 0.9)

# 2. Mean PnL per Trade by Sentiment
sns.barplot(ax=axes[0, 1], data=perf_by_sentiment, x='sentiment_simple', y='mean', palette='magma')
axes[0, 1].set_title('Mean PnL per Trade by Market Sentiment')

# 3. Average Trade Size by Sentiment
sns.barplot(ax=axes[1, 0], data=avg_trade_size_sentiment, x='sentiment_simple', y='Size USD', palette='rocket')
axes[1, 0].set_title('Average Trade Size by Market Sentiment')

# 4. Trader Archetypes Distribution
sns.countplot(ax=axes[1, 1], data=trader_features, x='archetype', palette='mako')
axes[1, 1].set_title('Distribution of Trader Archetypes (Bonus)')
plt.xticks(rotation=15)

plt.tight_layout()
plt.savefig(os.path.join(output_dir, 'final_analysis_charts.png'))

print(f"Analysis complete. Files saved in {output_dir}")
