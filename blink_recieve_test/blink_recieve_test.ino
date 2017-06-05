void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  if (Serial.available() > 0)
  {
    int message = Serial.read()- '0';
    //Serial.print(Serial.read()- '0');
    blink(message);
  }
}

void blink(int number) 
{
  for (int a=0; a<number; a++)
  {
    digitalWrite(13, HIGH);
    delay(500);
    digitalWrite(13, LOW);
    delay(500);
  }
}
