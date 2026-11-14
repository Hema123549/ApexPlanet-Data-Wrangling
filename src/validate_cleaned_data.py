import os
import pandas as pd

# ==========================================
# APEXPLANET - DATA VALIDATION
# ==========================================

INPUT_FILE = "data/processed/cleaned_dataset.csv"
REPORT_FILE = "outputs/data_quality_report.csv"


def validate_dataset():

    os.makedirs("outputs", exist_ok=True)

    # Load cleaned dataset
    df = pd.read_csv(INPUT_FILE)

    print("=" * 60)
    print("APEXPLANET CLEANED DATASET VALIDATION")
    print("=" * 60)

    # Convert date column
    df["Order_Date"] = pd.to_datetime(
        df["Order_Date"],
        errors="coerce"
    )

    # Expected columns
    expected_columns = [
        "Order_ID",
        "Order_Date",
        "Customer_ID",
        "Customer_Name",
        "Age",
        "Gender",
        "City",
        "Product",
        "Category",
        "Quantity",
        "Unit_Price",
        "Total_Sales",
        "Order_Year",
        "Order_Month",
        "Order_Month_Name",
        "Order_Quarter",
        "Age_Group"
    ]

    # Validation results
    results = []

    def add_result(check, status, details):
        results.append({
            "Validation_Check": check,
            "Status": status,
            "Details": details
        })

    # ------------------------------------------
    # 1. Row Count Validation
    # ------------------------------------------

    row_status = len(df) == 1000

    add_result(
        "Row Count",
        "PASS" if row_status else "FAIL",
        f"Total rows: {len(df)}"
    )

    # ------------------------------------------
    # 2. Column Count Validation
    # ------------------------------------------

    column_status = len(df.columns) == 17

    add_result(
        "Column Count",
        "PASS" if column_status else "FAIL",
        f"Total columns: {len(df.columns)}"
    )

    # ------------------------------------------
    # 3. Required Columns Validation
    # ------------------------------------------

    missing_columns = [
        col for col in expected_columns
        if col not in df.columns
    ]

    add_result(
        "Required Columns",
        "PASS" if not missing_columns else "FAIL",
        f"Missing columns: {missing_columns}"
    )

    # ------------------------------------------
    # 4. Missing Values Validation
    # ------------------------------------------

    missing_values = int(df.isnull().sum().sum())

    add_result(
        "Missing Values",
        "PASS" if missing_values == 0 else "FAIL",
        f"Total missing values: {missing_values}"
    )

    # ------------------------------------------
    # 5. Duplicate Records Validation
    # ------------------------------------------

    duplicates = int(df.duplicated().sum())

    add_result(
        "Duplicate Records",
        "PASS" if duplicates == 0 else "FAIL",
        f"Duplicate rows: {duplicates}"
    )

    # ------------------------------------------
    # 6. Date Validation
    # ------------------------------------------

    invalid_dates = int(df["Order_Date"].isnull().sum())

    add_result(
        "Date Validation",
        "PASS" if invalid_dates == 0 else "FAIL",
        f"Invalid dates: {invalid_dates}"
    )

    # ------------------------------------------
    # 7. Age Validation
    # ------------------------------------------

    invalid_age = int(
        ((df["Age"] < 18) | (df["Age"] > 65)).sum()
    )

    add_result(
        "Age Range Validation",
        "PASS" if invalid_age == 0 else "FAIL",
        f"Invalid age records: {invalid_age}"
    )

    # ------------------------------------------
    # 8. Sales Calculation Validation
    # ------------------------------------------

    expected_sales = df["Quantity"] * df["Unit_Price"]

    sales_mismatches = int(
        ((df["Total_Sales"] - expected_sales).abs() > 0.01).sum()
    )

    add_result(
        "Sales Calculation",
        "PASS" if sales_mismatches == 0 else "FAIL",
        f"Sales mismatches: {sales_mismatches}"
    )

    # ------------------------------------------
    # 9. Feature Engineering Validation
    # ------------------------------------------

    year_match = (
        df["Order_Year"] == df["Order_Date"].dt.year
    ).all()

    month_match = (
        df["Order_Month"] == df["Order_Date"].dt.month
    ).all()

    quarter_match = (
        df["Order_Quarter"] == df["Order_Date"].dt.quarter
    ).all()

    feature_status = (
        year_match and month_match and quarter_match
    )

    add_result(
        "Feature Engineering",
        "PASS" if feature_status else "FAIL",
        "Year, month and quarter values checked."
    )

    # ------------------------------------------
    # 10. Age Group Validation
    # ------------------------------------------

    age_group_missing = int(df["Age_Group"].isnull().sum())

    add_result(
        "Age Group Validation",
        "PASS" if age_group_missing == 0 else "FAIL",
        f"Missing age groups: {age_group_missing}"
    )

    # ------------------------------------------
    # 11. Repeated Order ID Investigation
    # ------------------------------------------

    repeated_order_ids = int(
        (df["Order_ID"].value_counts() > 1).sum()
    )

    add_result(
        "Repeated Order ID Investigation",
        "INFO",
        f"Repeated Order IDs: {repeated_order_ids}. "
        "Records are preserved."
    )

    # ------------------------------------------
    # 12. Save Validation Report
    # ------------------------------------------

    report = pd.DataFrame(results)

    report.to_csv(REPORT_FILE, index=False)

    # ------------------------------------------
    # 13. Display Validation Summary
    # ------------------------------------------

    print("\nVALIDATION RESULTS")
    print("-" * 60)

    print(report.to_string(index=False))

    passed = (report["Status"] == "PASS").sum()
    failed = (report["Status"] == "FAIL").sum()

    print("\n" + "=" * 60)
    print("VALIDATION SUMMARY")
    print("=" * 60)

    print("Passed Checks:", passed)
    print("Failed Checks:", failed)

    print("\nValidation Report Saved:")
    print(REPORT_FILE)

    if failed == 0:
        print("\nALL VALIDATION CHECKS PASSED!")
    else:
        print("\nVALIDATION ISSUES FOUND. Please investigate.")

    print("=" * 60)


if __name__ == "__main__":
    validate_dataset()