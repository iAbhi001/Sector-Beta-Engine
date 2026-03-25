import statsmodels.api as sm
import pandas as pd

def run_regression(df):
    """Calculates the static Beta and R-Squared."""
    y = df['sector_return']
    X = sm.add_constant(df['yield_change'])
    model = sm.OLS(y, X).fit()
    
    return {
        "beta": model.params['yield_change'],
        "r_squared": model.rsquared,
        "p_value": model.pvalues['yield_change'],
        "model": model
    }

def calculate_rolling_beta(df, window=60):
    """Calculates Beta over a moving window to show changing sensitivity."""
    rolling_cov = df['sector_return'].rolling(window).cov(df['yield_change'])
    rolling_var = df['yield_change'].rolling(window).var()
    return (rolling_cov / rolling_var).dropna()