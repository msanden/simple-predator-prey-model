class Bear(object):
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
        self.turtle.shape("Bear.gif")

        
