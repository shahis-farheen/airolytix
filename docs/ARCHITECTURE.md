# System architecture

**Proposed future system:** Exhaled breath -> controlled sampling chamber -> calibrated multichannel gas sensors -> ESP32 -> preprocessing/feature extraction -> trained classifier -> research interface.

**Implemented in this starter:** one-channel ESP32 ADC serial example; independent synthetic 3-feature Python training pipeline; synthetic dashboard. These pieces are NOT yet an integrated real-breath screening instrument.

Real sensor deployment needs circuit specifications, baseline/purge cycles, sample timing, sensor drift compensation, subject-level dataset splitting, and clinical evaluation.
