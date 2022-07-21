from tkinter import *

# creates the screen
window = Tk()
window.title("GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# components

# label
my_label = Label(text="I am a label", font=("Arial", 24, "normal"))
# place the label on the screen (kind of like query selector from js?)
my_label["text"] = "new text"
# my_label.pack()
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# button


def button_clicked():
    # print("I got clicked")
    # my_label["text"] = "Button got clicked"
    input_text = input.get()
    my_label["text"] = input_text


button = Button(text="Click me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="New button")
new_button.grid(column=2, row=0)

# entry (input)

input = Entry(width=10)
# input.pack()
# input_text = input.get()
input.grid(column=3, row=2)


# keeps the window on the screen
window.mainloop()
