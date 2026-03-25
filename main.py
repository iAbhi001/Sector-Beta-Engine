import os
from src.dashboard import run_app

if __name__ == "__main__":
    # This simply launches the streamlit dashboard
    os.system("streamlit run src/dashboard.py")