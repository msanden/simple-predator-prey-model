import cTurtle
import random

from world import *
from fish import *
from bear import *


def mainSimulation():
    numberOfBears = 10
    numberOfFish = 10
    worldLifeTime = 2500
    worldWidth = 50
    worldLength = 50

    myworld = World(worldWidth, worldLength)
    myworld.draw()

    for fish in range(numberOfFish):
        newfish = Fish()
        x = random.randrange(myworld.getXDimension())
        y = random.randrange(myworld.getYDimension())
        while not myworld.emptyLocation(x,y):
            x = random.randrange(myworld.getXDimension())
            y = random.randrange(myworld.getYDimension())
        myworld.addLifeForm(newfish, x, y)

    for bear in range(numberOfBears):
        newbear = Bear()
        x = random.randrange(myworld.getXDimension())
        y = random.randrange(myworld.getYDimension())
        while not myworld.emptyLocation(x,y):
            x = random.randrange(myworld.getXDimension())
            y = random.randrange(myworld.getYDimension())
        myworld.addLifeForm(newbear, x, y)

    for time in range(worldLifeTime):
        myworld.liveLife()
