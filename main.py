import pandas as pd

from src.metrics import calculate_metrics


def main():
    """
    Main pipeline entry.
    load data → calculate metrics → save results
    """

    # Load event data
    df = pd.read_csv("data/events.csv")

    # Calculate daily analytics metrics
    result = calculate_metrics(df)

    # Preview results
    print("\n=== Daily Metrics Preview ===")
    print(result.head())

    # Save output
    result.to_csv("output/metrics.csv")

    print("\nSaved: output/metrics.csv")


if __name__ == "__main__":
    main()