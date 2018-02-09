#Liam Collins
#2/7/18
#graphicsDemo.py - using ggame

from ggame import *

red = Color(0xFF0000,1)
green = Color(0x00FF00,1)
blue = Color(0x0000FF,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

redRectangle = RectangleAsset(100,100,blackOutline,red) #width, height, outline, fill
redRectangle2 = RectangleAsset(25,50,blackOutline,red)
#blueCircle = CircleAsset(50,blackOutline,blue) #radius, outline, fill
#greenEllipse = EllipseAsset(100,50,blackOutline,green) #width, height, outline, fill
#blackLine = LineAsset(0,60,blackOutline) #x_endpoint, y_endpoint, lineStyle
redTriangle = PolygonAsset([(100,100), (150,150), (50,150)],blackOutline,green) #endpoint, outline, fill
#text = TextAsset('Literature',fill=green, style='bold 40pt Times') #text, other options

Sprite(redRectangle, (100,150))
Sprite(redRectangle2, (135,200))
#Sprite(blueCircle,(50,50))
#Sprite(greenEllipse,(200,50))
#Sprite(blackLine, (135,190))
Sprite(redTriangle, (100,100))
#Sprite(text, (200,400))

App().run()
