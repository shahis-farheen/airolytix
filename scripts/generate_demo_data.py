"""Generate artificial numeric patterns. NOT human breath or medical evidence."""
from pathlib import Path
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 240
labels = np.repeat([0, 1], n // 2)
rng.shuffle(labels)
features = rng.normal(loc=0, scale=1, size=(n, 3)) + labels[:, None] * np.array([0.7, -0.4, 0.5])
df = pd.DataFrame(features, columns=["sensor_1", "sensor_2", "sensor_3"])
df["label"] = labels
out = Path(__file__).resolve().parents[1] / "data" / "demo_breath.csv"
out.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(out, index=False)
print(f"Created SYNTHETIC demonstration dataset: {out}")
