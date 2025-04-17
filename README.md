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

