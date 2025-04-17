import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium
from folium.plugins import HeatMap
import plotly.express as px

sns.set(style='whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

print("/n Loading and Cleaning Dataset...")
df = pd.read_excel("C:/Users/hello/Downloads/cleaned_python_dataset_ca.xlsx")


df.columns = df.columns.str.strip().str.upper().str.replace(" ", "_")

# Basic EDA Prints
print("/n Dataset Overview")
print(df)
print("/n Head of the dataset")
print(df.head())
print("/n Tail of the dataset")
print(df.tail())
print("/n Summary Statistics")
print(df.describe())
print("/n Info")
print(df.info())
print("/n Column Names")
print(df.columns)
print("/n Shape of Dataset")
print(df.shape)
print("/n Null Values")
print(df.isnull().sum())

# Date & Time Conversion
df['DATE_OCC'] = pd.to_datetime(df['DATE_OCC'], errors='coerce')
df['DATE_RPTD'] = pd.to_datetime(df['DATE_RPTD'], errors='coerce')
df['TIME_OCC'] = df['TIME_OCC'].astype(str).str.zfill(4)
df['HOUR'] = df['TIME_OCC'].str[:2].astype(int)
df['YEAR'] = df['DATE_OCC'].dt.year
df['MONTH'] = df['DATE_OCC'].dt.month

# Correlation & Covariance
correlation = df.corr(numeric_only=True)
print("/n Correlation Matrix")
print(correlation)
print("/n Covariance Matrix")
print(df.cov(numeric_only=True))

plt.figure()
sns.heatmap(correlation, annot=True, cmap="Blues", linewidth=5, fmt="0.2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()

# 1 Crime Distribution and Trends Over Time
print("/n Answer 1: Crime Distribution and Trends Over Time")

crime_by_month = df.groupby(['YEAR', 'MONTH']).size().reset_index(name='INCIDENTS')
crime_by_month['DATE'] = pd.to_datetime(crime_by_month[['YEAR', 'MONTH']].assign(DAY=1))

plt.figure()
sns.lineplot(data=crime_by_month, x='DATE', y='INCIDENTS')
plt.title('Crime Incidents Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Crimes')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
sns.histplot(df['HOUR'], bins=24, kde=True)
plt.title('Crime Frequency by Hour of the Day')
plt.xlabel('Hour')
plt.ylabel('Number of Crimes')
plt.xticks(range(0, 24))
plt.tight_layout()
plt.show()

heat_data = df.groupby(['YEAR', 'MONTH']).size().unstack()
plt.figure()
sns.heatmap(heat_data, cmap="Reds")
plt.title('Seasonal Crime Heatmap (Month vs Year)')
plt.tight_layout()
plt.show()

# 2 Geographic Crime Analysis (Crime Hotspots)
print("/n Answer 2: Geographic Crime Analysis (Crime Hotspots)")

map_df = df.dropna(subset=['LAT', 'LON'])
crime_map = folium.Map(location=[map_df['LAT'].mean(), map_df['LON'].mean()], zoom_start=10)
heat_data = [[row['LAT'], row['LON']] for _, row in map_df.iterrows()]
HeatMap(heat_data).add_to(crime_map)
crime_map.save("crime_hotspots_map.html")
print("✅ Crime hotspot map saved as: crime_hotspots_map.html")

area_crime = df['AREA_NAME'].value_counts().head(10)
plt.figure()
sns.barplot(x=area_crime.values, y=area_crime.index)
plt.title('Top 10 High-Crime Areas')
plt.xlabel('Number of Crimes')
plt.tight_layout()
plt.show()

# 3 Crime Type Analysis
print("/n Answer 3: Crime Type Analysis")

top_crimes = df['CRM_CD_DESC'].value_counts().head(10)
plt.figure()
sns.barplot(x=top_crimes.values, y=top_crimes.index, hue=top_crimes.index, palette='magma', legend=False)
plt.title('Top 10 Crime Types')
plt.xlabel('Frequency')
plt.tight_layout()
plt.show()

weapon_usage = df['WEAPON_DESC'].value_counts().head(10)
plt.figure()
sns.barplot(x=weapon_usage.values, y=weapon_usage.index, hue=weapon_usage.index, palette='coolwarm', legend=False)
plt.title('Top 10 Weapons Used')
plt.xlabel('Frequency')
plt.tight_layout()
plt.show()

# 4 Victim Demographics Breakdown
print("/n Answer 4: Victim Demographics Breakdown")

plt.figure()
sns.histplot(df['VICT_AGE'].dropna(), bins=20, kde=True, color='purple')
plt.title('Victim Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of Victims')
plt.tight_layout()
plt.show()

gender_count = df['VICT_SEX'].value_counts()
plt.figure()
sns.barplot(x=gender_count.index, y=gender_count.values, hue=gender_count.index, palette='pastel', legend=False)
plt.title('Gender Distribution of Victims')
plt.xlabel('Gender')
plt.ylabel('Number of Victims')
plt.tight_layout()
plt.show()

ethnicity = df['VICT_DESCENT'].value_counts().head(10)
plt.figure()
sns.barplot(x=ethnicity.values, y=ethnicity.index, hue=ethnicity.index, palette='BuGn_r', legend=False)
plt.title('Top 10 Affected Ethnic Groups')
plt.xlabel('Number of Victims')
plt.tight_layout()
plt.show()

# 5 Crime Resolution Status Analysis
print("/n Answer 5: Crime Resolution Status Analysis")

status_counts = df['STATUS_DESC'].value_counts()
plt.figure()
plt.pie(status_counts, labels=status_counts.index, startangle=140, autopct='%1.1f%%', wedgeprops={'width': 0.4})
plt.title('Crime Resolution Status (Donut Chart)')
plt.tight_layout()
plt.show()

top_types = df['CRM_CD_DESC'].value_counts().nlargest(5).index
status_by_type = df[df['CRM_CD_DESC'].isin(top_types)].groupby(['CRM_CD_DESC', 'STATUS_DESC']).size().unstack().fillna(0)
status_by_type.plot(kind='bar', stacked=True, colormap='Set2')
plt.title('Crime Status Breakdown for Top 5 Crime Types')
plt.xlabel('Crime Type')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()





