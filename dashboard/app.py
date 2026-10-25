"""Synthetic demonstration UI. Never enter patient measurements."""
from pathlib import Path
import sys
import streamlit as st

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from airolytix.data import FEATURES
from airolytix.predict import score_example

st.set_page_config(page_title="airolytix | Research demo")
st.title("airolytix — synthetic breath-pattern demo")
st.error("RESEARCH DEMO ONLY — not a COPD test, diagnosis, or clinical screening tool.")
st.write("Enter made-up sensor feature values to explore an illustrative machine-learning pipeline. Do not enter patient data.")
values = {feature: st.number_input(feature, value=0.0, step=0.1) for feature in FEATURES}
model_path = ROOT / "models" / "demo_model.joblib"
if st.button("Run synthetic demo"):
    if not model_path.exists():
        st.warning("Generate demo data and train the demo model first. See README.md.")
    else:
        try:
            score = score_example(model_path, values)
            st.metric("Example class-1 model score (synthetic)", f"{score:.1%}")
            st.caption("This number is not a COPD probability or medical result.")
        except Exception as exc:
            st.error(f"Could not score the example: {exc}")
