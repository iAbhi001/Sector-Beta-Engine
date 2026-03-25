import pandas as pd
import numpy as np
from src.analytics import run_regression

def test_beta_calculation():
    # Create dummy data where sector moves 2x yield
    data = pd.DataFrame({
        'yield_change': [0.01, 0.02, 0.03],
        'sector_return': [0.02, 0.04, 0.06]
    })
    results = run_regression(data)
    assert round(results['beta'], 1) == 2.0