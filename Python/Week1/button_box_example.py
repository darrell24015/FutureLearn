from guizero import App,PushButton,TextBox

def do_stuff():
	print("Well, Hello There!")

def do_other_stuff():
	print("Hello to you too!")

app = App("Lots of Buttons")

firstButtonOnTop = PushButton(app, text="First Button on Top", command=do_stuff)
button1 = PushButton(app, text="First Button", command=do_stuff)
button2 = PushButton(app, text="Second Button", command=do_other_stuff)

app.display()

