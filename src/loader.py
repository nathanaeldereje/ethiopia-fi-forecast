import pandas as pd
import os

def load_data(data_path, sheet_name=0):
    """
    Loads an Excel file.
    Args:
        data_path (str): Path to file.
        sheet_name (str or int): Sheet name or index (default 0 for first sheet).
    """
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"File not found: {data_path}")
    
    # Load the specific sheet (defaults to first sheet if not specified)
    df = pd.read_excel(data_path, sheet_name=sheet_name)
    
    # Convert date columns to datetime objects if they exist
    if 'observation_date' in df.columns:
        df['observation_date'] = pd.to_datetime(df['observation_date'])
        
    return df

def load_reference_codes(ref_path):
    """
    Helper to specifically load reference codes.
    """
    return load_data(ref_path, sheet_name=0)