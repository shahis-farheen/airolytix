"""Illustrative synthetic model scoring, NOT COPD prediction."""
import joblib
import pandas as pd

def score_example(model_path, values):
    bundle = joblib.load(model_path)  # Only load locally created, trusted joblib files.
    if not bundle.get("demo_only", False):
        raise ValueError("This dashboard only accepts demonstration models")
    frame = pd.DataFrame([values], columns=bundle["features"])
    return float(bundle["pipeline"].predict_proba(frame)[0, 1])
