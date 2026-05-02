import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ==============================
# STEP 1: Load Dataset
# ==============================
df = pd.read_csv("messy_dataset.csv")

print("===== ORIGINAL DATA =====")
print(df)

# ==============================
# STEP 2: Clean Data
# ==============================

# Fix incorrect text values
df['Age'] = df['Age'].replace("thirty-eight", 38)
df['Salary'] = df['Salary'].replace("sixty five thousand", 65000)

# Convert Age and Salary to numeric
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')
df['Salary'] = pd.to_numeric(df['Salary'], errors='coerce')

# Fix country values
df['Country'] = df['Country'].replace("AU", "AUS")

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df['Name'] = df['Name'].fillna("Unknown")
df['Country'] = df['Country'].fillna(df['Country'].mode()[0])
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

# Fix missing ID
df['ID'] = df['ID'].fillna(6)
df['ID'] = df['ID'].astype(int)

# Convert Join Date to datetime
df['Join Date'] = pd.to_datetime(df['Join Date'], errors='coerce', dayfirst=True)

print("\n===== CLEANED DATA =====")
print(df)

# ==============================
# STEP 3: Histogram
# ==============================
df[['Age', 'Salary']].hist(figsize=(8, 4))
plt.suptitle("Age and Salary Distribution")
plt.savefig("histogram.png", dpi=300, bbox_inches="tight")
plt.show()

# ==============================
# STEP 4: Pearson Correlation Heatmap
# ==============================
corr = df[['Age', 'Salary']].corr(method='pearson')

plt.figure(figsize=(6, 4))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Pearson Correlation Heatmap")
plt.savefig("heatmap.png", dpi=300, bbox_inches="tight")
plt.show()

# ==============================
# STEP 5: Outlier Detection Boxplot
# ==============================
plt.figure(figsize=(6, 4))
sns.boxplot(data=df[['Age', 'Salary']])
plt.title("Outlier Detection")
plt.savefig("boxplot.png", dpi=300, bbox_inches="tight")
plt.show()

print("\nImages saved successfully:")
print("histogram.png")
print("heatmap.png")
print("boxplot.png")