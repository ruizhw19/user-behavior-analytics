import pandas as pd


def calculate_metrics(df):
    """
    Calculate daily product analytics metrics.

    Parameters
    ----------
    df : pd.DataFrame
        Event-level user behavior data.

    Returns
    -------
    pd.DataFrame
        Daily metrics table.
    """

    # Convert timestamp to date
    df["date"] = pd.to_datetime(df["timestamp"]).dt.date

    # DAU = Daily Active Users
    dau = df.groupby("date")["user_id"].nunique()

    # Filter purchase events
    purchases = df[df["action"] == "purchase"]

    # Number of users who purchased each day
    purchasers = purchases.groupby("date")["user_id"].nunique()

    # Simplified revenue calculation
    revenue = purchases.groupby("date").size() * 20

    # Combine metrics into one table
    result = pd.DataFrame({
        "DAU": dau,
        "Purchasers": purchasers,
        "Revenue": revenue
    }).fillna(0)

    # Conversion rate = purchasers / DAU
    result["ConversionRate"] = result["Purchasers"] / result["DAU"]

    return result