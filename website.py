import utime
import time
import network
import socket
import machine
import random
from machine import I2C, Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 39
I2C_NUM_ROWS = 2
I2C_NUM_COLS = 16

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

goodButton = Pin(2, Pin.IN, Pin.PULL_UP)
badButton = Pin(3, Pin.IN, Pin.PULL_UP)


ssid = "Selena's IPhone"
password = 'Brillson'

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection')
        time.sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip
    
def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage():
    html = f"""
            <!DOCTYPE html>
            <head>
            </head>
            <body>
            <h1>welcome to rizzly grizzlys super rizz simulator</h1>
            <p> Have you ever yearned to approach a hot babe?
            Have you ever been too shy, and felt too ugly to even say hello?
            Well Rizzly Grizzly can help!
            Rizzly will supply you with all the charming, insightful lines needed to get that special someone.
            </p>
            <p>
            The first step to picking up your new special someone is to figure out what the best attitude is to approach them with.
            Rizzly Grizzly features two options depending on the situation.
            For a condifent, frisky vibe, press my lips and hear a wisp.
            If you're feeling friendly and want to awaken your inner charm, touch my heart, and I'll touch yours.
            </p>
            <p>
            If you're too nervous to even speak, no problem! Connect Rizzly's charm to our website, and he'll do all the talking!
            </p>
            <audio src="1.mp3"><audio>
            <script>
            </script>
            </body>
            </html>
            """
    return str(html)

def serve(connection):
        global buttonPressed
        client = connection.accept()[0]
        request = client.recv(1024)
        request =str(request)
        print(request)     
        html = webpage()
        client.send(html)
        client.close()
        
def goodLine1():
    lcd.clear()
    lcd.move_to(1,0)
    lcd.putstr("You are hotter")
    lcd.move_to(0,1)
    lcd.putstr("than Papa Bears")
    time.sleep(1)
    lcd.clear()
    lcd.move_to(6,0)
    lcd.putstr("...")
    time.sleep(3)
    lcd.clear()
    lcd.move_to(3,0)
    lcd.putstr("Porridge!")
    
def goodLine2 ():
    lcd.clear()
    lcd.putstr("If you were")
    lcd.move_to(0,1)
    lcd.putstr("a bear,")
    time.sleep(3)
    lcd.clear()
    lcd.putstr("you'd be")
    lcd.move_to(0,1)
    lcd.putstr("unBEARably cute!!")

def goodLine3 ():
    lcd.clear()
    lcd.putstr("Are you a teddy")
    lcd.move_to(0,1)
    lcd.putstr("bear?")
    time.sleep(2)
    lcd.clear()
    lcd.putstr("Because I wanna")
    lcd.move_to(0,1)
    lcd.putstr("snuggle you all")
    time.sleep(3)
    lcd.clear()
    lcd.putstr("night!!")

def goodLine4 ():
    lcd.clear()
    lcd.putstr("Is your name")
    lcd.move_to(0,1)
    lcd.putstr("Teddy?")
    time.sleep(3)
    lcd.clear()
    lcd.putstr("Because you")
    lcd.move_to(0,1)
    lcd.putstr("make me feel")
    time.sleep(2)
    lcd.clear()
    lcd.putstr("warm and fuzzy...")

def goodLine5 ():
    lcd.clear()
    lcd.putstr("You must be")
    lcd.move_to(0,1)
    lcd.putstr("the honey to")
    time.sleep(2)
    lcd.clear()
    lcd.putstr("my bear,")
    lcd.move_to(0,1)
    lcd.putstr("because I'm")
    time.sleep(2)
    lcd.clear()
    lcd.putstr("totally drawn")
    lcd.move_to(0,1)
    lcd.putstr("to you...")

