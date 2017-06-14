#include <OneWire.h>
#include <DallasTemperature.h>
#include <PID_v1.h>

#define ONE_WIRE_BUS 2
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

int warmtePin = 5;

char terminator = '.';

// Variabelen voor de PID waarden.
double Setpoint, Input, Output;

// Variabelen voor de PID tuning parameters.
double Kp, Ki, Kd;

// Instellen van de PID.
PID dePID(&Input, &Output, &Setpoint, Kp, Ki, Kd, DIRECT);

void setup() {
  Serial.begin(9600);
  sensors.begin();

  pinMode(warmtePin, OUTPUT);

  // PID variabelen initialiseren.
  sensors.requestTemperatures();
  
  Input = sensors.getTempCByIndex(1);
  Setpoint = sensors.getTempCByIndex(0) + 5;
}

void loop() {

  // Handling commands from UI.
  if (Serial.available() > 0)
  {
    String message = Serial.readStringUntil(terminator);
    if (message == "validate")
    {
      Serial.print("valid.");
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
      sensors.requestTemperatures();
      //writeString(String(sensors.getTempCByIndex(0), 2));
      writeString(String("hahah"));
    }
    else if (message == "ti")
    {
      sensors.requestTemperatures();
      //writeString(String(sensors.getTempCByIndex(1), 2)); 
      writeString(String(analogRead(2)));
    }
    else if (message == "i")
    {
      writeString(String(analogRead(3)));
    }
  }
}

void initialize()
{
  
}

void setTempDiffGoal()
{
  
}

void blinkInt(int number) 
{
  for (int a=0; a<number; a++)
  {
    digitalWrite(13, HIGH);
    delay(500);
    digitalWrite(13, LOW);
    delay(500);
  }
}

void writeString(String stringData) { // Used to serially push out a String with Serial.write()
  for (int i = 0; i < stringData.length(); i++)
  {
    Serial.write(stringData[i]);   // Push each char 1 by 1 on each loop pass
  }
  Serial.write(".");
}

