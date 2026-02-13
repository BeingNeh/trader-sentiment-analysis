# Data Science/Analytics Intern – Round-0 Assignment (Trader Performance vs Market Sentiment)

## Objective

This assignment analyzes how market sentiment (Fear/Greed) relates to trader behavior and performance on Hyperliquid, uncovering patterns that could inform smarter trading strategies.

## Datasets

1.  **Bitcoin Market Sentiment (Fear/Greed)**: Daily sentiment classifications.
2.  **Historical Trader Data (Hyperliquid)**: Detailed trade execution data.

## Methodology

### Part A — Data Preparation
*   **Alignment**: Merged datasets by date to sync market "mood" with specific trades.
*   **Metrics**: Calculated Daily PnL, Win Rates, and Average Trade Sizes per account.

### Part B — Analysis
*   **Sentiment Impact**: Evaluated how PnL and Win Rates fluctuate between Fear and Greed regimes.
*   **Behavioral Shifts**: Analyzed changes in trading frequency and long/short bias.

### Bonus — Behavioral Clustering (Archetypes)
Using K-Means clustering, I identified three distinct trader archetypes based on their trading volume, capital deployment, and profitability:
1.  **Whale Winners**: High-capital traders with significant positive PnL.
2.  **High-Frequency Scalpers**: Traders with extremely high trade counts, often sensitive to sentiment shifts.
3.  **Selective Retail**: Lower-frequency traders with varied performance.

## Key Insights

### 1. Performance Differences
| Sentiment | Mean PnL per Trade | Win Rate |
|:----------|:-------------------|:---------|
| Fear      | 49.21              | 0.844    |
| Greed     | 53.88              | 0.825    |

*   **Insight**: Traders are slightly more profitable on average during Greed days, but win rates are remarkably stable across all sentiments, suggesting that the "best" traders maintain their edge regardless of market mood.

### 2. Behavioral Shifts
*   **Insight**: Trading frequency **drops by ~60%** during Greed days compared to Fear days. This suggests that the "smart money" may be de-risking or becoming more selective when the market is euphoric.

### 3. Archetype Performance (Bonus)
*   **Insight**: **High-Frequency Scalpers** are the most vulnerable during Greed days if they are in the "Loser" segment, showing significant negative PnL. Conversely, **Whale Winners** tend to maximize their gains during these periods.

## Strategy Recommendations

1.  **The "Greed Filter"**: High-frequency traders should implement a "Greed Filter"—reducing trade frequency and leverage when the index crosses into Greed territory to avoid the high-volatility reversals that typically hurt this segment.
2.  **Selective Scaling**: Retail traders should look to the "Whale" behavior: increasing trade size during Fear days (where average sizes are higher) to capitalize on "blood in the streets" opportunities.

## Setup and How to Run

1.  Place `fear_greed_index.csv` and `historical_data.csv` in the same directory as the script.
2.  Install dependencies: `pip install pandas numpy matplotlib seaborn scikit-learn`
3.  Run the script: `python3 submission_script_v2.py`

## Deliverables Included
*   `submission_script_v2.py`: Full analysis code including clustering.
*   `final_analysis_charts.png`: Visual summary of findings.
*   `trader_archetypes.csv`: List of traders mapped to their behavioral archetypes.
*   `segment_sentiment_pnl.csv`: Detailed performance breakdown.

For a more detailed breakdown of our strategic findings, please see insights_and_recommendations.md.