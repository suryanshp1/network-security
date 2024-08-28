import os
import sys
import numpy as np
import pandas as pd

"""
defining common constant variable for the training pipeline
"""

TARGET_COLUMN: str = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "Artifacts"
FILE_NAME: str = "NetworkData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

PREPROCESSING_OBJECT_FILE_NAME: str = "preprocessing.pkl"
MODEL_FILE_NAME: str = "model.pkl"
SCHEMA_FILE_PATH: str = os.path.join("data_schema", "schema.yaml")
SCHEMA_DROP_COLS: str = "drop_columns"

SAVED_MODELS_DIR = os.path.join("saved_models")
"""
Data ingestion related constants start with DATA_INGESTION VAR name
"""

DATA_INGESTION_COLLECTION_NAME: str = "NetworkData"
DATA_INGESTION_DATABASE_NAME: str = "NetworkDB"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.2

"""
Data validation related constants start with DATA_VALIDATION VAR name
"""
DATA_VALIDATION_DIR_NAME: str = "data_validation"
DATA_VALIDATION_VALID_DIR: str = "validated"
DATA_VALIDATION_INVALID_DIR: str = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR: str = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME: str = "report.yaml"

"""
Data transformation related constants start with DATA_TRANSFORMATION VAR name
"""


"""
Model trainer related constants start with MODEL_TRAINER VAR name
"""