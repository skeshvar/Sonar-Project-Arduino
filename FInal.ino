# include<Servo.h>
int servoPin= 9;
int servoPos= 0; 
int StartPos= 10;
int EndPos= 170;
Servo myServo;
int echo= 11;
int trig= 12;
int numcol = 4;
float col = 4.;
float TravelTime[4];
float FinalTravelTime;
int dt= 100;
int Step= 2;
void setup() 
{
  Serial.begin(2e6);
  myServo.attach(servoPin);  
  myServo.write(servoPos);
  pinMode(echo, INPUT);
  pinMode(trig, OUTPUT);
  delay(2000);
}

void loop() 
{
  for(servoPos= StartPos; servoPos<EndPos; servoPos+= Step)
  {
    myServo.write(servoPos);
    for(int i=0; i<col; i++)
    {
      digitalWrite(trig, LOW);
      delayMicroseconds(5);
      digitalWrite(trig, HIGH);
      delayMicroseconds(5);
      digitalWrite(trig, LOW);
      TravelTime[i] = pulseIn(echo, HIGH)/2;
    }
    FinalTravelTime = 0;
    for(int i=0; i<numcol; i++)
    {
      FinalTravelTime = FinalTravelTime + TravelTime[i];
    }
    Serial.print(servoPos);
    Serial.print(", ");
    Serial.println(FinalTravelTime*340/(10000*col));
    delay(dt);
  }
  for(servoPos=EndPos; servoPos> StartPos; servoPos-= Step)
  {
    myServo.write(servoPos);
    for(int i=0; i<col; i++)
    {
      digitalWrite(trig, LOW);
      delayMicroseconds(5);
      digitalWrite(trig, HIGH);
      delayMicroseconds(5);
      digitalWrite(trig, LOW);
      TravelTime[i] = pulseIn(echo, HIGH)/2;
    }
    FinalTravelTime = 0;
    for(int i=0; i<numcol; i++)
    {
      FinalTravelTime = FinalTravelTime + TravelTime[i];
    }
    Serial.print(servoPos);
    Serial.print(", ");
    Serial.println(FinalTravelTime*340/(10000*col));
    delay(dt);
  }
  
}
