# portfolio_tracker.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def fetch_prices(symbols):
    data = {}
    for s in symbols:
        data[s] = 100 * (1 + pd.Series(range(30)).pct_change().fillna(0)).cumprod()
    return pd.DataFrame(data)

if __name__ == "__main__":
    print("[INFO] Running portfolio_tracker.py …")
    df = fetch_prices(["AAPL","MSFT","NVDA"])
    print("[INFO] Latest rows:\n", df.tail())

    ax = df.plot(title="Portfolio Tracker — Example Output")
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig("portfolio_tracker.png", dpi=200, bbox_inches="tight")
    print("[INFO] Saved chart -> portfolio_tracker.png")
    