import requests
import pandas as pd
import json


host = 'localhost'
port = '5000'
url = f'http://{host}:{port}/invocations'
headers = {'Content-Type': 'application/json',}

target_col = 'shot_made_flag'
df_prod = pd.read_parquet("../data/raw/dataset_kobe_prod.parquet")

#print(df_prod)

inference_request = {
    "dataframe_split": json.loads(df_prod.drop(target_col,axis=1).to_json(orient='split'))
}
r = requests.post(url=url, headers=headers, json=inference_request)



print(r)