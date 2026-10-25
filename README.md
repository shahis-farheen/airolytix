# airolytix

**Experimental electronic-nose breath-pattern research prototype for COPD screening research.**

> **Research only. Not a medical device, diagnostic test, or clinical screening service.** No COPD detection performance has been established. Synthetic data and demo outputs must never be interpreted as patient results.

## Concept
An ESP32 reads an analog gas-sensor channel, streams measurements over USB serial, and a Python pipeline explores patterns in labelled multichannel breath-sensor features. A Streamlit dashboard demonstrates model output on **synthetic demo data only**.

## Quick start (Python 3.10+)
```bash
python -m venv .venv
# macOS/Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python scripts/generate_demo_data.py
python -m airolytix.train --data data/demo_breath.csv --model models/demo_model.joblib
python -m pytest -q
streamlit run dashboard/app.py
```
The sample data is artificially generated; metrics are illustrative only. No actual breath dataset is provided.

## Hardware
See [hardware setup](docs/HARDWARE_SETUP.md). Firmware provides a **single analog channel example**, not a validated multi-sensor e-nose. Modify pins, circuitry and calibration for your actual sensors. Never connect a 5V analog output directly to an ESP32 ADC pin.

## Architecture
See [architecture](docs/ARCHITECTURE.md) and [validation plan](docs/VALIDATION.md).

## GitHub
Create a repository called `airolytix`, then follow the upload or Git steps below. Do not upload real patient data, secrets, or private medical records.

## Research references
The project reference document supplied literature search topics rather than verified publication metadata:
- [Detection of COPD and Lung Cancer with Electronic Nose using Ensemble Learning Methods](https://scholar.google.com/scholar?q=Detection+of+COPD+and+Lung+Cancer+with+Electronic+Nose+using+Ensemble+Learning+Methods)
- [Diagnostic Potential of Breath Analysis—Focus on Volatile Organic Compounds](https://scholar.google.com/scholar?q=Diagnostic+Potential+of+Breath+Analysis+Focus+on+Volatile+Organic+Compounds)

## License
MIT license for this starter code; not a grant of clinical-use approval.
