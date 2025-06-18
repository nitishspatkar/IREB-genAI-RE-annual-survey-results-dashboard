"""Data processing utilities for the dashboard."""

import pandas as pd
import re
from typing import Optional, Union, List
import os

def dedup_column_names(columns: List[str]) -> List[str]:
    """
    Deduplicate column names by adding a suffix for duplicates.
    
    Args:
        columns: List of column names
        
    Returns:
        List of unique column names
    """
    seen = {}
    result = []
    
    for item in columns:
        if item in seen:
            seen[item] += 1
            result.append(f"{item}.{seen[item]}")
        else:
            seen[item] = 0
            result.append(item)
    
    return result

def clean_column_name(col: str) -> str:
    """
    Clean a column name by normalizing all whitespace (including non-breaking spaces) to a single space, and stripping.
    Also removes quotes.
    """
    # Replace non-breaking spaces with regular spaces, then collapse all whitespace to a single space
    cleaned = col.replace('\u00a0', ' ')
    cleaned = re.sub(r'\s+', ' ', cleaned.strip())
    cleaned = cleaned.replace('"', '').replace("'", '')
    return cleaned

def load_single_year_data(data_folder: str, year: int) -> pd.DataFrame:
    """
    Load survey data for a specific year.
    
    Args:
        data_folder: Path to the folder containing data files
        year: Year of the survey data to load
        
    Returns:
        DataFrame containing the survey data
    """
    file_path = os.path.join(data_folder, f"{year}.csv")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file for year {year} not found at {file_path}")
    
    # Read CSV with specific parameters to handle formatting issues
    df = pd.read_csv(
        file_path,
        encoding='utf-8',
        on_bad_lines='skip',  # Skip problematic lines
        low_memory=False,     # Avoid mixed type inference issues
        quoting=1,           # Handle quoted fields
        escapechar='\\',     # Handle escaped characters
    )
    
    # Clean up column names
    df.columns = [clean_column_name(col) for col in df.columns]
    
    # Handle duplicate column names with our own function
    df.columns = dedup_column_names(list(df.columns))
    
    return df

def parse_experience(val: Union[str, float, None]) -> Optional[float]:
    """
    Parse years of experience from various string formats into a numeric value.
    
    Args:
        val: Experience value to parse
        
    Returns:
        Parsed numeric value or None if parsing fails
    """
    if pd.isna(val):
        return None
        
    val = str(val).strip()
    
    # If already a number
    try:
        return float(val)
    except:
        pass
        
    # If range like "5-10"
    match = re.match(r"(\d+)\s*-\s*(\d+)", val)
    if match:
        low, high = map(int, match.groups())
        return (low + high) / 2
        
    # If "10+" or "10 or more"
    match = re.match(r"(\d+)\s*\+|(\d+)\s*or more", val)
    if match:
        return float(match.group(1) or match.group(2))
        
    return None

def process_numeric_column(df: pd.DataFrame, col: str) -> pd.Series:
    """
    Process a numeric column, handling various formats and errors.
    
    Args:
        df: Input DataFrame
        col: Name of the column to process
        
    Returns:
        Series with processed numeric values
    """
    if col == "How many years of professional experience do you have in IT/software engineering?":
        return df[col].apply(parse_experience)
    else:
        return pd.to_numeric(df[col], errors='coerce')

def calculate_completion_rate(df: pd.DataFrame, col: str) -> float:
    """
    Calculate the completion rate for a column.
    
    Args:
        df: Input DataFrame
        col: Name of the column to analyze
        
    Returns:
        Percentage of non-null values
    """
    total = len(df)
    if total == 0:
        return 0.0
    return (df[col].notna().sum() / total) * 100

def get_response_summary(df: pd.DataFrame, col: str) -> dict:
    """
    Get a summary of responses for a column.
    
    Args:
        df: Input DataFrame
        col: Name of the column to analyze
        
    Returns:
        Dictionary containing response statistics
    """
    total_responses = len(df)
    valid_responses = df[col].notna().sum()
    completion_rate = calculate_completion_rate(df, col)
    
    if df[col].dtype in ['int64', 'float64'] or col in ["years_of_experience", "num_sustainability_trainings"]:
        numeric_values = process_numeric_column(df, col)
        return {
            "total_responses": total_responses,
            "valid_responses": valid_responses,
            "completion_rate": completion_rate,
            "mean": numeric_values.mean(),
            "median": numeric_values.median(),
            "min": numeric_values.min(),
            "max": numeric_values.max()
        }
    else:
        value_counts = df[col].value_counts()
        return {
            "total_responses": total_responses,
            "valid_responses": valid_responses,
            "completion_rate": completion_rate,
            "most_common": value_counts.index[0] if not value_counts.empty else None,
            "most_common_count": value_counts.iloc[0] if not value_counts.empty else 0,
            "unique_values": df[col].nunique()
        }

def load_data_file(data_file: str) -> pd.DataFrame:
    """
    Load and preprocess the GenAI RE survey data from a CSV file.
    Cleans column names and handles duplicates.
    Returns a pandas DataFrame.
    """
    if not os.path.exists(data_file):
        raise FileNotFoundError(f"Data file not found at {data_file}")
    df = pd.read_csv(
        data_file,
        encoding='utf-8',
        on_bad_lines='skip',
        low_memory=False,
        quoting=1,
        escapechar='\\',
    )
    df.columns = [clean_column_name(col) for col in df.columns]
    # Optionally handle duplicate columns if needed
    return df

def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Clean column names by removing special characters and standardizing format."""
    # Store original columns for reference
    original_columns = df.columns.tolist()
    
    # Clean each column name
    cleaned_columns = []
    for col in original_columns:
        cleaned_col = clean_column_name(col)
        cleaned_columns.append(cleaned_col)
    
    # Create new DataFrame with cleaned column names
    df_cleaned = df.copy()
    df_cleaned.columns = cleaned_columns
    
    return df_cleaned 