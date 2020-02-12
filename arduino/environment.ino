#include "DHT.h"

#define DHTPIN 2     // Digital pin connected to the DHT sensor
#define DHTTYPE DHT11   // DHT 11


int motorPin = 10;   //电机驱动管脚D3
int motorhighSpeed = 200;     //电机转速变量
float temp_val=30.0;

String datas="";
String datas_temp="";

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);   
  dht.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  
  lightsensor();
  //delay(1000);
  dhtsersor();
  datas=datas_temp;
  //Serial.println(datas);
  delay(3000);   

}

void serialEvent()
{
   while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
     Serial.println(datas);
    }
  } 
}

void issetmotor(float val)
{
  /*
  if (val>temp_val)
  {
    setmotor(1);
  }
  */
  setmotor(int(val));
}

void setmotor(int val)
{
  int motorSpeed = 0;
  if (val > 25)
  {
    motorSpeed = motorhighSpeed;
    datas_temp=datas_temp+"\"motor\": \"1\"";
    //Serial.print(" 1");
  }
  else
  {
    //Serial.print(" 0");
    datas_temp=datas_temp+"\"motor\": \"0\"";
  }
   //analogWrite(motorPin, motorSpeed);  
   analogWrite(motorPin, motorSpeed); 
   datas_temp=datas_temp+"}"; 
}

void lightsensor()
{
  int input;
  input=analogRead(0);   //读取A0脚的输入值
  datas_temp = "{\"light\":\"" + String(input);
  //Serial.print(datas_temp);
  setenLED(input);
}

void setenLED(int val)
{
  if(val<200)
  {
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    datas_temp=datas_temp+"\",\"LED\": \"1\"";
    //Serial.print(" 1 ");
  }
  else
  {
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
    datas_temp=datas_temp+"\",\"LED\": \"0\"";
    //Serial.print(" 0 ");
  }
    
}

void dhtsersor()
{
   float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  datas_temp=datas_temp+",\"Humidity\": \""+h+"\",\"Temperature\": \""+t+"\",";

  setmotor(int(t));
 /*
  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C "));
  

  

  Serial.print(f);
  Serial.print(F("°F  Heat index: "));
  Serial.print(hic);
  Serial.print(F("°C "));
  Serial.print(hif);
  Serial.println(F("°F"));
  */
}
