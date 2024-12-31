import turtle

class TurtleEx:
    def __init__(self, turtle_instance):
        self.t = turtle_instance

    def move(self, p):
        self.t.penup()
        self.t.goto(p)
        self.t.pendown()

    def draw_cycle(self, p, r):
        x, y = p
        self.move((x, y - r))
        self.t.circle(r)

    def draw_point(self, p, text=None):
        self.move(p)
        self.t.dot(5, "black")
        if text:
            x, y = p
            self.move((x + 10, y))
            self.t.write(text, font=("Arial", 12, "normal"))
            