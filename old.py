# File: main.py

__author__ = "Huy2007Chuck"
__date__ = "$Sep 20, 2020 10:34:39 AM$"

# Turtle race by Huy2007Chuck

import random
import time
from tkinter import messagebox
from tkinter import simpledialog
import turtle
from turtle import Turtle

# Constants and variables
W, H = 480, 640

FONT = ("Comic Sans MS", 5)
TITLE_FONT = ("Comic Sans MS", 30)

COLS = [
    "blue",
    "red",
    "green",
    "yellow",
    "purple",
    "orange",
    "cyan",
    "magenta",
]

run_count = 0

# Init
win = turtle.Screen()
win.title("Turtle Race")
win.setup(W, H)


class Racer:

    def __init__(self, order, count, xpos):
        self.order = order
        self.count = count
        self.xpos = xpos
        self.col = COLS[self.order]

        self.t = Turtle()
        self.t.penup()
        self.t.speed(4)
        self.t.color(self.col)
        self.t.shape("turtle")
        self.t.setpos(self.xpos[self.order], -240)
        self.t.left(90)
        self.t.pendown()

        # Write name (color)
        self.t.penup()
        self.t.backward(30)
        self.t.write(self.col.upper(), font=FONT, align="center")
        self.t.forward(30)
        self.t.pendown()


    def move(self):
        step = random.randint(0, self.count * 2)
        self.t.forward(step)
        return None


    def win(self):
        if self.t.pos()[1] >= 240:
            turtle.penup()
            turtle.setpos(0, 0)
            turtle.pendown()
            turtle.color(self.col)
            turtle.write(self.col.upper() + " WINS!", font=TITLE_FONT, align="center")

            self.t.setpos(self.xpos[self.order], 250)
            return True


def main():
    turtle.clearscreen()
    turtle.speed(0)
    turtle.hideturtle()

    turtle.penup()
    turtle.setpos(-240, 240)
    turtle.pendown()
    turtle.setpos(240, 240)

    count = simpledialog.askinteger("Input", "Enter racer count", minvalue=2, maxvalue=8)

    try:
        gap = W / (count + 1)
    except TypeError:
        print("cancel")
        quit()

    #gap = W / (count + 1)
    halves = [i * 0.5 for i in range(3, 14)]
    temp = [i * gap for i in range(1, count + 1)]
    xpos = [i -gap * halves[count - 2] for i in temp]

    racers = []

    for i in range(count):
        r = Racer(i, count, xpos)
        racers.append(r)

    run = True
    while run:
        for r in racers:
            if r.win():
                run = False
                break
            else:
                r.move()


if __name__ == "__main__":
    while True:
        run_count += 1

        if run_count == 1:
            redo = True

        if redo:
            main()
        else:
            quit()

        time.sleep(3)
        redo = messagebox.askyesno(title="Redo?", message="Do you want to redo the race?")
