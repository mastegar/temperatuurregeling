#include <PID_v1.h>
#include <DallasTemperature.h>
#include <OneWire.h>

#define ONE_WIRE_BUS 2
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

// Variabelen voor de PID waarden.
double Setpoint, Input, Output;

// Variabelen voor de PID tuning parameters.
double Kp = 150;
double Ki = 3.5;
double Kd = 20;

// Instellen van de PID.
PID dePID(&Input, &Output, &Setpoint, Kp, Ki, Kd, DIRECT);

int e = 0;

void setup() {
  Serial.begin(9600);
  sensors.begin();

  pinMode(5, OUTPUT);

  // PID variabelen initializeren.
  sensors.requestTemperatures();
  Input = sensors.getTempCByIndex(1);
  Setpoint = sensors.getTempCByIndex(0) + 8;

  // PID aanzetten.
  dePID.SetMode(AUTOMATIC);
}

void loop() {

  // Temperaturen ophalen.
  sensors.requestTemperatures();

  Input = sensors.getTempCByIndex(1);
  dePID.Compute();
  Serial.print(Output);

  // Data naar de serial sturen.
  Serial.print("Temperatuur binnen: ");
  Serial.println(sensors.getTempCByIndex(1));
  Serial.print("Temperatuur buiten: ");
  Serial.println(sensors.getTempCByIndex(0));
  Serial.print("Verschil: ");
  Serial.println(sensors.getTempCByIndex(1) - sensors.getTempCByIndex(0));
  Serial.print("Outputwaarde: ");
  Serial.println(Output);
  Serial.println("");
  //Serial.println(Setpoint - sensors.getTempCByIndex(1));
  
  // Verwarmingselement aansturen.
  analogWrite(5, Output);

  delay(1000);
}
