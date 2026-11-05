import pandas as pd

def transform(ktm_df ,ets_df):
    try:
        ktm_df = ktm_df[(ktm_df["origin"]=="Kepong Sentral") | 
                        (ktm_df["destination"]=="Kepong Sentral")]

        ets_df = ets_df[(ets_df["origin"]=="Kepong Sentral") | 
                        (ets_df["destination"]=="Kepong Sentral")]

        ktm_df["service"] = "komuter"

        ets_df["service"] = "ets"

        full_schedule = pd.concat([ktm_df,ets_df], ignore_index=True)
        
        print("successfull transform the data")
        
        return full_schedule

    except Exception as e:
        print(f"Error in data transformation: {type(e).__name__}: {e}")
