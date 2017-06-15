#include <Wire.h>
#include <Adafruit_INA219.h>
#include <OneWire.h>
#include <DallasTemperature.h>
#include <PID_v1.h>
#define ONE_WIRE_BUS 2

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);
Adafruit_INA219 stroomSensor;

int warmtePin = 5;
bool gedaan;

char terminator = '/';

double Setpoint, Input, Output;     // Variabelen voor de PID waarden.
double Kp, Ki, Kd;                  // Variabelen voor de PID tuning parameters.

// Instellen van de PID.
PID dePID(&Input, &Output, &Setpoint, Kp, Ki, Kd, DIRECT);

void setup() {
  Serial.begin(9600);
  sensors.begin();
  stroomSensor.begin();
  dePID.SetMode(AUTOMATIC);

  pinMode(warmtePin, OUTPUT);
}

void loop() {
  // Handling commands from UI.
  if (Serial.available() > 0)
  {
    String message = Serial.readStringUntil(terminator);
    if (message == "validate")
    {
      Serial.print("valid/");
    }
    else if (message == "iw") //Instellen ingestelde waarde
    {
      String value = Serial.readStringUntil(terminator);
      Setpoint = value.toFloat();
    }
    else if (message == "kp") //Instellen Kp constante
    {
      String value = Serial.readStringUntil(terminator);
      Kp = value.toFloat();
    }
    else if (message == "ki") //Instellen Ki constante
    {
      String value = Serial.readStringUntil(terminator);
      Ki = value.toFloat();
    }
    else if (message == "kd") //Instellen Kd constante
    {
      String value = Serial.readStringUntil(terminator);
      Kd = value.toFloat();
    }
    else if (message == "tu") //Opvragen buitentemperatuur
    {
      writeString(String(sensors.getTempCByIndex(0), 1));
    }
    else if (message == "ti")
    {
      writeString(String(sensors.getTempCByIndex(1), 1)); 
    }
    else if (message == "i")
    {
      float vermogen = stroomSensor.getCurrent_mA()/1000 * stroomSensor.getBusVoltage_V();
      writeString(String(vermogen, 1));
    }
    else if (message == "comp")
    {
      compute();
      Serial.print("fin/");
    }
    else if (message == "start")
    {
      dePID.SetTunings(Kp, Ki, Kd);
      Serial.print("start/");
    }
  }
}

void compute()
{
  sensors.requestTemperatures();
  Input = sensors.getTempCByIndex(1);
  gedaan = dePID.Compute();
  analogWrite(warmtePin, Output);
}

void blinkInt(int number) 
{
  for (int a=0; a<number; a++)
  {
    digitalWrite(13, HIGH);
    delay(100);
    digitalWrite(13, LOW);
    delay(100);
  }
}

void writeString(String stringData) { // Used to serially push out a String with Serial.write()
  for (int i = 0; i < stringData.length(); i++)
  {
    Serial.write(stringData[i]);   // Push each char 1 by 1 on each loop pass
  }
  Serial.write("/");
}

