import pandas as pd
import numpy as np

# SERIES EXERCISES

# 1. Compare elements of two Pandas series
def compare_series():
    series1 = pd.Series([4, 65, 436, 3, 9])
    series2 = pd.Series([7, 0, 3, 897, 9])
    comparison = series1 == series2
    print("\n1. Series Comparison:")
    print(comparison)

# 2. Add, subtract, multiply and divide two Pandas series
def series_operations():
    series1 = pd.Series([2, 4, 6, 8, 14])
    series2 = pd.Series([1, 3, 5, 7, 9])
    print("\n2. Series Operations:")
    print("Addition:", series1 + series2)
    print("Subtraction:", series1 - series2)
    print("Multiplication:", series1 * series2)
    print("Division:", series1 / series2)

# 3. Convert dictionary to Pandas series
def dict_to_series():
    dictionary1 = {'Josh': 24, 'Sam': 36, 'Peace': 19, 'Charles': 65, 'Tom': 44}
    series = pd.Series(dictionary1)
    print("\n3. Dictionary to Series:")
    print(series)

# 4. Convert series to array
def series_to_array():
    series = pd.Series(['Love', 800, 'Joy', 789.9, 'Peace', True])
    array = series.to_numpy()
    print("\n4. Series to Array:")
    print(array)

# 5. Display most frequent value and replace others
def most_frequent_value(df):
    home_goals = df['HomeTeamGoals']
    most_frequent = home_goals.mode()[0]
    modified_series = home_goals.apply(lambda x: x if x == most_frequent else 'Other')
    print("\n5. Most Frequent Home Team Goals:")
    print(modified_series)

# DATAFRAME EXERCISES

def dataframe_exercises(df):
    # 1. Read CSV file (already done above)
    print("\n1. DataFrame loaded successfully")
    
    # 2. Get first 7 rows
    print("\n2. First 7 rows:")
    print(df.head(7))
    
    # 3. Select specific columns
    selected_columns = df[['HomeTeam', 'AwayTeam', 'HomeTeamGoals', 'AwayTeamGoals']]
    print("\n3. Selected columns:")
    print(selected_columns)
    
    # 4. Select rows where Egypt appears
    egypt_matches = df[df['HomeTeam'].str.contains('Egypt') | df['AwayTeam'].str.contains('Egypt')]
    print("\n4. Egypt matches:")
    print(egypt_matches)
    
    # 5. Count rows and columns
    rows, cols = df.shape
    print("\n5. DataFrame dimensions:")
    print(f"Rows: {rows}, Columns: {cols}")
    
    # 6. Select rows where Attendance is missing
    missing_attendance = df[df['Attendance'].isna()]
    print("\n6. Matches with missing attendance:")
    print(missing_attendance)
    
    # 7. Select rows where HomeTeamGoals are between 3 and 6
    goals_range = df[(df['HomeTeamGoals'] >= 3) & (df['HomeTeamGoals'] <= 6)]
    print("\n7. Matches with 3-6 home team goals:")
    print(goals_range)
    
    # 8. Change AwayTeamGoals in 3rd row to 10
    df.loc[2, 'AwayTeamGoals'] = 10
    print("\n8. Modified 3rd row AwayTeamGoals:")
    print(df.iloc[2])
    
    # 9. Sort DataFrame
    sorted_df = df.sort_values(['HomeTeam', 'HomeTeamGoals'], ascending=[True, False])
    print("\n9. Sorted DataFrame:")
    print(sorted_df)
    
    # 10. Get column headers
    headers = df.columns.tolist()
    print("\n10. Column headers:")
    print(headers)
    
    # 11. Append new column
    df['TotalGoals'] = df['HomeTeamGoals'] + df['AwayTeamGoals']
    print("\n11. Added TotalGoals column:")
    print(df['TotalGoals'])
    
    # 12. Add 2 rows
    new_rows = pd.DataFrame({
        'Year': [2024, 2024],
        'Date': ['2024-01-01', '2024-01-02'],
        'Time': ['', ''],
        'HomeTeam': ['TeamA', 'TeamB'],
        'AwayTeam': ['TeamC', 'TeamD'],
        'HomeTeamGoals': [2, 1],
        'AwayTeamGoals': [1, 2],
        'Stage': ['Group', 'Group'],
        'SpecialWinConditions': ['', ''],
        'Stadium': ['Stadium1', 'Stadium2'],
        'City': ['City1', 'City2'],
        'Attendance': [10000, 15000],
        'TotalGoals': [3, 3]
    })
    df = pd.concat([df, new_rows], ignore_index=True)
    print("\n12. Added 2 new rows:")
    print(df.tail(2))
    
    # 13. Change Uganda to China in AwayTeam
    df['AwayTeam'] = df['AwayTeam'].replace('Uganda', 'China')
    print("\n13. Changed Uganda to China in AwayTeam:")
    print(df[df['AwayTeam'] == 'China'])
    
    # 14. Reset index
    df = df.reset_index(drop=True)
    print("\n14. Reset index:")
    print(df.head())
    
    # 15. Check if Stadium column exists
    has_stadium = 'Stadium' in df.columns
    print("\n15. Stadium column exists:", has_stadium)
    
    # 16. Convert AwayTeamGoals to float
    df['AwayTeamGoals'] = df['AwayTeamGoals'].astype(float)
    print("\n16. AwayTeamGoals data type:", df['AwayTeamGoals'].dtype)
    
    # 17. Remove last 10 rows
    df = df.iloc[:-10]
    print("\n17. Removed last 10 rows. New shape:", df.shape)
    
    # 18. Iterate over rows
    print("\n18. First 3 rows:")
    for index, row in df.head(3).iterrows():
        print(f"Row {index}: {row['HomeTeam']} vs {row['AwayTeam']}")
    
    # 19. Change column order
    new_order = ['Year', 'Date', 'Time', 'HomeTeam', 'AwayTeam', 'HomeTeamGoals', 
                 'AwayTeamGoals', 'TotalGoals', 'Stage', 'SpecialWinConditions', 
                 'Stadium', 'City', 'Attendance']
    df = df[new_order]
    print("\n19. New column order:")
    print(df.columns.tolist())
    
    # 20. Delete rows with 0 HomeTeamGoals
    df = df[df['HomeTeamGoals'] != 0]
    print("\n20. Removed rows with 0 HomeTeamGoals. New shape:", df.shape)
    
    return df

# Run all exercises
if __name__ == "__main__":
    # Read the CSV file
    df = pd.read_csv('AfricaCupofNationsMatches.csv')
    
    print("SERIES EXERCISES")
    compare_series()
    series_operations()
    dict_to_series()
    series_to_array()
    
    print("\nDATAFRAME EXERCISES")
    df = dataframe_exercises(df)
    most_frequent_value(df) 