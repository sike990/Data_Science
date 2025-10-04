import os 
import sys
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from src.logger import logging
from src.exception import CustomException
import pandas as pd


@dataclass
class Dataingestionconfig:
    train_data_path : str=os.path.join("artifacts","train.csv")
    test_data_path : str=os.path.join("artifacts","test.csv")
    raw_data_path : str=os.path.join("artifacts","data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = Dataingestionconfig()
    
    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method")
        try:
            df = pd.read_csv("notebook/data/stud.csv")
            logging.info("Read the dataset as dataframe.")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path) , exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,header=True,index=False)
            logging.info("Saved the raw dataset in artifacts.")

            logging.info("Train test split started.")
            train,test = train_test_split(df,test_size=0.2,random_state = 34)
            train.to_csv(self.ingestion_config.train_data_path,header=True,index=False)
            test.to_csv(self.ingestion_config.test_data_path,header=True,index=False)

            logging.info("Data ingestion completed.")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()