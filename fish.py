import cTurtle
from world import *

class Fish:
    """
    Fish should know: i.) the world they belong to, ii.) their specific
    location(x,y) iii.) and how long they have gone without breeding.
    iv.) Each fish also has an instance of Turtle so it can be displayed.
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
# "getting" values.
    def getX(self):
        return self.xpos
    def getY(self):
        return self.ypos

# Mutator methods ("setting" values) to interact with Fish objects
# and allow basic Turtle function
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
        '''
        A fish checks the number of fish in its surrounding locations, it
        dies if there's overcrowding or breeds and moves when there's no
        crowding.
        '''
        offsetList = [(-1,1), (0,1), (1,1),
                      (-1,0),        (1,0),
                      (-1,-1),(0,-1),(1,-1)]
        adjfish = 0
        for offset in offsetList:
            newx = self.xpos + offset[0]
            newy = self.ypos + offset[1]
            if 0 <= newx < self.world.getXDimension() and
               0 <= newx < self.world.getYDimension():
               if (not self.world.emptyLocation(newx,newy)) and
                  isinstance(self.world.lookAtLocation(newx, newy, Fish)):
                   adjfish = adjfish + 1

        if adjfish >= 2:
            self.world.delLifeForm(self)
        else:
            self.breedTick = self.breedTick + 1
            if self.breedTick >= 12:
                self.tryToBreed()
            self.tryToMove()

    def tryToBreed(self):
        offsetList = [(-1,1), (0,1), (1,1),
                      (-1,0),        (1,0),
                      (-1,-1),(0,-1),(1,-1)]
        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]
        nextx = self.xpos + randomOffset[0]
        nexty = self.xpos + randomOffset[1]
        while not (0 <= nextx < self.world.getXDimension() and
                   0 <= nexty < self.world.getYDimension() ):
                   randomOffsetIndex = random.randrange(len(offsetList))
                   randomOffset = offsetList[randomOffsetIndex]
                   nextx = self.xpos + randomOffset[0]
                   nexty = self.xpos + randomOffset[1]

        if self.world.emptyLocation(nextx, nexty):
            childFish = Fish()
            self.world.addLifeForm(childFish, nextx, nexty)
            self.breedTick = 0

    def tryToMove(self):
        offsetList = [(-1,1), (0,1), (1,1),
                      (-1,0),        (1,0),
                      (-1,-1),(0,-1),(1,-1)]
        randomOffsetIndex = random.randrange(len(offsetList))
        randomOffset = offsetList[randomOffsetIndex]
        nextx = self.xpos + randomOffset[0]
        nexty = self.xpos + randomOffset[1]
        while not (0 <= nextx < self.world.getXDimension() and
                   0 <= nexty < self.world.getYDimension() ):
                   randomOffsetIndex = random.randrange(len(offsetList))
                   randomOffset = offsetList[randomOffsetIndex]
                   nextx = self.xpos + randomOffset[0]
                   nexty = self.xpos + randomOffset[1]

        if self.world.emptyLocation(nextx, nexty):
            self.move(nextx, nexty)
