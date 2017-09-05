from tkinter import Tk, Label, Button
from shapes import Triangle, Rectangle, Oval

class MyGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="This is the Root Window")
        self.label.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack()

rectangle1 = Rectangle()

rectangle1.set_width(200)
rectangle1.set_height(100)
rectangle1.set_color("blue")
rectangle1.set_x(50)
rectangle1.set_y(250)

triangle1 = Triangle()
# triangle1.randomise()
triangle1.set_color("red")
triangle1.x=150
triangle1.y=150
triangle1.x2=150
triangle1.y2=200
triangle1.x3=200
triangle1.y3=150


oval1 = Oval()
# oval1.randomise()
oval1.set_color("green")
oval1.set_x(300)
oval1.set_y(300)
oval1.set_height(200)
oval1.set_width(200)

rectangle1.draw()
oval1.draw()
triangle1.draw()

root = Tk()
gui = MyGUI(root)
root.mainloop()