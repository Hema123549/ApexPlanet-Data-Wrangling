# ApexPlanet – Data Immersion & Data Wrangling

## Project Overview

This project focuses on understanding, investigating, cleaning, and transforming a raw sales dataset as part of the ApexPlanet Data Analytics Internship.

The primary objective is to improve data quality, handle missing values, investigate inconsistencies, perform feature engineering, and prepare a structured dataset for further analysis.

## Objectives

- Understand the structure and characteristics of the dataset.
- Identify missing values and data quality issues.
- Investigate duplicate records and inconsistent identifiers.
- Clean and transform raw data.
- Perform feature engineering.
- Validate the cleaned dataset.
- Prepare an analysis-ready dataset.

## Dataset Information

- **Source:** ApexPlanet Data Analytics Internship Dataset
- **Original Format:** Excel (.xlsx)
- **Original Records:** 1,000
- **Original Columns:** 12
- **Cleaned Records:** 1,000
- **Final Columns:** 17

### Dataset Columns

| Column | Description |
|---|---|
| Order_ID | Order identifier |
| Order_Date | Date of transaction |
| Customer_ID | Customer identifier |
| Customer_Name | Customer name |
| Age | Customer age |
| Gender | Customer gender |
| City | Customer city |
| Product | Purchased product |
| Category | Product category |
| Quantity | Number of units purchased |
| Unit_Price | Price per unit |
| Total_Sales | Total transaction sales |

## Project Structure

```text
Task_1_Data_Wrangling/
│
├── data/
│   ├── raw/
│   │   └── ApexPlanet_DataAnalytics_Dataset.xlsx
│   │
│   └── processed/
│       └── cleaned_dataset.csv
│
├── documentation/
│   └── data_dictionary.csv
│
├── notebooks/
│
├── outputs/
│   └── data_quality_report.csv
│
├── src/
│   ├── data_inspection.py
│   ├── data_quality_assessment.py
│   ├── data_investigation.py
│   ├── data_cleaning.py
│   └── validate_cleaned_data.py
│
├── requirements.txt
└── README.md
```

## Data Quality Assessment

The initial dataset inspection identified the following issues:

| Data Quality Check | Findings |
|---|---:|
| Total Records | 1,000 |
| Total Columns | 12 |
| Missing Age Values | 20 |
| Missing City Values | 13 |
| Exact Duplicate Records | 0 |
| Repeated Order IDs | 1 |
| Customer ID and Name Mapping Inconsistencies | 52 |

### Important Observations

- One Order_ID appears nine times with different transaction details. These records were preserved rather than incorrectly deleted.
- Some Customer_ID values are associated with multiple customer names. These inconsistencies were documented and preserved for further investigation.
- No invalid sales calculations were identified.

## Data Cleaning and Transformation

The following operations were performed:

1. Removed unnecessary leading and trailing spaces from text columns.
2. Replaced missing Age values with the median age (41).
3. Replaced missing City values with "Unknown".
4. Converted Order_Date into datetime format.
5. Checked exact duplicate records without deleting valid transactions.
6. Verified Total_Sales using Quantity multiplied by Unit_Price.
7. Preserved repeated Order_ID records containing different transaction details.

## Feature Engineering

Five additional columns were created:

| New Column | Description |
|---|---|
| Order_Year | Year extracted from Order_Date |
| Order_Month | Month number extracted from Order_Date |
| Order_Month_Name | Month name extracted from Order_Date |
| Order_Quarter | Quarter extracted from Order_Date |
| Age_Group | Customer age categorized into groups |

### Age Groups

- 18–25
- 26–35
- 36–45
- 46–55
- 56–65

## Validation Results

The cleaned dataset was validated using a separate Python script.

| Validation Check | Result |
|---|---|
| Row Count | PASS |
| Column Count | PASS |
| Required Columns | PASS |
| Missing Values | PASS |
| Duplicate Records | PASS |
| Date Validation | PASS |
| Age Range Validation | PASS |
| Sales Calculation | PASS |
| Feature Engineering | PASS |
| Age Group Validation | PASS |

**Final Validation Summary:**
- Passed Checks: 10
- Failed Checks: 0
- Total Records: 1,000
- Total Columns: 17

## Technologies Used

- Python
- Pandas
- NumPy
- OpenPyXL
- Matplotlib
- Seaborn
- Visual Studio Code

## Installation and Execution

### 1. Clone the Repository

```bash
git clone <your-repository-url>
```

### 2. Navigate to the Project Folder

```bash
cd Task_1_Data_Wrangling
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run Data Inspection

```bash
python src/data_inspection.py
```

### 7. Run Data Quality Assessment

```bash
python src/data_quality_assessment.py
```

### 8. Run Data Investigation

```bash
python src/data_investigation.py
```

### 9. Run Data Cleaning

```bash
python src/data_cleaning.py
```

### 10. Run Dataset Validation

```bash
python src/validate_cleaned_data.py
```

## Project Deliverables

- Data dictionary
- Data inspection script
- Data quality assessment script
- Data investigation script
- Data cleaning script
- Cleaned dataset
- Data validation script
- Data quality validation report

## Conclusion

The raw sales dataset was successfully inspected, investigated, cleaned, and transformed.

Missing values were handled, date information was converted into a suitable format, and five additional analytical features were created.

The final dataset contains 1,000 records and 17 columns, with all 10 validation checks passing.

This analysis-ready dataset can be used for further Exploratory Data Analysis (EDA), business intelligence, and dashboard development as part of the subsequent internship tasks.

---

**Project:** ApexPlanet Data Analytics Internship – Task 1  
**Task:** Data Immersion & Wrangling  
**Status:** Completed