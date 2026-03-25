# Sector Beta Engine: Macro-Equity Sensitivity Tracker

An algorithmic tool designed to measure the sensitivity of different stock sectors to changes in the 10-Year Treasury Yield. This project demonstrates a full data pipeline from ingestion (FRED/Yahoo Finance) to statistical analysis and interactive visualization.

## 🚀 Features
- **Automated Data Pipeline:** Real-time fetching and time-series alignment of macroeconomic and equity data.
- **Statistical Analysis:** Calculates OLS Regression Beta, R-Squared, and P-values to determine the significance of interest rate impacts.
- **Dynamic Sensitivity:** 60-day rolling beta visualization to track how market regimes shift over time.
- **Interactive Dashboard:** Built with Streamlit and Plotly for deep-dive sector exploration.

## 🛠️ Tech Stack
- **Language:** Python 3.11+
- **Data:** FRED API, Yahoo Finance (yfinance)
- **Math/DS:** Pandas, NumPy, Statsmodels, Scikit-learn
- **UI:** Streamlit, Plotly
- **Testing:** Pytest

## 📊 The Math
This engine calculates the **Interest Rate Beta ($\beta$)** using the following regression model:
$$\Delta \text{Sector Price} = \alpha + \beta (\Delta \text{10Y Yield}) + \epsilon$$

## ⚙️ Setup
1. Clone the repo: `git clone https://github.com/iAbhi001/Sector-Beta-Engine.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Add your FRED API key to a `.env` file: `FRED_API_KEY=your_key_here`
4. Run the dashboard: `streamlit run src/dashboard.py`