"""Train an illustrative model on explicitly labelled data; no medical validation."""
import argparse
from pathlib import Path
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from .data import FEATURES, TARGET

def train(data_path, model_path):
    df = pd.read_csv(data_path)
    missing = set(FEATURES + [TARGET]) - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    if df[TARGET].isna().any() or not set(df[TARGET].unique()).issubset({0, 1}) or df[TARGET].nunique() != 2:
        raise ValueError("Labels must contain both classes 0 and 1 without missing values")
    X_train, X_test, y_train, y_test = train_test_split(
        df[FEATURES], df[TARGET], test_size=0.25, random_state=42, stratify=df[TARGET]
    )
    model = make_pipeline(SimpleImputer(strategy="median"), StandardScaler(), LogisticRegression(max_iter=1000, random_state=42))
    model.fit(X_train, y_train)
    accuracy = accuracy_score(y_test, model.predict(X_test))
    Path(model_path).parent.mkdir(parents=True, exist_ok=True)
    joblib.dump({"pipeline": model, "features": FEATURES, "demo_only": True}, model_path)
    print(f"Synthetic/example holdout accuracy: {accuracy:.3f} (NOT clinical accuracy)")
    print(f"Saved model: {model_path}")
    return accuracy

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", default="data/demo_breath.csv")
    parser.add_argument("--model", default="models/demo_model.joblib")
    args = parser.parse_args()
    train(args.data, args.model)
