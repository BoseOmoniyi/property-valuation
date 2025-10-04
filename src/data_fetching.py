"""
Fetch data from Winnipeg Open Data Portal API
"""
import pandas as pd
import requests
import json
from pathlib import Path
from datetime import datetime

# API URL - defined here to avoid circular import
WINNIPEG_API_URL = "https://data.winnipeg.ca/resource/d4mq-wa44.json"


def get_dataset_info(api_url=None):
    """
    Get information about the dataset (row count, columns, etc.)
    
    Parameters
    ----------
    api_url : str, optional
        API endpoint URL
        
    Returns
    -------
    dict
        Dataset metadata
    """
    if api_url is None:
        api_url = WINNIPEG_API_URL
    
    print("Fetching dataset information...")
    
    # Get sample to see columns
    response = requests.get(api_url, params={'$limit': 1})
    response.raise_for_status()
    sample = response.json()
    
    # Try to get count
    try:
        count_params = {'$select': 'COUNT(*)'}
        count_response = requests.get(api_url, params=count_params)
        count_data = count_response.json()
        total_count = int(count_data[0]['COUNT']) if count_data else 'Unknown'
    except:
        total_count = 'Unknown'
    
    info = {
        'total_records': total_count,
        'columns': list(sample