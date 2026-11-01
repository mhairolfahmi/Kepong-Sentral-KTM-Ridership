import pandas as pd
import sqlite3
from datetime import datetime 

table_name = "kepong_sentral_ridership"
conn = sqlite3.connect('kepong_sentral_ridership.db')

ktm_url = "https://storage.data.gov.my/transportation/ktmb/komuter_2026.parquet"

ets_url = "https://storage.data.gov.my/transportation/ktmb/ets_2026.parquet"

def read_file(url):
    df=pd.read_parquet(url)
    return df

def transform(ktm_df ,ets_df):
    ktm_df = ktm_df[(ktm_df["origin"]=="Kepong Sentral") | 
                    (ktm_df["destination"]=="Kepong Sentral")]

    ets_df = ets_df[(ets_df["origin"]=="Kepong Sentral") | 
                    (ets_df["destination"]=="Kepong Sentral")]

    ktm_df["service"] = "komuter"

    ets_df["service"] = "ets"

    full_service = pd.concat([ktm_df,ets_df], ignore_index=True)

    return full_service

def load_to_csv(full_service):
    full_schdule = full_service.to_csv("full_ridership_kepong_sentral", index = False)

def load_to_db(full_service,conn,table_name):
    full_service.to_sql(table_name,conn, if_exists='replace', index=False)

def run_query(query,conn):
    print(query)
    query_output = pd.read_sql(query,conn)
    print(query_output)

def log_progress(message): 
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open("./etl_project_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')


log_progress('Preliminaries complete. Initiating ETL process')

ktm_df = read_file(ktm_url)

ets_df = read_file(ets_url)

log_progress('Data extraction complete. Initiating Transformation process')

full_service = transform(ktm_df,ets_df)

log_progress('Data transformation complete. Initiating loading process')

load_to_csv(full_service)

log_progress('Data saved to CSV file')

log_progress('SQL Connection initiated.')

load_to_db(full_service,conn, table_name)

log_progress('Data loaded to Database as table. Running the query')

log_progress('Query: show full ridership table')

query = f"select * from {table_name}"

run_query(query,conn)

log_progress('Query: number of ridership by service')

query = f"select service, count(*) FROM {table_name} GROUP BY service"

run_query(query,conn)

log_progress('Process Complete.')

conn.close()






