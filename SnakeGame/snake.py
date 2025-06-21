from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
STEP_SIZE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Model the snake class"""

    def __init__(self):
        """Initialize the snake"""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("triangle")

    def create_snake(self):
        """Create the snake's body"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.create_snake()

    def add_segment(self, position):
        new_segment = Turtle("square")
        if len(self.segments) == 0:
            new_segment.color("palegreen1")
        elif self.segments[-1].color() == ("palegreen1", "palegreen1"):
            new_segment.color("forestgreen")
        else:
            new_segment.color("palegreen1")
        new_segment.penup()
        new_segment.setpos(position)
        self.segments.append(new_segment)

    def extend(self):
        """Add a new segment to the snake on collision with food"""
        self.add_segment(self.segments[-1].pos())

    def move(self):
        """Move the snake body forwards by one unit"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].setpos(self.segments[seg_num - 1].pos())
        self.segments[0].forward(STEP_SIZE)

    def up(self):
        """Change the snake's direction to move upwards."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the snake's direction to move downwards."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change the snake's direction to move left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change the snake's direction to move right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
