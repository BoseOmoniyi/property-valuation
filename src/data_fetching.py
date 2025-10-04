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
        'columns': list(sample[0].keys()) if sample else [],
        'sample_record': sample[0] if sample else None
    }
    
    return info


def fetch_all_records(api_url, batch_size=50000):
    """
    Fetch all records from Socrata API with pagination.
    
    Parameters
    ----------
    api_url : str
        Base API endpoint URL
    batch_size : int, default=50000
        Number of records per request
        
    Returns
    -------
    pd.DataFrame
        Complete dataset
    """
    all_data = []
    offset = 0
    
    print("Fetching all records with pagination...")
    
    while True:
        params = {
            '$limit': batch_size,
            '$offset': offset
        }
        
        print(f"  Fetching batch at offset {offset}...")
        response = requests.get(api_url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        if not data:  # No more data
            break
            
        all_data.extend(data)
        offset += len(data)
        
        print(f"  Total records fetched: {len(all_data):,}")
        
        # If we got fewer records than requested, we've reached the end
        if len(data) < batch_size:
            break
    
    print(f"Success: Completed! Total records: {len(all_data):,}")
    
    df = pd.DataFrame(all_data)
    return df


def fetch_winnipeg_assessment_data(api_url=None, save_local=True, limit=None):
    """
    Fetch Winnipeg property assessment data from Open Data Portal API.
    
    Uses Socrata Open Data API (SODA) format.
    
    Parameters
    ----------
    api_url : str, optional
        API endpoint URL. If None, uses default
    save_local : bool, default=True
        Whether to save a local copy in data/raw/
    limit : int, optional
        Maximum number of records to fetch. If None, fetches all records.
        
    Returns
    -------
    pd.DataFrame
        Property assessment data
        
    Examples
    --------
    >>> df = fetch_winnipeg_assessment_data(limit=1000)  # Sample
    >>> df = fetch_winnipeg_assessment_data()  # Full dataset
    """
    if api_url is None:
        api_url = WINNIPEG_API_URL
    
    print("=" * 60)
    print("FETCHING WINNIPEG ASSESSMENT DATA")
    print("=" * 60)
    print(f"API URL: {api_url}")
    print()
    
    try:
        if limit is None:
            # Fetch all data with pagination
            df = fetch_all_records(api_url)
        else:
            # Fetch limited records
            print(f"Fetching sample of {limit:,} records...")
            response = requests.get(api_url, params={'$limit': limit})
            response.raise_for_status()
            data = response.json()
            df = pd.DataFrame(data)
            print(f"SUCCESS: Successfully fetched {len(df):,} records")
        
        # Save local copy if requested
        if save_local:
            output_dir = Path('data/raw')
            output_dir.mkdir(parents=True, exist_ok=True)
            
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = output_dir / f'Assessment_Parcels_{timestamp}.csv'
            
            df.to_csv(output_file, index=False)
            print(f"Success: Saved local copy to: {output_file}")
        
        print("=" * 60)
        return df
        
    except requests.exceptions.RequestException as e:
        print(f"ERROR: Error fetching data: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"ERROR: Error parsing JSON response: {e}")
        raise


if __name__ == "__main__":
    # Test: Get dataset info
    print("TESTING DATA FETCHING")
    print("=" * 60)
    
    info = get_dataset_info()
    print(f"\nTotal Records: {info['total_records']}")
    print(f"\nAvailable Columns ({len(info['columns'])}):")
    for col in info['columns']:
        print(f"  - {col}")
    
    print("\n" + "=" * 60)
    print("Fetching sample data (100 records)...")
    print("=" * 60)
    
    # Fetch small sample for testing
    df = fetch_winnipeg_assessment_data(limit=100)
    print(f"\nData shape: {df.shape}")
    print("\nFirst few rows:")
    print(df.head())