import Adafruit_CharLCD as LCD
import time
import requests
import json

#SETS ALL THE PINS, change this if you  did not follow the schematics
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 0
lcd_columns = 16
lcd_rows = 2


lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight) #initialise the pins
lcd.clear()
def getData(): #get request to find the btc price
    r = requests.get('https://blockchain.info/ticker')
    a = r.text
    data = json.loads(a)
    current_price = data['USD']['last']
    current_price = str(current_price)
    printLCD(current_price)

def printLCD(price): #display the price on the screen, waits 10 seconds and repeat.
    lcd.clear()
    lcd.message("BTC:" + price + "$")
    time.sleep(10)
    getData()

getData()
