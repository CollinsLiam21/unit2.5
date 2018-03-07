#Liam Collins
#3/7/18
#olympics.py

from ggame import *

blue = Color(0x0000FF,1)
black = Color(0x000000,1)
red = Color(0xFF0000,1)
yellow = Color(0xFFFF00,1)
green = Color(0x00FF00,1)
white = Color(0xFFFFFF,1)

blueCircle = CircleAsset(100,LineStyle(1,blue),blue)
whiteCircle = CircleAsset(80,LineStyle(1,white),white)
blackCircle = CircleAsset(100,LineStyle(1,black),black)
redCircle = CircleAsset(100,LineStyle(1,red),red)
yellowCircle = CircleAsset(100,LineStyle(1,yellow),yellow)

Sprite(blueCircle)
Sprite(whiteCircle, (20,20))
Sprite(blackCircle, (225,0))
Sprite(whiteCircle, (245,20))
Sprite(redCircle, (450,0))
Sprite(whiteCircle, (470,20))
Sprite(yellowCircle, (113,113))
Sprite(whiteCircle, (133,133))

App().run()
