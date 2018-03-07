#Liam Collins
#3/7/18
#yield.py

from ggame import *

yellow = Color(0xFFFF00,1)
black = Color(0x000000,1)

blackOutline = LineStyle(1,black)

triangle = PolygonAsset([(0,0), (400,0), (200,400)],blackOutline,yellow)
text = TextAsset('Yield',fill=black,style='bold 60pt Times')

Sprite(triangle)
Sprite(text, (105,5))

App().run()
