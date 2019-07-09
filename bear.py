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
        self.turtle.shape("img/bear.gif")

    def getX(self):
        return self.xpos
    def getY(self):
        return self.ypos

    def setX(self, newx):
        self.xpos = newx
    def setY(self, newy):
        self.ypos = newy
    def setWorld(self, aworld):
        self.world = aworld

    def appear(self):
        self.turtle.goto(self.xpos, self.ypos)
        self.turtle.showturtle()

    def hide(self):
        self.turtle.hideturtle()

    def move(self, newx, newy):
        self.world.moveLifeForm(self.xpos, self.ypos, newx, newy)
        self.xpos =  newx
        self.ypos =  newy
        self.turtle.goto(self.xpos, self.ypos)


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
               if (not self.world.emptyLocation(newx,newy)) and isinstance(self.world.lookAtLocation(newx, newy), Fish):
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

    def tryToBreed(self):
        offsetList = [(-1,1), (0,1), (1,1),
                      (-1,0),        (1,0),
                      (-1,-1),(0,-1),(1,-1)]
        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]
        nextx = self.xpos + randomOffset[0]
        nexty = self.ypos + randomOffset[1]
        while not (0 <= nextx < self.world.getXDimension() and
                   0 <= nexty < self.world.getYDimension() ):
                   randomOffsetIndex = random.randrange(len(offsetList))
                   randomOffset = offsetList[randomOffsetIndex]
                   nextx = self.xpos + randomOffset[0]
                   nexty = self.ypos + randomOffset[1]

        if self.world.emptyLocation(nextx, nexty):
            childBear = Bear()
            self.world.addLifeForm(childBear, nextx, nexty)
            self.breedTick = 0

    def tryToMove(self):
        offsetList = [(-1,1), (0,1), (1,1),
                      (-1,0),        (1,0),
                      (-1,-1),(0,-1),(1,-1)]
        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]
        nextx = self.xpos + randomOffset[0]
        nexty = self.ypos + randomOffset[1]
        while not (0 <= nextx < self.world.getXDimension() and
                   0 <= nexty < self.world.getYDimension() ):
                   randomOffsetIndex = random.randrange(len(offsetList))
                   randomOffset = offsetList[randomOffsetIndex]
                   nextx = self.xpos + randomOffset[0]
                   nexty = self.ypos + randomOffset[1]

        if self.world.emptyLocation(nextx, nexty):
            self.move(nextx, nexty)
