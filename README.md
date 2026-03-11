# Content Performance Analysis (Python)
Python pipeline for Instagram engagement analysis, including data cleaning, IQR outlier detection and category-based performance metrics. 

## Example Output
![Engagement Report](images/comparison_with_and_without_outliers_categories_post.png)
The chart shows inconsistent values and extreme outliers that distort engagement metrics and make analysis unreliable.

## Problem

Social media datasets often contain inconsistent values and extreme outliers that distort engagement metrics and make analysis unreliable.

## Solution

This project cleans and processes engagement data, calculates key metrics, detects outliers, and categorizes content to enable more reliable performance analysis.

## Tech Stack

Python  
Pandas  
NumPy
Openpyxl
matplotlib

## Features

- Data cleaning and normalization
- Engagement metric calculation
- Content categorization
- Outlier detection using IQR method

## How to Run

```bash
pip install -r requirements.txt
python main.py