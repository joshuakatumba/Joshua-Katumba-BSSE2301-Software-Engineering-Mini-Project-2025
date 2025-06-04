import pandas as pd
import numpy as np
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Read the CSV file
input_file = os.path.join(current_dir, 'Mine.csv')
df = pd.read_csv(input_file)

# 1. Handle missing values
# Replace NaN values in numeric columns with their median
numeric_columns = ['Duration', 'Pulse', 'Maxpulse', 'Calories']
for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

# 2. Fix inconsistent date formats
# Remove any trailing quotes and standardize date format
df['Date'] = df['Date'].str.replace("'", "")
df['Date'] = pd.to_datetime(df['Date'], format='%Y/%m/%d', errors='coerce')

# 3. Remove duplicate rows
df = df.drop_duplicates()

# 4. Fix wrong data
# Remove any rows where Duration is unreasonably high (e.g., > 180 minutes)
df = df[df['Duration'] <= 180]

# Ensure Pulse is less than Maxpulse
df = df[df['Pulse'] <= df['Maxpulse']]

# 5. Remove unnecessary columns (if any)
# In this case, all columns seem relevant, but we can add logic here if needed

# Save the cleaned dataset
output_file = os.path.join(current_dir, 'cleaned_data.csv')
df.to_csv(output_file, index=False)

# Print summary of the cleaning process
print("Data Cleaning Summary:")
print(f"Original number of rows: {len(pd.read_csv(input_file))}")
print(f"Final number of rows: {len(df)}")
print("\nMissing values after cleaning:")
print(df.isnull().sum()) 