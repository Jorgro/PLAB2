

const int buttonPin = 2;
const int ledPinRed = 5;
const int ledPinGreen = 7;


int buttonState = 0;     // current state of the button
int lastButtonState = 0; // previous state of the button
int startPressed = 0;    // the time button was pressed
int endPressed = 0;      // the time button was released
int timeHold = 0;        // the time button was hold
int timeReleased = 0;    // the time button was released
bool start = false;

void setup() {
  
  pinMode(ledPinRed, OUTPUT);
  pinMode(ledPinGreen, OUTPUT);
  pinMode(buttonPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  buttonState = digitalRead(buttonPin);
  
  if (buttonState != lastButtonState) { // button state changed
     updateState();
  }

  lastButtonState = buttonState; 
  

}

void updateState() {
  
  // the button was just pressed
  if (buttonState == HIGH) {
      
      startPressed = millis();
      timeReleased = startPressed - endPressed;
      start = true;

      if (timeReleased >= 50 && timeReleased < 300) {
          Serial.print("0");
          digitalWrite(ledPinRed, HIGH);
          digitalWrite(ledPinGreen, LOW);
      }

      if (timeReleased >= 300 && timeReleased < 3000) {
          Serial.print("1"); 
          digitalWrite(ledPinGreen, HIGH);
          digitalWrite(ledPinRed, LOW);
          
      }

      if (timeReleased >= 3000) {
          Serial.print("5");
          start = false;
      }

  // the button was just released
  } else {
      endPressed = millis();
      timeHold = endPressed - startPressed;

      if (timeHold >= 500 && timeHold < 2100) {
          Serial.print("3"); 
      }
      if (timeHold >= 2100 && start) {
          Serial.print("4"); 
      } 


  }
}
