import os
import pandas as pd
import numpy as np

# ======================================================
# Resolve project root path
# ======================================================

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

# Auto-create data folder
os.makedirs(DATA_DIR, exist_ok=True)


def make_events():
    """
    Generate synthetic user behavior events.
    """

    np.random.seed(7)

    n_users = 200
    n_rows = 3000

    user_ids = np.random.randint(1, n_users, n_rows)

    actions = np.random.choice(
        ["view", "add_to_cart", "purchase", "search"],
        size=n_rows,
        p=[0.6, 0.2, 0.1, 0.1]
    )

    timestamps = pd.date_range(
        "2025-01-01",
        periods=n_rows,
        freq="min"
    )

    df = pd.DataFrame({
        "user_id": user_ids,
        "timestamp": timestamps,
        "action": actions
    })

    # Save CSV into project data folder
    output_path = os.path.join(DATA_DIR, "events.csv")
    df.to_csv(output_path, index=False)

    print(f"Created: {output_path}")
    print("Rows:", len(df))


if __name__ == "__main__":
    make_events()