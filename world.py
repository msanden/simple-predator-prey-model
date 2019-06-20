import cTurtle

class World:
    def __init__(self, xDimension, yDimension):
        '''
        The world model consists of life-forms that live at specific
        locations in a two-dimensional world grid.
        The grid is a list of rows.
        '''
        self.xDimension = xDimension
        self.yDimension = yDimension
        self.lifeForms = []
        self.grid = []

        # ======================================
        # Creating the list of lists implementation:
        # Each entry in list is initialized as a None type
        # ex. g = [ [None, None, None, None, None],
        #           [None, None, None, None, None],
        #           [None, None, None, None, None],
        #           [None, None, None, None, None] ]
        # ======================================
        for arow in range(self.xDimension):
            row = []
            for acol in range(self.yDimension):
                row.append(None)
            self.grid.append(row)

        #Defining the bounds of our world model
        self.wturtle = cTurtle.Turtle()
        self.wturtle.setWorldCoordinates(0,0,self.xDimension-1,self.yDimension-1)
        self.wturtle.addshape("Bear.gif")
        self.wturtle.addshape("Fish.gif")
        self.wturtle.hideturtle()

    def draw(self):
        '''
        Method draws the grid system using x & y dimensions.
        '''
        self.wturtle.tracer(0)
        self.wturtle.forward(self.xDimension-1)
        self.wturtle.left(90)
        self.wturtle.forward(self.yDimension-1)
        self.wturtle.left(90)
        self.wturtle.forward(self.xDimension-1)
        self.wturtle.left(90)
        self.wturtle.forward(self.yDimension-1)
        self.wturtle.left(90)

        for i in range(self.yDimension-1):
            self.wturtle.forward(self.xDimension-1)
            self.wturtle.backward(self.xDimension-1)
            self.wturtle.left(90)
            self.wturtle.forward(1)
            self.wturtle.right(90)
        self.wturtle.forward(1)
        self.wturtle.right(90)

        for i in range(self.xDimension-2):
            self.wturtle.forward(self.yDimension-1)
            self.wturtle.backward(self.yDimension-1)
            self.wturtle.left(90)
            self.wturtle.forward(1)
            self.wturtle.right(90)
        self.wturtle.tracer(1)

    def freezeGraphic(self):
        self.wturtle.exitOnClick()

    def getXDimension(self):
        return self.xDimension

    def getYDimension(self):
        return self.yDimension

    def lookAtLocation(self, x, y):
        return self.grid[y][x]

    def addLifeForm(self, creature, x, y):
        '''
        Method adds the life-form to our list and the position where it should
        be placed
        '''
        creature.setX(x)
        creature.setY(y)
        self.grid[y][x] = creature
        creature.setWorld(self)
        self.lifeForms.append(creature)
        creature.appear()

    def moveLifeForm(self, oldx, oldy, newx, newy):
        self.grid[newy][newx] = self.grid[oldy][oldx]
        self.grid[oldy][oldx] = None

    def emptyLocation(self, x,y):
        if self.grid[y][x] == None:
            return True
        else:
            return False

    def liveLife(self):
    '''A creature is selected at random, then allowed to live life (breed)'''
        if self.lifeForms != [ ]:
            creature = random.randrange(len(self.lifeForms))
            randomCreature = self.lifeForms[creature]
            randomCreature.livelife()

    def delLifeForm(self, creature):
        creature.hide()
        self.grid[creature.getYDimension()][creature.getXDimension()] = None
        self.lifeForms.remove(creature)
