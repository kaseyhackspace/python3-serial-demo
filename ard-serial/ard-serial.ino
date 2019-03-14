
String input = "";
int index = 0;
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
      Serial.print(index);
      Serial.print(',');
      Serial.print(random(50));
      
    }
    else{
      
      Serial.print("-1");
    }
  }
}
