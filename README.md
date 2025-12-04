Weather Data Visualizer
-----------------------

## 📌 Project Overview
Weather Data Visualizer is a Python-based project that analyzes real-world weather data and creates meaningful insights through data cleaning, statistical analysis, and visualizations.  
This project uses **Pandas, NumPy, and Matplotlib** to process weather information such as temperature, humidity, and rainfall.

---

## 🎯 Objectives  
This project aims to:  
- Load and clean raw CSV weather data  
- Identify missing values and normalize inconsistent column names  
- Calculate daily and monthly temperature statistics  
- Generate graphics such as line plots, bar charts, and scatter plots  
- Group data by months and seasons  
- Export cleaned data and generate a weather analysis report  

---

## 🗂️ Features  
✔ Automatically detects correct Date, Temperature, Humidity, and Rainfall columns  
✔ Handles missing rainfall by generating realistic synthetic values  
✔ Cleans and prepares dataset (drops invalid dates, normalizes names)  
✔ Computes:  
- Mean / Min / Max / Std Temperature  
- Monthly statistics  
- Seasonal averages  

✔ Generates professional plots:  
- Daily Temperature Trend  
- Monthly Rainfall Bar Chart  
- Humidity vs Temperature Scatter Plot  
- Combined Temperature + Rainfall plot  

✔ Exports:  
- Cleaned CSV file (`cleaned_weather_data.csv`)  
- Markdown report (`weather_report.md`)  
- PNG visualizations  

---

## 📁 Files Generated  
After running the code, the following output files are created:

- `cleaned_weather_data.csv`  
- `daily_temperature.png`  
- `monthly_rainfall.png`  
- `humidity_vs_temperature.png`  
- `combined_plot.png`  
- `weather_report.md`  

These files contain your processed data, visual insights, and final analysis report.

---

## 🛠️ Technologies Used  
- **Python**  
- **Pandas** for data cleaning and manipulation  
- **NumPy** for statistical calculations  
- **Matplotlib** for plotting  
- **CSV datasets**  

---

## ▶️ How to Run  
1. Install required libraries:
    ```bash
    pip install pandas numpy matplotlib
    ```
2. Place your weather CSV file in the same folder.  
3. Make sure the file name matches:
    ```
    Weather Data.csv
    ```
4. Run the script:
    ```bash
    python weather data.py
    ```

---

## 📊 Sample Output  
The project prints:  
- Dataset head  
- Basic information  
- Cleaned data  
- Daily temperature statistics  
- Monthly and seasonal statistics  

And generates all plots inside the project folder.
