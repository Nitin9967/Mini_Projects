from tkinter import *
from tkinter import PhotoImage
from tkinter import messagebox
import random



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    pass_letters = [random.choice(letters) for _ in range(4)]
    pass_numbers = [random.choice(numbers) for _ in range(4)]
    pass_symbols = [random.choice(symbols) for _ in range(4)]
    password = pass_letters + pass_numbers + pass_symbols
    password = "".join(password)
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_entry_get = website_entry.get()
    email_entry_get = email_entry.get()
    password_entry_get = password_entry.get()
    if len(website_entry_get) < 1 or len(email_entry_get) < 1 or len(password_entry_get) < 1:
        messagebox.showwarning(title="Invalid Inputs",message="You Have Not Entered All Details CorrectLy Please Check !!")
    else:
        is_ok = messagebox.askokcancel(title = website_entry_get,message=f"The Details You Entered are : \nEmail : {email_entry_get}\nPasswoord : {password_entry_get}")
        # print(f"{website_entry_get} | {email_entry_get} | {password_entry_get}")
        if is_ok:
            file = open("Data.txt","a")
            file.write(f"\n{website_entry_get} | {email_entry_get} | {password_entry_get}")
            file.close()
            website_entry.delete(0,END)
            email_entry.delete(0,END)
            password_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx = 20,pady = 20)
window.title("Password Manager !!")
canvas = Canvas(height=200,width=200)
img = PhotoImage(file = "logo.png")
canvas.create_image(100,100,image = img)
canvas.grid(row = 0 , column = 1)
##   Label    ##
website_label = Label(text = 'Website :')
website_label.grid(row = 1 , column = 0)
email_label = Label(text = 'Email :')
email_label.grid(row = 2 , column = 0)
password_label = Label(text = 'Password :')
password_label.grid(row = 3 , column = 0)
##   Entry    ##
website_entry = Entry(width = 40)
website_entry.grid(row = 1,column = 1)
website_entry.focus()
email_entry = Entry(width = 40)
email_entry.grid(row = 2,column = 1)
password_entry = Entry(width = 40)
password_entry.grid(row = 3,column = 1)

##   Button   ##
password_button = Button(text = 'Generate Password',command=gen_pass)
password_button.grid(row=4,column = 1)
add_password_button = Button(text = 'add Password',command=save)
add_password_button.grid(row=4,column = 2)

window.mainloop()