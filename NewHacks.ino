int H2O = 0;
int redPin = 9;
int greenPin = 10;
int bluePin = 11;
int value;

void setup(){
  pinMode(H2O, INPUT);
  pinMode(redPin, OUTPUT);
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  Serial.begin(115200);
}

void loop(){

  value = analogRead(H2O);
  
  if(value <= 400){
    digitalWrite(redPin,HIGH);
    digitalWrite(greenPin, LOW);
    digitalWrite(bluePin, LOW);
    Serial.println(value);
    delay(1000);
  }
  else if(value > 400 && value <= 660) {
    digitalWrite(redPin,LOW);
    digitalWrite(greenPin, HIGH);
    digitalWrite(bluePin, LOW);
    Serial.println(value);
    delay(1000);
  }
  else {
    digitalWrite(redPin, LOW);
    digitalWrite(greenPin, LOW);
    digitalWrite(bluePin, HIGH);
    Serial.println(value);
    delay(1000);  
  }
}
