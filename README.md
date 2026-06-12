# Data Cleaning & Reporting Automation

## Overview

This project automates data cleaning, validation, reporting, and visualization workflows using Python. The objective is to improve data quality, reduce manual preprocessing effort, and generate meaningful reports from HR employee data.

The project performs automated data quality checks, generates summary reports, and creates visualizations to support business decision-making.



## Objectives

- Automate data cleaning workflows
- Validate dataset quality
- Detect missing values and duplicate records
- Generate automated reports
- Create visual summaries for HR analytics
- Improve reporting efficiency through automation



## Dataset

The project uses an Employee Attrition dataset containing employee demographic, job-related, and performance information.

Key attributes include:

- Age
- Gender
- Education
- Job Role
- Monthly Income
- Work-Life Balance
- Job Satisfaction
- Performance Rating
- Overtime
- Attrition Status



## Technologies Used

- Python
- Pandas
- Matplotlib
- VS Code



## Project Workflow

### 1. Data Loading

- Imported employee data from CSV files
- Validated dataset structure and dimensions

### 2. Data Quality Assessment

Performed automated checks for:

- Missing Values
- Duplicate Records
- Dataset Dimensions
- Column Validation

### 3. Data Cleaning

- Verified data completeness
- Ensured data consistency
- Prepared dataset for reporting

### 4. Automated Reporting

Generated a Data Quality Report containing:

- Total Rows
- Total Columns
- Missing Values Count
- Duplicate Records Count

### 5. Data Visualization

Created automated visual reports including:

- Employee Attrition Distribution
- Monthly Income Distribution
- Gender Distribution
- Job Role Distribution



## Project Structure

Data-Cleaning-and-Reporting-Automation/
│
├── images/
│   ├── attrition_distribution.png
│   ├── salary_distribution.png
│   ├── gender_distribution.png
│   └── job_role_distribution.png
│
├── reports/
│   └── data_quality_report.csv
│
├── train.csv
├── test.csv
├── main.py
├── requirements.txt
└── README.md



## Data Quality Results

Metric| Result
Missing Values| 0
Duplicate Records| 0

The dataset passed all automated quality checks and required no additional cleaning.



## Key Insights

- No missing values were detected in the dataset.
- No duplicate records were found.
- Employee attrition patterns were successfully visualized.
- Salary distribution analysis highlighted employee income trends.
- Gender distribution provided workforce demographic insights.
- Job role analysis identified the most common employee positions.



## Generated Outputs

### Reports

- Data Quality Report (CSV)

### Visualizations

- Employee Attrition Distribution
- Salary Distribution
- Gender Distribution
- Job Role Distribution



## Business Value

This project demonstrates how automated data validation and reporting can improve efficiency, reduce manual effort, and provide faster access to actionable insights.



## Future Improvements

- Automated Excel Dashboard Generation
- Power BI Integration
- Scheduled Reporting Automation
- Email-Based Report Delivery
- Interactive Streamlit Dashboard



## Author

## Piyush Royal

Data Analytics | Data Visualization | Automation | Python
