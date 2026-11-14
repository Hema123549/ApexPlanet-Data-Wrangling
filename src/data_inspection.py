import pandas as pd
import os

# Dataset path
file_path = "data/raw/ApexPlanet_DataAnalytics_Dataset.xlsx"

# Load dataset
df = pd.read_excel(file_path)

print("=" * 50)
print("APEXPLANET DATA ANALYTICS - DATA INSPECTION")
print("=" * 50)

# Dataset shape
print("\n1. DATASET DIMENSIONS")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Column names
print("\n2. COLUMN NAMES")
print(df.columns.tolist())

# Dataset information
print("\n3. DATASET INFORMATION")
df.info()

# Missing values
print("\n4. MISSING VALUES")
print(df.isnull().sum())

# Duplicate records
print("\n5. DUPLICATE RECORDS")
print("Total Duplicates:", df.duplicated().sum())

# Statistical summary
print("\n6. STATISTICAL SUMMARY")
print(df.describe(include="all"))

# Unique values
print("\n7. UNIQUE VALUES")
print(df.nunique())

print("\n" + "=" * 50)
print("DATA INSPECTION COMPLETED")
print("=" * 50)