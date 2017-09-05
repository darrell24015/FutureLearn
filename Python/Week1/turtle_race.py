import turtle
from random import randint

window = turtle.Screen()

laura = turtle.Turtle()
laura.color('red')
laura.shape('turtle')
laura.penup()
laura.goto(-160, 100)
laura.pendown()

randy = turtle.Turtle()
randy.color('green')
randy.shape('turtle')
randy.penup()
randy.goto(-160, 70)
randy.pendown()

chuck = turtle.Turtle()
chuck.color('blue')
chuck.shape('turtle')
chuck.penup()
chuck.goto(-160, 40)
chuck.pendown()

lucy = turtle.Turtle()
lucy.color('purple')
lucy.shape('turtle')
lucy.penup()
lucy.goto(-160, 10)
lucy.pendown()

for movement in range(100):
	laura.forward(randint(1,5))
	randy.forward(randint(1,5))
	chuck.forward(randint(1,5))
	lucy.forward(randint(1,5))

window.mainloop()

