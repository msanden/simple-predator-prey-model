import cTurtle
import random

from world import *
from fish import *

class Bear:
    """In this context, bears will first and foremost try to breed.  They
    will eat fish if they are available, and if any bear does not get enough
    food it will starve and die."""

    def __init__(self):
        self.breedTick = 0
        self.starveTick = 0
        self.world = None

        self.xpos = 0
        self.ypos = 0
        self.turtle = cTurtle.Turtle()
        self.turtle.up()
        self.turtle.hideturtle()
        self.turtle.shape("bear.gif")

    def liveLife(self):
        self.breedTick = self.breedTick + 1
        if self.breedTick >= 8:
            self.tryToBreed()

        self.tryToEat()

        if self.starveTick == 10:
            self.world.delLifeForm(self)
        else:
            self.tryToMove()

    def tryToEat(self):
        offsetList = [(-1,1), (0,1), (1,1),
                      (-1,0),        (1,0),
                      (-1,-1),(0,-1),(1,-1)]
        adjprey = []
        for offset in offsetList:
            newx = self.xpos + offset[0]
            newy = self.ypos + offset[1]
            if 0 <= newx < self.world.getXDimension() and 0 <= newy < self.world.getYDimension():
               if (not self.world.emptyLocation(newx,newy)) and isinstance(self.world.lookAtLocation(newx, newy, Fish)):
                   adjprey.append(self.world.lookAtLocation(newx, newy))

        if len(adjprey) > 0:
            randomprey = adjprey[random.randrange(len(adjprey))]
            preyx = randomprey.getX()
            preyy = randomprey.getY()

            self.world.delLifeForm(randomprey)
            self.move(preyx, preyy)
            self.starveTick = 0
        else:
            self.starveTick = self.starveTick + 1
