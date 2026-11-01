import pandas as pd

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
    full_schdule = full_service.to_csv("final_schedule", index = False)


ktm_df = read_file(ktm_url)

ets_df = read_file(ets_url)

full_service = transform(ktm_df,ets_df)

full_schedule_kepong_sentral = load_to_csv(full_service)
