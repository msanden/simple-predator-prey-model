import cTurtle
from world import *

class Fish:
    """
    Fish should know: i) the world they belong to, ii) their specific
    location(x,y) iii) and how long they have gone without breeding.
    iv) Each fish also has an instance of Turtle so it can be displayed.
    """

    def __init__(self):
        self.turtle = cTurtle.Turtle()
        self.turtle.up()
        self.turtle.hideturtle()
        self.turtle.shape("Fish.gif")

        self.xpos = 0
        self.ypos = 0
        self.world = None

        self.breedTick = 0

# Accessor methods to interact with Fish objects.
# "getting" and "setting" values.
    def setX(self, newx):
        self.xpos = newx
    def setY(self, newy):
        self.ypos = newy

    def getX(self):
        return self.xpos
    def getY(self):
        return self.ypos
