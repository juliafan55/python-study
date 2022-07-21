from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:").grid(column=0, row=1)
website_entry = Entry(width=35).grid(column=1, row=1, columnspan=2)

email_username_label = Label(
    text="Email/Username:").grid(column=0, row=2)
email_username_entry = Entry(width=35).grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password:").grid(column=0, row=3)
password_entry = Entry(width=21).grid(column=1, row=3)

generate_pass_button = Button(text="Generate Password").grid(column=2, row=3)

add_button = Button(text="Add", width=36).grid(column=1, row=4, columnspan=2)

window.mainloop()
