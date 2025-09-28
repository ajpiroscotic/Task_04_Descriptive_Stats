import polars as pl

if __name__ == "__main__":
    file_path = "C:\Users\Anjaneya Padwal\Downloads\coffe.csv"
    df = pl.read_csv(file_path)

    # Overall descriptive stats
    print("Overall Stats:")
    print(df.describe())

    # Grouped by coffee_name
    print("\nGrouped by coffee_name:")
    print(df.group_by("coffee_name").agg([
        pl.count(),
        pl.col("money").mean(),
        pl.col("money").min(),
        pl.col("money").max(),
        pl.col("money").std()
    ]).head())

    # Frequency counts
    print("\nMost popular coffee types:")
    print(df["coffee_name"].value_counts().head())

    print("\nCash type distribution:")
    print(df["cash_type"].value_counts())
