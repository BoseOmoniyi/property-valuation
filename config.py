"""
Configuration for Winnipeg Property Valuation Model
"""

# ===== REPRODUCIBILITY =====
RANDOM_STATE = 42

# ===== API CONFIGURATION =====
WINNIPEG_API_URL = "https://data.winnipeg.ca/resource/d4mq-wa44.json"
WINNIPEG_DATASET_ID = "d4mq-wa44"
API_BATCH_SIZE = 50000
API_TIMEOUT = 30

# ===== DATA PATHS =====
RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"
MODEL_DIR = "models"
RESULTS_DIR = "results"

# ===== DATA PROCESSING =====
# Train/test split
TEST_SIZE = 0.2
VALIDATION_SIZE = 0.2

# Missing value threshold (drop columns with > X% missing)
MISSING_THRESHOLD = 0.5

# Outlier detection (IQR method)
OUTLIER_IQR_MULTIPLIER = 1.5

# ===== MODEL FEATURES =====
# Features for baseline model (will be updated after data exploration)
BASELINE_FEATURES = ['Total.Living.Area.Num', 'Assessed.Land.Area.Num']
TARGET_VARIABLE = 'Total.Assessed.Value.Num'

# ===== MODEL PARAMETERS =====

# Random Forest
RANDOM_FOREST_PARAMS = {
    'n_estimators': 100,
    'max_depth': 20,
    'min_samples_split': 5,
    'min_samples_leaf': 2,
    'max_features': 'sqrt',
    'random_state': RANDOM_STATE,
    'n_jobs': -1,
    'verbose': 0
}

# XGBoost
XGBOOST_PARAMS = {
    'n_estimators': 100,
    'max_depth': 6,
    'learning_rate': 0.1,
    'subsample': 0.8,
    'colsample_bytree': 0.8,
    'random_state': RANDOM_STATE,
    'n_jobs': -1,
    'verbosity': 0
}

# ===== CROSS-VALIDATION =====
CV_FOLDS = 5
CV_SCORING = 'neg_mean_squared_error'

# ===== MODEL VERSION =====
MODEL_VERSION = '1.0.0'