import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Read the dataset
df = pd.read_csv('climate_action_data.csv')

# Display initial information
print("\nInitial Dataset Info:")
print(df.info())
print("\nInitial Missing Values:")
print(df.isnull().sum())

# Clean the dataset
# 1. Replace 'error' values with NaN
df = df.replace('error', np.nan)

# 2. Convert numeric columns to appropriate types
numeric_columns = ['Soil_Moisture(%)', 'Soil_pH', 'Temperature(C)', 'Humidity(%)', 
                  'Fertilizer_Recommended(kg/ha)', 'Irrigation_Recommended(mm)']
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# 3. Convert date to datetime
df['Date'] = pd.to_datetime(df['Date'])

# 4. Remove duplicate rows
df = df.drop_duplicates()

# 5. Handle missing values
# For numeric columns, fill with median
for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

# For categorical columns, fill with mode
df['Crop_Type'] = df['Crop_Type'].fillna(df['Crop_Type'].mode()[0])

# Display cleaned dataset information
print("\nCleaned Dataset Info:")
print(df.info())
print("\nCleaned Missing Values:")
print(df.isnull().sum())

# Save cleaned dataset
df.to_csv('cleaned_precision_agriculture_data.csv', index=False)

# Exploratory Data Analysis
print("\nDescriptive Statistics:")
print(df.describe())

# Create histograms for numeric variables
plt.figure(figsize=(15, 10))
for i, col in enumerate(numeric_columns, 1):
    plt.subplot(2, 3, i)
    sns.histplot(data=df, x=col, bins=30)
    plt.title(f'Distribution of {col}')
plt.tight_layout()
plt.savefig('numeric_distributions.png')
plt.close()

# Create correlation heatmap
plt.figure(figsize=(10, 8))
correlation_matrix = df[numeric_columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Heatmap')
plt.tight_layout()
plt.savefig('correlation_heatmap.png')
plt.close()

# Analysis of fertilizer recommendations
print("\nFertilizer Recommendations by Crop Type:")
fertilizer_by_crop = df.groupby('Crop_Type')['Fertilizer_Recommended(kg/ha)'].mean().sort_values(ascending=False)
print(fertilizer_by_crop)

# Find crop with highest average soil moisture
print("\nAverage Soil Moisture by Crop Type:")
moisture_by_crop = df.groupby('Crop_Type')['Soil_Moisture(%)'].mean().sort_values(ascending=False)
print(moisture_by_crop)

# Analyze crops with high temperature
high_temp_crops = df[df['Temperature(C)'] > 30]
print("\nCrops with Temperature > 30°C:")
print(high_temp_crops[['Crop_Type', 'Temperature(C)', 'Irrigation_Recommended(mm)']].groupby('Crop_Type').mean())

# Generate insights
print("\nKey Insights:")
print("1. Most influential variables for fertilizer recommendations:")
correlations = correlation_matrix['Fertilizer_Recommended(kg/ha)'].sort_values(ascending=False)
print(correlations)

print("\n2. Crop with highest average soil moisture:", moisture_by_crop.index[0])
print("   Average soil moisture:", round(moisture_by_crop.iloc[0], 2), "%")

print("\n3. Irrigation recommendations for high temperature crops:")
high_temp_irrigation = high_temp_crops.groupby('Crop_Type')['Irrigation_Recommended(mm)'].mean()
print(high_temp_irrigation) 