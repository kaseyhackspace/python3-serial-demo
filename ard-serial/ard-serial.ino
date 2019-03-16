
String input = "";
int index = 0;
float celsius = 0;
float fahrenheit = 0;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  if(Serial.available() > 0){
    input = Serial.readString();
    
    if(input.equals("1")){
      index++;

      celsius = random(50);
      fahrenheit = (celsius*1.8)+32;
      //prints str to serial
      Serial.print(index);
      Serial.print(',');
      Serial.print(celsius);
      Serial.print(',');
      Serial.println(fahrenheit);
      
    } // if equal to 1
    else{
      
      Serial.println("-1");
    } // else
  } // if serial.available
}// loop()
