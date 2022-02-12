import math
import turtle


def xt(i):
    return 16 * math.sin(i) ** 3


def yt(i):
    return 13 * math.cos(i) - 5 * \
            math.cos(2 * i) - 2 * \
            math.cos(3 * i) - \
            math.cos(4 * i)


t = turtle.Turtle()
t.speed(500)
turtle.colormode(255)
turtle.Screen().bgcolor(0, 0, 0)

for i_line in range(2550):
    t.goto((xt(i_line) * 20, yt(i_line) * 20))
    t.pencolor((255 - i_line) % 255, (i_line % 255), (255 + i_line) % 255)
    t.goto(0, 0)

t.hideturtle()
turtle.update()
turtle.mainloop()
