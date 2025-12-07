# test_install.py
# Simple manual test to verify dependencies are installed

def main():
    try:
        import streamlit
        import pandas as pd
        import plotly.express as px

        print("✅ All required packages are installed and importable!")
        print(f"Streamlit version: {streamlit.__version__}")
        print(f"Pandas version: {pd.__version__}")
        print(f"Plotly version: {px.__version__}")

    except ImportError as e:
        print("❌ Missing package:", e)

if __name__ == "__main__":
    main()