import streamlit as st
import plotly.express as px
from data_loader import DataLoader
from analytics import run_regression, calculate_rolling_beta

def run_app():
    st.set_page_config(page_title="Macro Sector Beta", layout="wide")
    st.title("📈 Sector Sensitivity to Interest Rates")
    
    ticker = st.sidebar.selectbox("Select Sector ETF", ["XLK", "XLF", "XLU", "XLE", "XLV"])
    
    loader = DataLoader()
    with st.spinner('Fetching Data...'):
        data = loader.fetch_data(ticker)
    
    # Metrics
    stats = run_regression(data)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Interest Rate Beta", f"{stats['beta']:.4f}")
    col2.metric("R-Squared (Reliability)", f"{stats['r_squared']:.4f}")
    col3.metric("P-Value", f"{stats['p_value']:.4f}")

    # Plot 1: Scatter with Regression Line
    st.subheader(f"Regression: {ticker} Returns vs. 10Y Yield Changes")
    fig_scatter = px.scatter(data, x="yield_change", y="sector_return", trendline="ols",
                             labels={"yield_change": "Δ 10Y Yield", "sector_return": "Sector % Return"})
    st.plotly_chart(fig_scatter, use_container_width=True)

    # Plot 2: Rolling Beta
    st.subheader("60-Day Rolling Beta (Time-Series Sensitivity)")
    roll_beta = calculate_rolling_beta(data)
    st.line_chart(roll_beta)

if __name__ == "__main__":
    run_app()