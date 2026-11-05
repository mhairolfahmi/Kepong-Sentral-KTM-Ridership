from extraction import read_file, quality_check
from transform import transform
from load_data import load_to_csv,load_to_sql
import sqlite3

print("process starting.....")
ktm_url = "https://storage.data.gov.my/transportation/ktmb/komuter_2026.parquet"

ets_url = "https://storage.data.gov.my/transportation/ktmb/ets_2026.parquet"

# extract
print("Extracting Phase Starting...")
df_ktm = read_file(ktm_url)

df_ets = read_file(ets_url)

# data validation
print("Data Validation Phase Starting...")
quality_check(df_ktm,"komuter")

quality_check(df_ets,"ETS")

# data transformation
print("Trnasformation Phase Starting...")
full_schedule = transform(df_ktm, df_ets)

# load to parquet
print("Loading data to csv file....")
load_to_csv(full_schedule)

# load to sql
print("Loading data to sql database")
table_name = "kepong_sentral_ridership"
conn = sqlite3.connect('kepong_sentral.db')

load_to_sql(full_schedule,table_name,conn)

print("Process Complete")