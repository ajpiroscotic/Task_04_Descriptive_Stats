import polars as pl

if __name__ == "__main__":
    file_path = "Stores.csv"
    df = pl.read_csv(file_path)

    # Overall descriptive stats
    print("Overall Stats:")
    print(df.describe())

    # Grouped by Store ID
    print("\nGrouped by Store ID:")
    print(df.group_by("Store ID ").agg([
        pl.col("Store_Area").mean(),
        pl.col("Store_Area").min(),
        pl.col("Store_Area").max(),
        pl.col("Store_Area").std(),
        pl.col("Items_Available").mean(),
        pl.col("Daily_Customer_Count").mean(),
        pl.col("Store_Sales").mean()
    ]).head())
