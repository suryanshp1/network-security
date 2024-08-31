import os
import sys
from networksecurity.constant.training_pipeline import SAVED_MODEL_DIR, MODEL_FILE_NAME
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

class NetworkModel:
    def __init__(self, preprocessor, model) -> None:
        try:
            self.preprocessor = preprocessor
            self.model = model
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def predict(self, X):
        try:
            transformed_feature = self.preprocessor.transform(X)
            return self.model.predict(transformed_feature)
        except Exception as e:
            raise NetworkSecurityException(e, sys)

class ModelResolver:
    def __init__(self, model_dir: str = SAVED_MODEL_DIR) -> None:
        try:
            
            self.model_dir = model_dir
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def get_best_model_path(self) -> str:
        try:
            timestamps = list(map(int, os.listdir(self.model_dir)))
            timestamp = max(timestamps)
            return os.path.join(self.model_dir, f"{timestamp}", MODEL_FILE_NAME)
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def is_model_exists(self) -> bool:
        try:
            if not os.path.exists(self.model_dir):
                return False
            
            timestamps = os.listdir(self.model_dir)
            if len(timestamps) == 0:
                return False
            
            latest_model_path = self.get_best_model_path()

            return os.path.exists(latest_model_path)
        except Exception as e:
            raise NetworkSecurityException(e, sys)