import pandas as pd
import os

def load_data(data_path='data/raw/ethiopia_fi_unified_data.xlsx'):  #data\raw\ethiopia_fi_unified_data.xlsx
    """
    Loads the unified financial inclusion dataset.
    """
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"File not found: {data_path}")
    
    df = pd.read_excel(data_path)
    
    # Convert date columns to datetime objects
    if 'observation_date' in df.columns:
        df['observation_date'] = pd.to_datetime(df['observation_date'])
        
    return df

def load_reference_codes(ref_path='data/raw/reference_codes.xlsx'):
    """
    Loads the reference codes for validation.
    """
    return pd.read_excel(ref_path)