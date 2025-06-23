import logging
import gc
import time
from contextlib import contextmanager
from lightgbm import LGBMClassifier
from sklearn.model_selection import KFold
from sklearn.metrics import roc_auc_score
import pandas as pd
from src.features import one_hot_encoder
from src.utils import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

@contextmanager
def timer(title):
    t0 = time.time()
    yield
    logger.info(f"{title} - done in {time.time() - t0:.0f}s")

def main():
    logger.info("Starting Home Credit Default Risk pipeline.")
    # Example: Load and preprocess data
    with timer("Feature Engineering"):
        df = pd.read_csv("data/application_train.csv")
        df, new_cols = one_hot_encoder(df)
        logger.info(f"Data shape after encoding: {df.shape}")
    # Modeling, cross-validation, results...
    logger.info("Pipeline complete.")

if __name__ == "__main__":
    main()
