#============================================================================================================================
# Using read_file, we can extract CSV data directly from the data.gov.my website.
# Using quality_check, we can validate the extracted data and identify potential errors before proceeding with data cleaning.
#============================================================================================================================
import pandas as pd 
from urllib.error import HTTPError, URLError

def read_file(url):
    try:
        df=pd.read_parquet(url)
        print(f"successful read the file {url}")
        return df
        

    except HTTPError as e:
        print(f"HTTP error {e.code} for {url}")
    except URLError as e:
        print(f"Cannot reach {url}: {e.reason}")
    except ImportError:
        print(f"Missing parquet engine: run 'pip install pyarrow'")
    except Exception as e:
        print(f"Unexcpected error: {type(e).___name___}: {e}")

def quality_check(df,dataset_name):
    # check data 
    if df is None or df.empty:
        raise ValueError(f"{dataset_name}: No Data Avalaible")
    else:
        print(f"{dataset_name}: data is okay")

    # check for columns
    required_columns =["date","origin","destination"]

    missing_columns =[ col for col in required_columns
                      if col not in df.columns]

    if missing_columns: 
        raise KeyError(f"{dataset_name} have missing columns {missing_columns}")
    else:
        print(f"{dataset_name}: all required columns found")

    # check for null values
    null_values = df.isnull().sum()

    column_with_null =[]

    for col in df.columns:
        if null_values[col]>0:
            column_with_null.append(col)
            print(f"{dataset_name}: column'{col}' has {null_values[col]} null values")
    
    if len(column_with_null)==0:
            print(f"{dataset_name}: no null values")

    # check duplicates
    duplicates = df.duplicated().sum()

    if duplicates >0:
        print(f"{dataset_name}: found {duplicates} duplicate rows")
    else:
        print(f"{dataset_name}: no duplicate rows")

    print(f"{dataset_name}: all quality checks passed")

    return True
    



