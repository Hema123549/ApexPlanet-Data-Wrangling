import os
import pandas as pd

# ==========================================
# APEXPLANET - DATA CLEANING
# ==========================================

INPUT_FILE = "data/raw/ApexPlanet_DataAnalytics_Dataset.xlsx"
OUTPUT_FILE = "data/processed/cleaned_dataset.csv"


def clean_dataset():

    # Create required directories
    os.makedirs("data/processed", exist_ok=True)
    os.makedirs("outputs", exist_ok=True)

    # Load dataset
    df = pd.read_excel(INPUT_FILE)

    print("=" * 60)
    print("APEXPLANET DATA CLEANING PROCESS")
    print("=" * 60)

    print("\nOriginal Dataset Shape:", df.shape)

    # ------------------------------------------
    # 1. Remove Unnecessary Spaces
    # ------------------------------------------

    text_columns = df.select_dtypes(include="object").columns

    for column in text_columns:
        df[column] = df[column].str.strip()

    print("\nUnnecessary spaces removed.")

    # ------------------------------------------
    # 2. Handle Missing Age Values
    # ------------------------------------------

    age_median = df["Age"].median()

    missing_age = df["Age"].isnull().sum()

    df["Age"] = df["Age"].fillna(age_median)

    print("Missing Age Values Filled:", missing_age)
    print("Age Median Used:", age_median)

    # ------------------------------------------
    # 3. Handle Missing City Values
    # ------------------------------------------

    missing_city = df["City"].isnull().sum()

    df["City"] = df["City"].fillna("Unknown")

    print("Missing City Values Replaced:", missing_city)

    # ------------------------------------------
    # 4. Convert Date Column
    # ------------------------------------------

    df["Order_Date"] = pd.to_datetime(
        df["Order_Date"],
        errors="coerce"
    )

    invalid_dates = df["Order_Date"].isnull().sum()

    print("Invalid or Missing Dates:", invalid_dates)

    # ------------------------------------------
    # 5. Feature Engineering
    # ------------------------------------------

    df["Order_Year"] = df["Order_Date"].dt.year

    df["Order_Month"] = df["Order_Date"].dt.month

    df["Order_Month_Name"] = (
        df["Order_Date"].dt.month_name()
    )

    df["Order_Quarter"] = df["Order_Date"].dt.quarter

    df["Age_Group"] = pd.cut(
        df["Age"],
        bins=[17, 25, 35, 45, 55, 65],
        labels=[
            "18-25",
            "26-35",
            "36-45",
            "46-55",
            "56-65"
        ]
    )

    print("\nFeature Engineering Completed.")

    # ------------------------------------------
    # 6. Duplicate Validation
    # ------------------------------------------

    duplicate_count = df.duplicated().sum()

    print("\nExact Duplicate Records:", duplicate_count)

    # Repeated Order_ID values are preserved.
    # They represent different transaction records.

    # ------------------------------------------
    # 7. Sales Validation
    # ------------------------------------------

    expected_sales = df["Quantity"] * df["Unit_Price"]

    sales_mismatch = (
        (df["Total_Sales"] - expected_sales).abs() > 0.01
    )

    print(
        "Sales Calculation Mismatches:",
        sales_mismatch.sum()
    )

    # ------------------------------------------
    # 8. Save Cleaned Dataset
    # ------------------------------------------

    df.to_csv(OUTPUT_FILE, index=False)

    # ------------------------------------------
    # 9. Final Cleaning Summary
    # ------------------------------------------

    print("\n" + "=" * 60)
    print("FINAL CLEANING SUMMARY")
    print("=" * 60)

    print("\nTotal Rows:", len(df))
    print("Total Columns:", len(df.columns))

    print("\nRemaining Missing Values:")
    print(df.isnull().sum())

    print("\nCleaned Dataset Saved Successfully:")
    print(OUTPUT_FILE)

    print("\n" + "=" * 60)
    print("DATA CLEANING COMPLETED SUCCESSFULLY")
    print("=" * 60)


if __name__ == "__main__":
    clean_dataset()