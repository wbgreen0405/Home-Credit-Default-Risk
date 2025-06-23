import logging
import numpy as np
import pandas as pd

logger = logging.getLogger(__name__)

def one_hot_encoder(df, nan_as_category=True):
    original_columns = list(df.columns)
    categorical_columns = [col for col in df.columns if df[col].dtype == "object"]
    df = pd.get_dummies(df, columns=categorical_columns, dummy_na=nan_as_category)
    new_columns = [c for c in df.columns if c not in original_columns]
    logger.info(f"One-hot encoded {len(categorical_columns)} columns, {len(new_columns)} new columns.")
    return df, new_columns

