import pandas as pd
import sqlite3

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


ktm_df = read_file(ktm_url)

ets_df = read_file(ets_url)

full_service = transform(ktm_df,ets_df)

load_to_csv(full_service)

load_to_db(full_service,conn, table_name)

query = f"select * from {table_name}"

run_query(query,conn)

query = f"select service, count(*) FROM {table_name} GROUP BY service"

run_query(query,conn)

conn.close()






