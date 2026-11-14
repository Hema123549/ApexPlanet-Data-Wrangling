import pandas as pd

# Load dataset
df = pd.read_excel(
    "data/raw/ApexPlanet_DataAnalytics_Dataset.xlsx"
)

print("=" * 60)
print("DATA QUALITY ASSESSMENT")
print("=" * 60)

# 1. Missing value percentage
print("\n1. MISSING VALUE PERCENTAGE")

missing = pd.DataFrame({
    "Missing_Count": df.isnull().sum(),
    "Missing_Percentage": df.isnull().mean() * 100
})

print(missing[missing["Missing_Count"] > 0])

# 2. Repeated Order IDs
print("\n2. REPEATED ORDER IDs")

repeated_orders = df[
    df["Order_ID"].duplicated(keep=False)
].sort_values("Order_ID")

print(repeated_orders)

# 3. Customer ID and Name relationship
print("\n3. CUSTOMER ID-NAME MAPPING")

customer_mapping = df.groupby(
    "Customer_ID"
)["Customer_Name"].nunique()

print("Customer IDs with multiple names:",
      (customer_mapping > 1).sum())

# 4. Invalid numerical values
print("\n4. NUMERICAL VALUE VALIDATION")

print("Invalid Age:",
      ((df["Age"] < 0) | (df["Age"] > 100)).sum())

print("Invalid Quantity:",
      (df["Quantity"] <= 0).sum())

print("Invalid Unit Price:",
      (df["Unit_Price"] <= 0).sum())

print("Invalid Total Sales:",
      (df["Total_Sales"] <= 0).sum())

# 5. Sales calculation validation
print("\n5. SALES CALCULATION VALIDATION")

expected_sales = df["Quantity"] * df["Unit_Price"]

sales_mismatch = (
    (df["Total_Sales"] - expected_sales).abs() > 0.01
)

print("Sales mismatches:", sales_mismatch.sum())

# 6. Date validation
print("\n6. DATE VALIDATION")

dates = pd.to_datetime(
    df["Order_Date"], errors="coerce"
)

print("Invalid dates:", dates.isna().sum())
print("Earliest date:", dates.min())
print("Latest date:", dates.max())

print("\n" + "=" * 60)
print("ASSESSMENT COMPLETED")
print("=" * 60)