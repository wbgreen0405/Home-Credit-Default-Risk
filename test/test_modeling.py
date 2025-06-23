import pandas as pd
from src.modeling import timer

def test_timer_context_manager(caplog):
    with timer("test step"):
        x = 1 + 1
    assert any("test step - done in" in rec.message for rec in caplog.records)
