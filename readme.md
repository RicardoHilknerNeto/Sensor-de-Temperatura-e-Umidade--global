## Codigo:
// Carrega a Biblioteca LiquidCrystal
#include <LiquidCrystal.h>

// Define os pinos que serão utilizados para ligação ao display
LiquidCrystal LCD(12,11,5,4,3,2);

// Variáveis

int SensorTempPino=0;
int SensorUmidPino=1;
int porcem=0;


// Define o pino 8 para o alerta de temperatura baixa
int AlertaTempBaixa=10;
int AlertaTempNormal=9;
int AlertaTempAlta=8;

// Define temperatura baixa como abaixo de zero grau Celsius
int TempBaixa=0;
// Define temperatura alta como acima de 40 graus Celsius
int TempAlta=40;

void setup() 
{
  // Informa se os pinos dos LEDs são de entrada ou saída
  pinMode(AlertaTempBaixa, OUTPUT);
  pinMode(AlertaTempNormal, OUTPUT);
  pinMode(AlertaTempAlta, OUTPUT);
	
  // Define LCD 16 colunas por 2 linhas
  LCD.begin(16,2);
  
  //Posiciona o cursor na coluna 0, linha 0;
  LCD.setCursor(0,0);
  
  // Imprime a mensagem no LCD
  LCD.print("Temper.:");
  
  // Imprime a mensagem no LCD
  LCD.print("Umidad.:");
  
  // Muda o cursor para a primeira coluna e segunda linha do LCD
  LCD.setCursor(0,1);
  
  // Imprime a mensagem no LCD
  LCD.print("      C      ");
  
  // Imprime a mensagem no LCD
  LCD.setCursor(14,1);
  LCD.print("%");
}

void loop()
{
   // Faz a leitura da tensao no Sensor de Temperatura
   int SensorTempTensao=analogRead(SensorTempPino);

   // Converte a tensao lida
   float Tensao=SensorTempTensao*5;
   Tensao/=1024;

   // Converte a tensao lida em Graus Celsius
   float TemperaturaC=(Tensao-0.5)*100;

   // Muda o cursor para a primeira coluna e segunda linha do LCD
   LCD.setCursor(0,1);

   // Imprime a temperatura em Graus Celsius
   LCD.print(TemperaturaC);
  
    
    // Faz a leitura da tensao no Sensor de Umidade 
    int SensorUmidTensao=analogRead(SensorUmidPino);
        
    // Converte a tensao lida em porcentagem
    float porcem=map(SensorUmidTensao,0,1023,0,100);
    
    // Muda o cursor para a segunda coluna e nona linha do LCD
    LCD.setCursor(8,1);
     
    // Imprime a umidade em porcentagem
    LCD.print(porcem);
  
  // Acende ou apaga os alertas luminosos de temperatura baixa e alta
  	if (TemperaturaC>=TempAlta) {
  		digitalWrite(AlertaTempBaixa, LOW);
      	digitalWrite(AlertaTempNormal, LOW);
  		digitalWrite(AlertaTempAlta, HIGH);
    }
  	else if (TemperaturaC<=TempBaixa) {
  		digitalWrite(AlertaTempBaixa, HIGH);
      	digitalWrite(AlertaTempNormal, LOW);
  		digitalWrite(AlertaTempAlta, LOW);
  	}
  	else {
      	digitalWrite(AlertaTempNormal, HIGH);
  		digitalWrite(AlertaTempBaixa, LOW);
  		digitalWrite(AlertaTempAlta, LOW);
    }

  // Aguarda 1 segundo
  	delay(1000);
}  


### Componentes:

1 Arduino Uno R3,
1 Sensor de temperatura [TMP36],
1 LCD 16x2,
4 Resistores,
1 Potenciômetro,
3 Leds [vermelho, verde, azul].
