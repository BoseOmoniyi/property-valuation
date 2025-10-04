

\# Property Valuation Model



\[!\[Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/BoseOmoniyi/property-valuation/blob/main/notebooks/BoseOmoniyi\_ta\_colab.ipynb)



Automated valuation model (AVM) to predict assessed property values in Winnipeg, Manitoba.



> \*\*Start\*\*: Click the badge above to run the complete analysis in Google Colab



\## Overview



This project develops a machine learning model to predict property assessment values in Winnipeg using publicly available data from the City of Winnipeg's Open Data Portal.



\## Data Source



\- \*\*Source\*\*: \[City of Winnipeg Open Data Portal](https://data.winnipeg.ca/)

\- \*\*Dataset\*\*: Assessment Parcels

\- \*\*Dataset ID\*\*: d4mq-wa44

\- \*\*API Endpoint\*\*: https://data.winnipeg.ca/resource/d4mq-wa44.json

\- \*\*Format\*\*: Socrata Open Data API (SODA)



\*\*Note\*\*: Based on assessment requirements, data should not be included in this repository so data is automatically fetched from the API when running the code.



\## Options to Run Model



\### Option 1: Google Colab (Recommended)



\*\*No installation required!\*\*



1\. Click the "Open in Colab" badge above

2\. Run all cells (Runtime → Run all)

3\. Complete analysis runs in the cloud



\### Option 2: Local Setup

```bash

\# Clone repository

git clone https://github.com/BoseOmoniyi/property-valuation.git

cd property-valuation



\# Install dependencies

pip install -r requirements.txt



\# Fetch data and run model

python main.py

