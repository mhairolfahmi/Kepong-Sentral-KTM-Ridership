#============================================================================================================================
# Using load_to_csv to save as csv file
# Using load_to_sql to save to sql database
#============================================================================================================================

import pandas as pd
from sqlalchemy import create_engine
import sqlite3

def load_to_csv(df):
    df = df.to_csv("kepong_sentral",index=False)
    print("successfull load to csv file")

def load_to_sql(df,table_name,conn):
    df.to_sql(table_name,conn, if_exists='replace', index=False)
    print("successfull load to sql")