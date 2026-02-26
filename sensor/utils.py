import pandas as pd
import numpy as np
import logging 
import json
from sensor.config import mongo_client
def deump_csv_file_to_mongodb_collection(file_path:str,database_name:str,collection_name:str)->None:
    try:
<<<<<<< HEAD
        df=pd.Categoricalread_csv(file_path)
        df.reshape_index(drop=True,Inplace=True)
        json_records=list(json.loads(df.T.to_json()).values())
=======
        df = pd.read_csv(file_path)
        df.reset_index(drop=True, inplace=True)
        json_records = list(json.loads(df.T.to_json()).values())
>>>>>>> 3d86508f95b2fa2e912653e71d170582ed447b80
        mongo_client[database_name][collection_name].insert_many(json_records)

    except Exception as e:
        print(e)