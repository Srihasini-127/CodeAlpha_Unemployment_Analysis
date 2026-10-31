
# ============================================================
# CODEALPHA INTERNSHIP
# PROJECT: UNEMPLOYMENT ANALYSIS WITH PYTHON
# ============================================================

# 1. IMPORT LIBRARIES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries imported successfully!")

sns.set_theme(style="whitegrid")

# 2. LOAD DATASET

df = pd.read_csv("C:/Users/HP/Downloads/archive (1)/Unemployment in India.csv")

print("\nOriginal Dataset:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

# 3. DATA CLEANING

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Remove extra spaces from text values
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip()

# Convert Date column into datetime format
df["Date"] = pd.to_datetime(
    df["Date"],
    dayfirst=True,
    errors="coerce"
)

# Convert numerical columns
numeric_cols = [
    "Estimated Unemployment Rate (%)",
    "Estimated Employed",
    "Estimated Labour Participation Rate (%)"
]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove rows with missing essential values
df.dropna(
    subset=[
        "Region",
        "Date",
        "Area",
        "Estimated Unemployment Rate (%)"
    ],
    inplace=True
)

df.reset_index(drop=True, inplace=True)

print("\nCleaned Dataset:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nCleaned Dataset Shape:")
print(df.shape)

# 4. EXPLORATORY DATA ANALYSIS

print("\nStatistical Summary:")
print(df.describe())

print("\nRegion-wise Average Unemployment Rate:")

region_analysis = (
    df.groupby("Region")["Estimated Unemployment Rate (%)"]
    .mean()
    .sort_values(ascending=False)
)

print(region_analysis)

# 5. AREA-WISE UNEMPLOYMENT ANALYSIS

area_analysis = (
    df.groupby("Area")["Estimated Unemployment Rate (%)"]
    .mean()
)

print("\nArea-wise Unemployment Rate:")
print(area_analysis)

plt.figure(figsize=(8, 5))

sns.barplot(
    x=area_analysis.index,
    y=area_analysis.values
)

plt.title("Average Unemployment Rate by Area")
plt.xlabel("Area")
plt.ylabel("Unemployment Rate (%)")

plt.tight_layout()
plt.show()

# 6. STATE-WISE UNEMPLOYMENT ANALYSIS

plt.figure(figsize=(12, 8))

region_analysis.sort_values().plot(
    kind="barh"
)

plt.title("Average Unemployment Rate by Region")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Region")

plt.tight_layout()
plt.show()

# 7. MONTHLY UNEMPLOYMENT TREND

monthly_data = (
    df.groupby("Date")["Estimated Unemployment Rate (%)"]
    .mean()
    .sort_index()
)

plt.figure(figsize=(12, 5))

plt.plot(
    monthly_data.index,
    monthly_data.values,
    marker="o"
)

plt.title("Monthly Unemployment Rate in India")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 8. COVID-19 IMPACT ANALYSIS

# Before COVID period: Before March 2020
# COVID period: March 2020 onwards

before_covid = df[
    df["Date"] < "2020-03-01"
]

during_covid = df[
    df["Date"] >= "2020-03-01"
]

before_rate = before_covid[
    "Estimated Unemployment Rate (%)"
].mean()

during_rate = during_covid[
    "Estimated Unemployment Rate (%)"
].mean()

print("\nCOVID-19 IMPACT ANALYSIS")

print("Average Unemployment Before March 2020:",
      round(before_rate, 2), "%")

print("Average Unemployment From March 2020:",
      round(during_rate, 2), "%")

print("Difference:",
      round(during_rate - before_rate, 2), "percentage points")

# Visual comparison

covid_comparison = pd.DataFrame({
    "Period": ["Before COVID-19", "March 2020 Onwards"],
    "Unemployment Rate": [before_rate, during_rate]
})

plt.figure(figsize=(8, 5))

sns.barplot(
    data=covid_comparison,
    x="Period",
    y="Unemployment Rate"
)

plt.title("Unemployment Rate: Before and During COVID-19")
plt.xlabel("Period")
plt.ylabel("Average Unemployment Rate (%)")

plt.tight_layout()
plt.show()

# 9. EMPLOYMENT ANALYSIS

employment_analysis = (
    df.groupby("Date")["Estimated Employed"]
    .mean()
    .sort_index()
)

plt.figure(figsize=(12, 5))

plt.plot(
    employment_analysis.index,
    employment_analysis.values,
    marker="o"
)

plt.title("Employment Trend in India")
plt.xlabel("Date")
plt.ylabel("Estimated Employed")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 10. LABOUR PARTICIPATION ANALYSIS

participation_analysis = (
    df.groupby("Date")[
        "Estimated Labour Participation Rate (%)"
    ].mean()
    .sort_index()
)

plt.figure(figsize=(12, 5))

plt.plot(
    participation_analysis.index,
    participation_analysis.values,
    marker="o"
)

plt.title("Labour Participation Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Participation Rate (%)")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 11. CORRELATION ANALYSIS

plt.figure(figsize=(8, 6))

correlation = df[
    numeric_cols
].corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Between Employment Variables")

plt.tight_layout()
plt.show()

# 12. HIGHEST UNEMPLOYMENT OBSERVATION

highest = df.loc[
    df["Estimated Unemployment Rate (%)"].idxmax()
]

print("\nHighest Unemployment Observation:")

print("Region:", highest["Region"])
print("Area:", highest["Area"])
print("Date:", highest["Date"].date())

print(
    "Unemployment Rate:",
    highest["Estimated Unemployment Rate (%)"],
    "%"
)

# 13. FINAL INSIGHTS

print("\n========== PROJECT FINDINGS ==========")

print(
    "Average unemployment before March 2020:",
    round(before_rate, 2), "%"
)

print(
    "Average unemployment from March 2020:",
    round(during_rate, 2), "%"
)

print(
    "Highest unemployment region:",
    highest["Region"]
)

print(
    "Highest unemployment rate:",
    highest["Estimated Unemployment Rate (%)"],
    "%"
)

print(
    "Highest unemployment observation area:",
    highest["Area"]
)

print("\n========== PROJECT COMPLETED ==========")

# 14. SAVE CLEANED DATASET

df.to_csv(
    "Cleaned_Unemployment_Data.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")
