// airolytix — one-channel sensor acquisition EXAMPLE (not clinical hardware).
// IMPORTANT: ESP32 ADC GPIO34 must NEVER receive >3.3V. Use a suitable
// voltage divider/buffer for modules that output 5V. Check board pinout.
// Many gas sensors need warm-up, calibration, safe power, and airflow control.
const int SENSOR_PIN = 34;
const unsigned long SAMPLE_INTERVAL_MS = 500;
unsigned long lastSample = 0;

void setup() {
  Serial.begin(115200);
  analogReadResolution(12);
  Serial.println("milliseconds,adc_raw");
}
void loop() {
  unsigned long now = millis();
  if (now - lastSample >= SAMPLE_INTERVAL_MS) {
    lastSample = now;
    int raw = analogRead(SENSOR_PIN);
    Serial.print(now);
    Serial.print(',');
    Serial.println(raw);
  }
}
