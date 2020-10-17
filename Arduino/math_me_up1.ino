#include <LiquidCrystal.h>

LiquidCrystal lcd(13, 12, 5, 4, 3, 2);

int decimal(int a,int b,int c,int d){
  int dec = (8*a)+(4*b)+(2*c)+(1*d);
  return dec;
}

int octal(int a,int b,int c,int d){
  int oct = (a*10)+(4*b)+(2*c)+(1*d);
  return oct;
}

char hexadecimal(int a,int b,int c,int d){
  int bn = (8*a)+(4*b)+(2*c)+(1*d);
  char ch;
  if(bn<10)
  {
    ch = (char)(bn+48);
  }
  else
  {
    ch = (char)(bn+55);
  }
  return ch;
}

void setup() {
  lcd.begin(16, 2);
  pinMode(8, INPUT);
  pinMode(9, INPUT);
  pinMode(10, INPUT);
  pinMode(11, INPUT);
}

void loop() {
  int d1, d2, d3, d4, decim, octa;
  char hexadecim;
  lcd.setCursor(0, 0);
  lcd.print("Conversions:");
  d1 = digitalRead(11);
  d2 = digitalRead(10);
  d3 = digitalRead(9);
  d4 = digitalRead(8);
  lcd.setCursor(0, 1);
  lcd.print(d1);
  lcd.setCursor(1, 1);
  lcd.print(d2);
  lcd.setCursor(2, 1);
  lcd.print(d3);
  lcd.setCursor(3, 1);
  lcd.print(d4);
  decim = decimal(d1,d2,d3,d4);
  lcd.setCursor(6, 1);
  lcd.print(decim);
  octa = octal(d1,d2,d3,d4);
  lcd.setCursor(10, 1);
  lcd.print(octa);
  hexadecim = hexadecimal(d1,d2,d3,d4);
  lcd.setCursor(15, 1);
  lcd.print(hexadecim);
  delay(3000);
  lcd.clear();
}
 