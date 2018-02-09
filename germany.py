#Liam Collins
#2/9/18
#germany.py

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)
yellow = Color(0xFFFF00,1)

blackOutline = LineStyle(1,black)
redOutline = LineStyle(1,red)
yellowOutline = LineStyle(1,yellow)

blackRectangle = RectangleAsset(300,50,blackOutline,black)
redRectangle = RectangleAsset(300,50,redOutline,red) #width, height, outline, fill
yellowRectangle = RectangleAsset(300,50,yellowOutline,yellow)


text = TextAsset('Literature',fill=green, style='bold 40pt Times') #text, other options

Sprite(blackRectangle, (100,100))
Sprite(redRectangle, (100,150))
Sprite(yellowRectangle, (100,200))


App().run()
