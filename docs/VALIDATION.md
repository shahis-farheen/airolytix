# Validation roadmap

The included generated dataset has no clinical meaning. Before making screening claims:

- Specify the exact sensors, breath-collection protocol, environmental controls and safety requirements.
- Obtain ethical approval and informed consent for any human-subject data collection.
- Label cases using clinician-confirmed reference tests (e.g., spirometry as appropriate).
- Separate participants (not just rows) across train/validation/test; use an independent external test set.
- Report sensitivity, specificity, AUROC, confidence intervals, calibration, subgroup performance and failure cases.
- Test sensor drift, humidity, temperature, confounders, repeatability and out-of-distribution inputs.
- Assess privacy, cybersecurity, clinical workflow, regulatory requirements and prospective utility.

Do not use this prototype for medical decisions.
