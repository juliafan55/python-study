from tkinter import *


def miles_to_km():
    miles_input = int(entry.get())
    km_result = round(miles_input * 1.6, 2)
    conversion["text"] = km_result


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=200)
window.config(padx=20, pady=20)

# labels
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

conversion = Label(text="0")
conversion.grid(column=1, row=1)

# entry
entry = Entry(width=7)
entry.grid(column=1, row=0)

# button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)


window.mainloop()
