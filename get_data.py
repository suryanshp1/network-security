import os
import sys
import json
from dotenv import load_dotenv
import certifi
import pandas as pd
import numpy as np
import pymongo
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

load_dotenv()

MOMGO_DB_URL = os.getenv("MONGO_DB_URL")
ca = certifi.where()

class NetworkDataExtract:
    def __init__(self) -> None:
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e, sys)

    def csv_to_json_converter(self, file_path):
        try:
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records=list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def pushing_data_to_mongodb(self, records, database_name, collection_name):
        try:
            self.database = database_name
            self.collection = collection_name
            self.records = records
            self.mongo_client = pymongo.MongoClient(MOMGO_DB_URL, tlsCAFile=ca)

            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return len(self.records)
        
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
if __name__ == "__main__":
    FILE_PATH = "./Network_Data/NetworkData.csv"
    network_obj=NetworkDataExtract()
    DATABASE = "NetworkDB"
    COLLECTION = "NetworkData"
    records = network_obj.csv_to_json_converter(FILE_PATH)
    number_of_records = network_obj.pushing_data_to_mongodb(records, DATABASE, COLLECTION)
    print(f"Number of records inserted: {number_of_records}")