def goodLine6 ():
    lcd.clear()
    lcd.putstr("I'm not a")
    lcd.move_to(0,1)
    lcd.putstr("bear, but I'd")
    time.sleep(2)
    lcd.clear()
    lcd.putstr("definitely like")
    lcd.move_to(0,1)
    lcd.putstr("to cuddle")
    time.sleep(2)
    lcd.clear()
    lcd.putstr("with you")
    lcd.move_to(0,1)
    lcd.putstr("in the wild!")

def goodLine7 ():
    lcd.clear()
    lcd.putstr("You must be")
    lcd.move_to(0,1)
    lcd.putstr("made of honey")
    time.sleep(3)
    lcd.clear()
    lcd.putstr("because you are")
    lcd.move_to(0,1)
    lcd.putstr("stuck in my mind")
    
def badLine1 ():
    lcd.clear()
    lcd.putstr("I must be a")
    lcd.move_to(0,1)
    lcd.putstr("grizzly, beacuse")
    time.sleep(3)
    lcd.clear()
    lcd.putstr("every time your")
    lcd.move_to(0,1)
    lcd.putstr("are near, I'm")
    time.sleep(3)
    lcd.clear()
    lcd.putstr("growling for")
    lcd.move_to(0,1)
    lcd.putstr("more...")
    

def badLine2 ():
    lcd.clear()
    lcd.putstr("I must be a")
    lcd.move_to(0,1)
    lcd.putstr("grizzly because")
    time.sleep(3)
    lcd.clear()
    lcd.putstr("every time your")
    lcd.move_to(0,1)
    lcd.putstr("are near, I'm")
    time.sleep(3)
    lcd.clear()
    lcd.putstr("just growling")
    lcd.move_to(0,1)
    lcd.putstr("for more...")
    

def badLine3 ():
    lcd.clear()
    lcd.putstr("Bears are known")
    lcd.move_to(0,1)
    lcd.putstr("for their")
    time.sleep(3)
    lcd.clear()
    lcd.putstr("strength... but")
    lcd.move_to(0,1)
    lcd.putstr("I'd let you make")
    time.sleep(3)
    lcd.clear()
    lcd.putstr("me weak in the")
    lcd.move_to(0,1)
    lcd.putstr("knees anytime")

def badLine4 ():
    lcd.clear()
    lcd.putstr("You are the")
    lcd.move_to(0,1)
    lcd.putstr("honey, I'm the")
    time.sleep(3)
    lcd.clear()
    lcd.putstr("bear- I can")
    lcd.move_to(0,1)
    lcd.putstr("not resist you")

def badLine5 ():
    lcd.clear()
    lcd.putstr("Lets skip")
    lcd.move_to(0,1)
    lcd.putstr("hibernation")
    time.sleep(3)
    lcd.clear()
    lcd.putstr("and get wild")
    lcd.move_to(0,1)
    lcd.putstr("tonight...")

def badLine6 ():
    lcd.clear()
    lcd.putstr("I'd let you")
    lcd.move_to(0,1)
    lcd.putstr("wake me up")
    time.sleep(3)
    lcd.clear()
    lcd.putstr("from hibernation")

def badLine7 ():
    lcd.clear()
    lcd.putstr("If I were")
    lcd.move_to(0,1)
    lcd.putstr("a bear, I'd")
    time.sleep(3)
    lcd.clear()
    lcd.putstr("choose your")
    lcd.move_to(0,1)
    lcd.putstr("arms as my den")

goodLines = [goodLine1, goodLine2, goodLine3, goodLine4, goodLine5, goodLine6, goodLine7]
badLines = [badLine1, badLine2, badLine3, badLine4, badLine5, badLine6, badLine7]

ip = connect()
connection = open_socket(ip)
serve(connection)

while True:
        if goodButton.value() == 0:
            print("yay")
            random_goodline = random.choice(goodLines)
            random_goodline()
            time.sleep(3)
            lcd.clear()
        if badButton.value() == 0:
            print("nay")
            random_badline = random.choice(badLines)
            random_badline()
            time.sleep(3)
            lcd.clear()
       