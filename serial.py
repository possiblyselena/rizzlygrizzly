from machine import Pin
import time
import random

goodLines = ["You’re hotter than papa bears porridge!! ","If you were a bear, you’d be unBEARably cute!! ","Are you a teddy bear? Because I wanna snuggle you all night!!", "Is your name Teddy? Because you make me feel warm and fuzzy…", "You must be the honey to my bear, because I’m totally drawn to you.","I’m not a bear, but I’d definitely like to cuddle with you in the wild.", "You must be made of honey, because you’re stuck on my mind."]
badLines = ["I must be a grizzly, because every time you’re near, I’m just growling for more.","I must be a grizzly, because every time you’re near, I’m just growling for more.", "Bears are known for their strength… but I’d let you make me weak in the knees anytime.", "You’re the honey, I’m the bear—can’t resist you.", "Let’s skip hibernation and get wild tonight… ", "I’d let you wake me up from hibernation.", "If I were a bear, I’d choose your arms as my den.",]

goodButton = Pin(2, Pin.IN, Pin.PULL_UP)
badButton = Pin(3, Pin.IN, Pin.PULL_UP)


while True:
    if goodButton.value() == 0:
        print(random.choice(goodLines))
        time.sleep(1)
    if badButton.value() == 0:
        print(random.choice(badLines))
        time.sleep(1)