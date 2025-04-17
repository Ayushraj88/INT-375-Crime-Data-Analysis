# INT-375-Crime-Data-Analysis
🕵️‍♂️ Crime Data Analysis & Visualization
This project explores and visualizes crime data to uncover meaningful insights about criminal activity across time, geography, crime types, victim demographics, and case resolutions. The goal is to assist analysts, policymakers, and citizens in understanding crime trends and patterns to support data-driven decision-making.

📌 Key Objectives
1. 📈 Crime Distribution and Trends Over Time
Visuals: Line charts, bar plots, heatmaps

Insights:

Compare crime frequency by date reported vs. date occurred

Identify peak crime hours using time-of-occurrence data

Highlight seasonal trends in crime using monthly and yearly breakdowns

2. 🗺️ Geographic Crime Analysis (Hotspot Mapping)
Visuals: Interactive map using Folium, bar plots

Insights:

Pinpoint high-crime zones using latitude and longitude coordinates

Compare crime activity across districts (e.g., AREA, AREA NAME, Rpt Dist No)

Visualize top 10 high-crime neighborhoods

3. 🧪 Crime Type Analysis
Visuals: Bar charts, treemaps, pie charts

Insights:

Show distribution of different crime types (CRM_CD_DESC)

Identify most frequent crimes by category and area

Analyze weapon usage (WEAPON_DESC) and its impact on crime severity

4. 👤 Victim Demographics Breakdown
Visuals: Histograms, gender distribution charts, bar graphs

Insights:

Analyze crime victims by age (VICT_AGE)

Compare crime rates affecting males vs. females (VICT_SEX)

Identify if certain ethnic groups (VICT_DESCENT) are disproportionately affected

5. ✅ Crime Resolution Status Analysis
Visuals: Donut charts, stacked bar plots

Insights:

Show proportions of solved vs. pending cases (STATUS, STATUS_DESC)

Examine clearance rates across different crime types

Identify which crimes are more likely to be resolved

🛠️ Technologies Used
Python

Pandas for data manipulation

Matplotlib & Seaborn for static visualizations

Folium & Plotly for interactive maps and charts

Jupyter Notebook or any Python IDE for analysis and development

📂 Dataset
Source: Cleaned crime dataset (cleaned_python_dataset_ca.xlsx)

Key Fields: DATE_OCC, DATE_RPTD, TIME_OCC, CRM_CD_DESC, VICT_SEX, VICT_AGE, WEAPON_DESC, LAT, LON, STATUS_DESC, etc.

📍 Output Highlights
📅 Trend plots showcasing crime spikes over time

🔥 Interactive heatmap of crime hotspots

🧩 Category breakdowns for types of crimes and weapon usage

👥 Demographic insights of victims

🗂️ Status overview of case resolutions

📁 How to Use
Clone the repository

Install dependencies using pip install -r requirements.txt

Make sure the dataset (cleaned_python_dataset_ca.xlsx) is in the correct directory

Run the script or notebook to generate all visualizations

Open crime_hotspots_map.html in a browser to explore the interactive map

## Project Overview

**Crime Data Analysis & Visualization**

This script performs analysis and visualization on a cleaned crime dataset. It covers various tasks including data cleaning, exploratory data analysis (EDA), and the generation of multiple visualizations to understand crime patterns across several dimensions.

**Key functionalities include:**
- **Loading and cleaning the dataset from an Excel file:** The script reads in the dataset and standardizes column names.
- **Standardizing column names and converting date/time fields:** Dates, times, and columns are transformed for easier analysis.
- **Displaying basic dataset information:** It outputs the overview, head, tail, summary statistics, column names, shape, and null values.
- **Creating new time-based columns:** Additional fields like HOUR, YEAR, and MONTH are derived from the date information.
- **Calculating and visualizing correlation and covariance matrices:** These assist in understanding relationships between variables.
- **Analyzing crime trends over time:** Uses line charts, histograms (crime frequency by hour), and heatmaps (seasonal trends).
- **Generating geographic visualizations with Folium:** Includes an interactive heatmap for crime hotspots and a bar chart for top high-crime areas.
- **Visualizing crime type distributions:** Uses bar charts and treemaps to show the frequency of different crime types.
- **Breaking down victim demographics:** Analyzes age, gender, and ethnicity with histograms and bar plots.
- **Analyzing crime resolution statuses:** Displays donut charts and stacked bar plots highlighting case clearances by crime type.

