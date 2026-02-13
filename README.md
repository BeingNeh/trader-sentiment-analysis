# Data Science/Analytics Intern – Round-0 Assignment  
## Trader Performance vs Market Sentiment (Fear/Greed)

## Objective
This project analyzes how Bitcoin market sentiment (Fear/Greed Index) influences trader behavior and profitability on Hyperliquid.  
The goal is to uncover actionable patterns that can inform smarter trading and risk strategies.

---

## Datasets

1. **Bitcoin Market Sentiment Dataset (Fear/Greed Index)**  
   - Daily sentiment classification (Fear, Greed, Neutral)  
   - Numerical sentiment score  

2. **Hyperliquid Historical Trader Dataset**  
   - Trade-level execution data including:  
     Account, Symbol, Side, Size, Price, Timestamp, Leverage, Closed PnL  

---

## Methodology

### Part A — Data Preparation
- Converted timestamps into daily format for alignment  
- Merged both datasets by date to map sentiment → trading activity  
- Simplified sentiment labels into:
  - Fear  
  - Greed  
  - Neutral  

### Key Metrics Computed
- **Daily PnL per trader**
- **Win Rate per trader**
- **Average Trade Size**
- **Long vs Short Bias**
- **Trader Segmentation**
  - Frequent vs Infrequent (median trade count split)
  - Winner vs Loser (total PnL split)

---

## Analysis & Results

### 1. Performance Differences Across Sentiment

| Sentiment | Mean PnL per Trade | Win Rate |
|----------|-------------------|----------|
| Fear     | 49.21             | 0.844    |
| Greed    | 53.88             | 0.825    |
| Neutral  | 34.31             | 0.824    |

**Insights**
- Traders achieve slightly higher average profitability during **Greed** periods.
- Win rates remain consistently high (~82–84%), suggesting strong traders maintain an edge regardless of sentiment.

---

### 2. Behavioral Shifts Under Sentiment Regimes

| Sentiment | Avg Daily Trades | Long Ratio |
|----------|------------------|-----------|
| Fear     | 792.73           | 0.495     |
| Greed    | 294.12           | 0.471     |
| Neutral  | 562.48           | 0.503     |

**Insights**
- Trading activity drops sharply (~60%) during Greed days, suggesting traders become more selective in euphoric markets.
- Greed periods show a slight increase in short bias.
- Trade sizes are largest during Fear days, consistent with “buying the dip” behavior.

---

### 3. Segment-Level Performance

| Activity Segment | Profitability Segment | Fear PnL | Greed PnL | Neutral PnL |
|-----------------|----------------------|---------|----------|------------|
| Frequent        | Loser                | 46.14   | -207.95  | 18.49      |
| Frequent        | Winner               | 47.41   | 48.80    | 35.35      |
| Infrequent      | Loser                | -110.66 | 104.41   | -37.24     |
| Infrequent      | Winner               | 70.75   | 157.32   | 32.46      |

**Key Observations**
- Frequent Losers collapse during Greed regimes, likely due to overtrading and leverage misuse.
- Infrequent Winners perform best during Greed, suggesting selective entry into strong momentum environments.

---

## Bonus — Behavioral Clustering (Trader Archetypes)

Using K-Means clustering, traders were grouped into three behavioral archetypes:

1. **Whale Winners**
   - High capital deployment
   - Strong positive PnL

2. **High-Frequency Scalpers**
   - Extremely high trade count
   - Most sentiment-sensitive group

3. **Selective Retail Traders**
   - Lower frequency participation
   - Mixed performance outcomes

---

## Strategy Recommendations

### Strategy 1 — The “Greed Filter” for High-Frequency Traders
- During Greed regimes, frequent traders (especially losers) should reduce leverage and trade frequency.
- Prevents large drawdowns during euphoric volatility reversals.

### Strategy 2 — Opportunistic Scaling for Selective Winners
- Infrequent winners should prioritize Greed periods for trend continuation setups.
- Larger opportunities emerge when optimism fuels momentum.

---

## Setup & How to Run

1. Place both datasets in the project folder:
   - `fear_greed_index.csv`
   - `historical_data.csv`

2. Install dependencies:
```bash
pip install pandas numpy matplotlib scikit-learn

For a more detailed breakdown of my strategic findings, please see "insights_and_recommendations.md" .