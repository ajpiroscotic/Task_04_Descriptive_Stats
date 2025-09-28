import pandas as pd

if __name__ == "__main__":
    file_path = ""C:\Users\Anjaneya Padwal\Downloads\coffe.csv""
    df = pd.read_csv(file_path)

    # Overall descriptive stats
    print("Overall Stats:")
    print(df.describe(include='all'))

    # Grouped by coffee_name
    print("\nGrouped by coffee_name:")
    print(df.groupby("coffee_name").describe().head())

    # Frequency counts for categorical fields
    print("\nMost popular coffee types:")
    print(df['coffee_name'].value_counts().head())

    print("\nCash type distribution:")
    print(df['cash_type'].value_counts())
