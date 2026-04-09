# ============================================
# ADS500B - Step 3: Data Importing, Processing,
# Analysis, and Basic Machine Learning
# ============================================

# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# ============================================
# 1. LOAD DATASET
# ============================================

# CHANGE this to your dataset file name
file_path = "dataset.csv"

df = pd.read_csv(file_path)

print("\n=== FIRST 5 ROWS ===")
print(df.head())


# ============================================
# 2. DESCRIBE DATASET
# ============================================

print("\n=== DATASET SHAPE ===")
print(df.shape)

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== SUMMARY STATISTICS ===")
print(df.describe())

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())


# ============================================
# 3. DATA CLEANING
# ============================================

# Remove duplicates
df = df.drop_duplicates()

# Handle missing values (choose one approach)
df = df.dropna()

# Alternative:
# df.fillna(df.mean(numeric_only=True), inplace=True)

print("\n=== AFTER CLEANING ===")
print(df.isnull().sum())


# ============================================
# 4. DATA TRANSFORMATION
# ============================================

# Normalize numeric columns
scaler = StandardScaler()
numeric_cols = df.select_dtypes(include=np.number).columns

df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

print("\n=== NORMALIZED DATA SAMPLE ===")
print(df.head())


# ============================================
# 5. DATA REDUCTION / DISCRETIZATION
# ============================================

# Example: Drop unnecessary columns (EDIT if needed)
# df = df.drop(columns=["column_name"])

# Example: Binning (EDIT if needed)
# df["binned"] = pd.cut(df["column"], bins=3, labels=["Low", "Medium", "High"])


# ============================================
# 6. IDENTIFY VARIABLE TYPES
# ============================================

categorical = df.select_dtypes(include=["object"]).columns
numerical = df.select_dtypes(include=np.number).columns

print("\nCategorical Columns:", list(categorical))
print("Numerical Columns:", list(numerical))


# ============================================
# 7. VISUALIZATION
# ============================================

# Histograms
df[numerical].hist(figsize=(10, 8))
plt.tight_layout()
plt.savefig("histograms.png")
plt.close()

# Boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(data=df[numerical])
plt.xticks(rotation=45)
plt.savefig("boxplot.png")
plt.close()

# Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.savefig("correlation_heatmap.png")
plt.close()


# ============================================
# 8. MACHINE LEARNING
# ============================================

# Select target (CHANGE THIS)
target = df.columns[-1]

X = df.drop(columns=[target])
y = df[target]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n=== MODEL PERFORMANCE ===")
print("Mean Squared Error:", mse)
print("R2 Score:", r2)


# ============================================
# 9. SAVE CLEANED DATA
# ============================================

df.to_csv("cleaned_data.csv", index=False)

print("\n=== PROCESS COMPLETE ===")
