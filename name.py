#Liam Collins
#2/7/18
#graphicsDemo.py - using ggame

from ggame import *

name = input('Enter your name: ')
colorCode = input('Enter color code: ')

color = Color(colorCode,1)

blackOutline = LineStyle(0,black)

Rectangle = RectangleAsset(1100,600,blackOutline,color) #width, height, outline, fill
text = TextAsset(name,fill=black, style='bold 25pt Times') #text, other options

Sprite(Rectangle)
Sprite(text,(400,225))

App().run()
