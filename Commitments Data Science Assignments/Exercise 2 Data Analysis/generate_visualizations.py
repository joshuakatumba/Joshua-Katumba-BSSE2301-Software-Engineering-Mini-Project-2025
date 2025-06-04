import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create output directory if it doesn't exist
if not os.path.exists('visualizations'):
    os.makedirs('visualizations')

# Read the data
df = pd.read_csv('AfricaCupofNationsMatches.csv')

# Set style for better visualizations
plt.style.use('seaborn-v0_8')
sns.set_palette('husl')

# 1. Goals Distribution
plt.figure(figsize=(12, 6))
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
sns.histplot(data=df, x='HomeTeamGoals', bins=range(0, 10), ax=ax1)
ax1.set_title('Distribution of Home Team Goals')
ax1.set_xlabel('Goals')
ax1.set_ylabel('Frequency')

sns.histplot(data=df, x='AwayTeamGoals', bins=range(0, 10), ax=ax2)
ax2.set_title('Distribution of Away Team Goals')
ax2.set_xlabel('Goals')
ax2.set_ylabel('Frequency')
plt.tight_layout()
plt.savefig('visualizations/goals_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Top Teams by Goals
plt.figure(figsize=(12, 6))
home_goals = df.groupby('HomeTeam')['HomeTeamGoals'].sum()
away_goals = df.groupby('AwayTeam')['AwayTeamGoals'].sum()
total_goals = home_goals.add(away_goals, fill_value=0)
top_10_teams = total_goals.sort_values(ascending=False).head(10)

sns.barplot(x=top_10_teams.index, y=top_10_teams.values)
plt.title('Top 10 Teams by Total Goals Scored')
plt.xticks(rotation=45)
plt.xlabel('Team')
plt.ylabel('Total Goals')
plt.tight_layout()
plt.savefig('visualizations/top_teams_goals.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Attendance by Stage
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='Stage', y='Attendance')
plt.title('Attendance Distribution by Match Stage')
plt.xticks(rotation=45)
plt.xlabel('Match Stage')
plt.ylabel('Attendance')
plt.tight_layout()
plt.savefig('visualizations/attendance_by_stage.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. Historical Trends
plt.figure(figsize=(15, 6))
df['TotalGoals'] = df['HomeTeamGoals'] + df['AwayTeamGoals']
yearly_goals = df.groupby('Year')['TotalGoals'].mean()
plt.plot(yearly_goals.index, yearly_goals.values, marker='o')
plt.title('Average Goals per Match Over Time')
plt.xlabel('Year')
plt.ylabel('Average Goals per Match')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visualizations/historical_trends.png', dpi=300, bbox_inches='tight')
plt.close()

# 5. Match Stage Distribution
plt.figure(figsize=(10, 10))
stage_counts = df['Stage'].value_counts()
plt.pie(stage_counts.values, labels=stage_counts.index, autopct='%1.1f%%')
plt.title('Distribution of Matches by Stage')
plt.axis('equal')
plt.savefig('visualizations/stage_distribution.png', dpi=300, bbox_inches='tight')
plt.close()

# 6. Top Stadiums
plt.figure(figsize=(12, 6))
stadium_counts = df['Stadium'].value_counts().head(10)
sns.barplot(x=stadium_counts.index, y=stadium_counts.values)
plt.title('Top 10 Stadiums by Number of Matches')
plt.xticks(rotation=45)
plt.xlabel('Stadium')
plt.ylabel('Number of Matches')
plt.tight_layout()
plt.savefig('visualizations/top_stadiums.png', dpi=300, bbox_inches='tight')
plt.close()

# 7. Correlation Heatmap
plt.figure(figsize=(8, 6))
numeric_cols = ['HomeTeamGoals', 'AwayTeamGoals', 'Attendance']
correlation = df[numeric_cols].corr()
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation Matrix')
plt.tight_layout()
plt.savefig('visualizations/correlation_heatmap.png', dpi=300, bbox_inches='tight')
plt.close()

# 8. Goals Over Time
plt.figure(figsize=(15, 6))
yearly_stats = df.groupby('Year').agg({
    'HomeTeamGoals': 'mean',
    'AwayTeamGoals': 'mean'
}).reset_index()

plt.plot(yearly_stats['Year'], yearly_stats['HomeTeamGoals'], marker='o', label='Home Goals')
plt.plot(yearly_stats['Year'], yearly_stats['AwayTeamGoals'], marker='o', label='Away Goals')
plt.title('Average Goals per Match Over Time')
plt.xlabel('Year')
plt.ylabel('Average Goals')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('visualizations/goals_over_time.png', dpi=300, bbox_inches='tight')
plt.close()

print("Visualizations have been generated in the 'visualizations' directory.") 