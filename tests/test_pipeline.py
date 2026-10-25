from pathlib import Path
import pandas as pd
import pytest
from airolytix.train import train
from airolytix.predict import score_example

def test_training_and_scoring(tmp_path):
    rows = []
    for i in range(40):
        label = i % 2
        rows.append({"sensor_1": float(i % 7) + label, "sensor_2": float(i % 5), "sensor_3": float(i % 3), "label": label})
    csv = tmp_path / "data.csv"
    model = tmp_path / "model.joblib"
    pd.DataFrame(rows).to_csv(csv, index=False)
    accuracy = train(csv, model)
    assert 0 <= accuracy <= 1
    assert 0 <= score_example(model, {"sensor_1": 1.0, "sensor_2": 2.0, "sensor_3": 3.0}) <= 1

def test_missing_columns(tmp_path):
    csv = tmp_path / "bad.csv"
    pd.DataFrame({"sensor_1": [1], "label": [0]}).to_csv(csv, index=False)
    with pytest.raises(ValueError, match="Missing required columns"):
        train(csv, tmp_path / "bad.joblib")
