from turtle import Turtle

STARTING_POSITIONS = [(20,0), (0,0),(-20,0)]

class Snake:
            
    def __init__(self):
         self.segments = []
         self.create_snake()
         self.head = self.segments[0]

    def add_segment(self, position):
        current_segment = Turtle("square")
        current_segment.color("white")
        current_segment.penup()
        current_segment.setpos(position)
        self.segments.append(current_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())



    def create_snake(self):
        for position in STARTING_POSITIONS:
          self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_position = self.segments[seg_num-1].pos()
            self.segments[seg_num].setpos(new_position)
        self.segments[0].forward(20)

    def up(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_position = self.segments[seg_num-1].pos()
            self.segments[seg_num].setpos(new_position)
        self.segments[0].setheading(90)  
        self.segments[0].forward(20)     

    def down(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_position = self.segments[seg_num-1].pos()
            self.segments[seg_num].setpos(new_position)
        self.segments[0].setheading(270)    
        self.segments[0].forward(20)

    def left(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_position = self.segments[seg_num-1].pos()
            self.segments[seg_num].setpos(new_position)
        self.segments[0].setheading(180)  
        self.segments[0].forward(20) 

    def right(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_position = self.segments[seg_num-1].pos()
            self.segments[seg_num].setpos(new_position)
        self.segments[0].setheading(0) 
        self.segments[0].forward(20) 