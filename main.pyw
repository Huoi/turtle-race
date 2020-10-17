# File: main.pyw
# By: Huy2007Chuck
# Turtle race with randomized steps
# Credit to Tech with Tim for giving me idea

import random
import time
from tkinter import simpledialog
import turtle
from turtle import Turtle

# Constants and variables
W, H = 480, 640

FONT = ("Comic Sans MS", 5)
MEDIUM_FONT = ("Comic Sans MS", 15)
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

race_index = 0

# Init
win = turtle.Screen()
win.title("Turtle Race")
win.setup(W, H)


class Racer:

    def __init__(self, order, count, pos):
        self.order = order
        self.count = count
        self.pos = pos
        self.col = COLS[self.order]

        self.t = Turtle()
        self.t.penup()
        self.t.speed(0)
        self.t.color(self.col)
        self.t.shape("turtle")
        self.t.setpos(self.pos[self.order], -240)
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
            turtle.write(self.col.upper() + " WINS!", font=TITLE_FONT,
                         align="center")

            self.t.setpos(self.pos[self.order], 300)

            with open("winners.txt", "a") as file:
                file.write(self.col + "\n")
                file.close()

            return True


def pos_list(dimension, count):
    if dimension == "x":
        side = W
    elif dimension == "y":
        side = H

    try:
        gap = side / (count + 1)
    except TypeError:
        print("cancel")
        quit()

    #gap = W / (count + 1)
    halves = [i * 0.5 for i in range(3, 14)]
    temp = [i * gap for i in range(1, count + 1)]
    pos = [i - gap * halves[count - 2] for i in temp]

    return pos


def reset_screen(race_index):
    turtle.clearscreen()
    turtle.penup()
    turtle.setpos(W / 2 * -1 + 10, H / 2 * -1 + 10)
    turtle.color("black")
    turtle.pendown()
    turtle.write("Race " + str(race_index), font=MEDIUM_FONT, align="left")
    turtle.penup()


def show_result(count, winners):
    turtle.clearscreen()
    turtle.penup()
    pos = pos_list("y", count)
    pos = pos[::-1]

    for i in range(count):
        turtle.penup()
        turtle.setpos(-100, pos[i])
        turtle.pendown()
        turtle.color(COLS[i])
        turtle.write(COLS[i].upper() + ": " + str(winners.count(COLS[i])),
                     font=MEDIUM_FONT, align="left")
        turtle.penup()

    turtle.hideturtle()

def main(count):
    turtle.speed(0)
    turtle.hideturtle()

    turtle.penup()
    turtle.setpos(-240, 240)
    turtle.pendown()
    turtle.setpos(240, 240)

    racers = []

    for i in range(count):
        r = Racer(i, count, pos_list("x", count))
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
    with open("winners.txt", "w") as file:
        file.close()

    count = simpledialog.askinteger("Input", "Enter racer count",
                                    minvalue=2, maxvalue=8)

    race_count = simpledialog.askinteger("Input", "How many races?",
                                         minvalue=1)

    try:
        for _ in range(race_count):
            race_index += 1
            reset_screen(race_index)
            main(count)
            time.sleep(3)
    except TypeError:
        print("cancel")

    with open("winners.txt", "r") as file:
        winners = []
        for line in file:
            winners.append(line.strip())

    print(winners)
    show_result(count, winners)
    turtle.Screen().exitonclick()
