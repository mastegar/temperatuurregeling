char terminator = '.';

bool pinStatus = 0;

void setup() {
  Serial.begin(9600);

}

void loop() {
  /*
  while (true)
  {
    Serial.write("bi-24");
    delay(1000);
    Serial.write("bu-2.");
    delay(1000);
  }
  */
  
  if (Serial.available() > 0)
  {
    String message = Serial.readStringUntil(terminator);
    Serial.println(message);
    if (message == "validate")
    {
      //blinkk();
      Serial.write("valid");
    }
  }
  

}

void switchh()
{
  if (!pinStatus)
  {
    digitalWrite(13, HIGH);
    pinStatus = 1;
  }
  else
  {
    digitalWrite(13, LOW);
    pinStatus = 0;
  }
}

void blinkk()
{
  for (int a=0; a<10; a++)
  {
    digitalWrite(13, HIGH);
    delay(100);
    digitalWrite(13, LOW);
    delay(100);
  }
  
}

