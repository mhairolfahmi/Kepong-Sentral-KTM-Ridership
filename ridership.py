import pandas as pd

ktm_url = "https://storage.data.gov.my/transportation/ktmb/komuter_2026.parquet"

ets_url = "https://storage.data.gov.my/transportation/ktmb/ets_2026.parquet"

def read_file(url):
    df=pd.read_parquet(url)
    return df

ktm_df = read_file(ktm_url)

ets_df = read_file(ets_url)