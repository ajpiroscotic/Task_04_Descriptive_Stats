import pandas as pd

if __name__ == "__main__":
    file_path = "Stores.csv"
    df = pd.read_csv(file_path)

    # Overall descriptive stats
    print("Overall Stats:")
    print(df.describe())

    # Grouped by Store ID
    print("\nGrouped by Store ID:")
    print(df.groupby("Store ID ").describe().head())
