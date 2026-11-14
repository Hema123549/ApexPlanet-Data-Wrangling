import pandas as pd

df = pd.read_excel(
    "data/raw/ApexPlanet_DataAnalytics_Dataset.xlsx"
)

print("=" * 60)
print("CUSTOMER DATA INVESTIGATION")
print("=" * 60)

# 1. Customer IDs with multiple names

customer_mapping = (
    df.groupby("Customer_ID")["Customer_Name"]
    .nunique()
)

inconsistent_customers = customer_mapping[
    customer_mapping > 1
]

print("\n1. CUSTOMER ID-NAME INCONSISTENCIES")

print("Total inconsistent Customer IDs:",
      len(inconsistent_customers))

# Display sample records

print("\nSample inconsistent customer records:")

sample_ids = inconsistent_customers.index[:10]

print(
    df[df["Customer_ID"].isin(sample_ids)]
    [["Customer_ID", "Customer_Name"]]
    .sort_values("Customer_ID")
    .to_string(index=False)
)

# 2. Order ID investigation

print("\n2. ORDER ID INVESTIGATION")

order_counts = df["Order_ID"].value_counts()

repeated_ids = order_counts[order_counts > 1]

print("Repeated Order IDs:", len(repeated_ids))

print("\nRepeated IDs and their frequencies:")

print(repeated_ids)

# 3. Customer name uniqueness

print("\n3. CUSTOMER NAME ANALYSIS")

print("Unique Customer Names:",
      df["Customer_Name"].nunique())

print("Unique Customer IDs:",
      df["Customer_ID"].nunique())

# 4. Category distribution

print("\n4. CATEGORY DISTRIBUTION")

print(df["Category"].value_counts())

# 5. Product distribution

print("\n5. PRODUCT DISTRIBUTION")

print(df["Product"].value_counts())

print("\n" + "=" * 60)
print("INVESTIGATION COMPLETED")
print("=" * 60)