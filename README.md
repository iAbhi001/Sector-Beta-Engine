
---

# **Sector Beta Engine: Macro-Equity Sensitivity Tracker**

The **Sector Beta Engine** is an end-to-end quantitative analytics platform designed to measure and monitor how different equity sectors respond to changes in macroeconomic conditions—specifically movements in the U.S. 10-Year Treasury Yield. This project bridges macroeconomics and equity market behavior through a fully automated data pipeline, statistical modeling, and interactive visualization.

At its core, the system helps answer a fundamental question in financial markets: *Which sectors are most sensitive to interest rate changes, and how does that sensitivity evolve over time?*

---

## 🚀 **Key Features**

### **1. Automated Data Pipeline**

The engine integrates multiple data sources to ensure reliable and up-to-date analysis:

* Pulls macroeconomic data (10-Year Treasury Yield) from the **FRED API**
* Fetches sector-level equity price data via **Yahoo Finance (yfinance)**
* Aligns and cleans time-series data, handling missing values and frequency mismatches
* Automates preprocessing steps to produce analysis-ready datasets

This pipeline ensures consistency and reproducibility across all analyses.

---

### **2. Statistical Modeling & Inference**

The platform uses **Ordinary Least Squares (OLS) regression** to quantify the relationship between interest rate changes and sector returns. For each sector, it computes:

* **Beta (β):** Measures sensitivity to changes in yields
* **Alpha (α):** Baseline return independent of yield changes
* **R-squared:** Explains how much of the variation is driven by rates
* **P-values:** Tests statistical significance of the relationship

This allows users to distinguish between meaningful macro-driven effects and random noise.

---

### **3. Dynamic Sensitivity Analysis**

Market relationships are not static. To capture evolving dynamics, the engine includes:

* **Rolling 60-day regression windows**
* Time-varying beta estimates for each sector
* Visualization of regime shifts (e.g., tightening cycles, recessions, risk-on/risk-off periods)

This feature is particularly useful for identifying structural changes in market behavior.

---

### **4. Interactive Dashboard**

The analytics are delivered through a user-friendly interface built with:

* **Streamlit** for rapid web app deployment
* **Plotly** for rich, interactive visualizations

Users can:

* Explore sector sensitivities in real time
* Compare beta trends across sectors
* Drill down into specific time periods
* Visually assess statistical relationships

---

## 🛠️ **Technology Stack**

* **Programming Language:** Python 3.11+
* **Data Sources:** FRED API, Yahoo Finance (yfinance)
* **Data Processing:** Pandas, NumPy
* **Statistical Modeling:** Statsmodels, Scikit-learn
* **Visualization & UI:** Streamlit, Plotly
* **Testing Framework:** Pytest

---

## 📊 **Mathematical Framework**

The engine models the relationship between sector returns and interest rate movements using the following regression equation:

[
\Delta \text{Sector Price} = \alpha + \beta \cdot (\Delta \text{10Y Yield}) + \epsilon
]

Where:

* **Δ Sector Price** represents daily (or periodic) sector returns
* **Δ 10Y Yield** represents changes in the 10-Year Treasury Yield
* **β (Beta)** captures sensitivity to interest rate movements
* **α (Alpha)** represents baseline return
* **ε (Error term)** captures unexplained variation

A positive beta indicates that a sector tends to rise with increasing yields, while a negative beta suggests inverse sensitivity.

---

## ⚙️ **Setup Instructions**

To run the project locally:

1. **Clone the repository**

   ```bash
   git clone https://github.com/iAbhi001/Sector-Beta-Engine.git
   cd Sector-Beta-Engine
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API access**
   Create a `.env` file in the root directory and add:

   ```env
   FRED_API_KEY=your_key_here
   ```

4. **Launch the dashboard**

   ```bash
   streamlit run src/dashboard.py
   ```

---

## 💡 **Use Cases**

* Macro hedge fund strategy research
* Sector rotation analysis
* Interest rate risk assessment
* Academic and financial data science projects
* Portfolio sensitivity diagnostics

---

