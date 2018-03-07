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

Sprite(blueCircle)
Sprite(whiteCircle, (20,20))

App().run()
