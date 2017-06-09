void setup() {
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop() {
  if (Serial.available() > 0)
  {
    char message = Serial.read();
    if (message == 'w')
    {
      blinkChar(message);
    }
    else
    {
      int integer = message- '0';
      blinkInt(integer);
    }
    //Serial.print(Serial.read()- '0');
    
  }
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

void blinkChar(char message)
{
  if (message == 'w')
  {
    for (int a=0; a<5; a++)
    {
      digitalWrite(13, HIGH);
      delay(100);
      digitalWrite(13, LOW);
      delay(100);
    }
    delay(2000);
  }
}

