import pandas as pd
from src.features import one_hot_encoder

def test_one_hot_encoder_basic():
    df = pd.DataFrame({
        'A': ['a', 'b', 'a'],
        'B': [1, 2, 3]
    })
    df_encoded, new_cols = one_hot_encoder(df)
    assert 'A_a' in df_encoded.columns
    assert 'A_b' in df_encoded.columns
    assert len(new_cols) == 3  # A_a, A_b, A_nan (if nan_as_category=True)
    assert all(col in df_encoded.columns for col in new_cols)
