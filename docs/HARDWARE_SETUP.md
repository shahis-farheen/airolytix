# Hardware setup (example only)

1. Identify your exact ESP32 board, sensor module model, operating voltage and analog output limits.
2. Connect sensor ground to ESP32 ground. Provide the sensor's rated power supply separately as required.
3. Connect a **conditioned, 0–3.3V maximum** analog signal to GPIO34; NEVER connect a 5V output directly.
4. Open `firmware/esp32_sensor/esp32_sensor.ino` in Arduino IDE with the ESP32 board package installed.
5. Select your board and port, upload, and open Serial Monitor at 115200 baud.
6. Observe CSV columns `milliseconds,adc_raw`. These raw counts are not VOC concentrations.

**Caution:** MQ-type sensors may use heaters, consume significant current, respond to multiple gases, and need long warm-up and calibration. Do not connect a person's breath to electronics without an appropriate hygienic sampling system, safety review and research approvals. A single channel is insufficient to demonstrate the proposed e-nose array.
