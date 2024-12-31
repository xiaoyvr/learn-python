import turtle
import math
import time
import sys
import numpy as np
from turtle_ex import TurtleEx
from collections import namedtuple

Config = namedtuple('Config', ['h', 'background_radius', 'deferent_radius', 'epicycle_radius', 'center_x', 'center_y'])

config = Config(
    h=50,
    background_radius=300,
    deferent_radius=150,
    epicycle_radius=50,
    center_x =0,
    center_y =0,
)

center = (config.center_x, config.center_y)
eccentric = (center[0], center[1] + config.h)
equant = (center[0], center[1] + config.h * 2)

def draw_background(t):
    t.draw_point(center, "O")
    t.draw_point(equant, "Q")
    t.draw_point(eccentric, "D")
    t.draw_cycle(center, config.background_radius)
    t.draw_cycle(eccentric, config.deferent_radius)

def draw_track(t_deferent, t_epicycle, epicycle_factor):
    eccentric_x, eccentric_y = eccentric
    t_deferent.move((eccentric_x, eccentric_y + config.deferent_radius))
    t_deferent.t.setheading(180)
    t_epicycle.move((eccentric_x, eccentric_y + config.deferent_radius - config.epicycle_radius))
    for equant_angle in range(1, 361):
    # for equant_angle in np.arange(0.05, 360.05, 0.05):
        deferent_point = calculate_deferent_point(equant_angle)
        t_deferent.t.goto(deferent_point)
        t_epicycle.t.goto(calculate_epic_point(equant_angle, deferent_point, epicycle_factor))

def calculate_epic_point(equant_angle, center, epicycle_factor):
    epicycle_randians = math.radians(equant_angle) * epicycle_factor - math.pi/2
    x, y = center
    return config.epicycle_radius * math.cos(epicycle_randians) + x, config.epicycle_radius * math.sin(epicycle_randians) + y

def calculate_deferent_point(equtant_angle):
    equtant_radians = math.radians(equtant_angle)
    deferent_radians = equtant_radians - math.asin(math.sin(equtant_radians) * config.h / config.deferent_radius) + math.pi/2
    x, y = eccentric
    return config.deferent_radius * math.cos(deferent_radians) + x, config.deferent_radius * math.sin(deferent_radians) + y

def main():
    screen = turtle.Screen()
    screen.title("ptolemy")
    screen.tracer(5)

    t = turtle.Turtle()
    t.shape("arrow")
    t.speed(0)
    t.hideturtle()

    draw_background(TurtleEx(t))

    t_deferent = turtle.Turtle()
    t_deferent.shapesize(0.2, 0.2)
    t_deferent.shape("circle")
    t_deferent.speed(0)

    t_epicycle = turtle.Turtle()
    t_epicycle.shape("circle")
    t_epicycle.shapesize(0.2, 0.2)
    t_epicycle.color("red")
    t_epicycle.speed(0)

    # while True:

    r = int(sys.argv[1])
    r1 = int(sys.argv[2]) if len(sys.argv) > 2 else r + 1

    for epicycle_factor in range(r, r1):
        t_epicycle.clear()
        t_deferent.clear()
        draw_track(TurtleEx(t_deferent), TurtleEx(t_epicycle), epicycle_factor)
        screen.update()
        time.sleep(0.1)
        print(epicycle_factor)

    screen.mainloop()

if __name__ == "__main__":
    main()