from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []


    [password_list.append(random.choice(letters)) for _ in range(nr_letters)]

    [password_list.append(random.choice(symbols)) for _ in range(nr_symbols)]

    [password_list.append(random.choice(numbers)) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0 , password)

    pyperclip.copy(password)

# ---------------------------- SEARCH METHOD ------------------------------- #

def find_password():
    website = website_input.get()
    try:
        with open("data.json" , "r") as data_file :
            data = json.load(data_file)
            try:
                messagebox.showinfo(title=website , message=f"email : {data[website]["email"]} \n password : {data[website]["password"]}")
            except KeyError :
                messagebox.showerror(title="Error" , message="Couldn't find a website by given name !")
    except FileNotFoundError :
        messagebox.showerror(title="Error" , message="No Data File Found")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    new_data = {
        website_input.get():{
            "email" : email_input.get(),
            "password" : password_entry.get()
    }}

    if len(email_input.get()) < 1 or len(password_entry.get()) < 1 or len(website_input.get()) < 1 :
        messagebox.showerror(title="Error" , message="Remember not to left a entry empty !!")
    else:
        try:
            with open("data.json" , "r") as data_file :
                data = json.load(data_file)
        except FileNotFoundError :
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json" , "w") as data_file:
                json.dump(data , data_file , indent=4)
        finally:
            website_input.delete(0 , 'end')
            password_entry.delete(0 , 'end')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("password")
window.config(padx=50 , pady=50)


# LOGO
canvas = Canvas(width=200 , height=200 , highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100 , 100 , image= photo)
canvas.grid(column = 1 , row=0)

# WEBSITE
website_name = Label(text="Website:")
website_name.grid(column = 0 , row= 1)
website_input = Entry(width= 21)
website_input.focus()
website_input.grid(row= 1 ,column = 1)

# USERNAME AND EMAIL
email_name = Label(text="Email/Username:")
email_name.grid(row = 2 , column = 0)
email_input = Entry(width=35)
email_input.insert(0 , "example@gmail.com")
email_input.grid(row=2 , column = 1 , columnspan = 2)

# PASSWORD
password_text = Label(text="Password:")
password_text.grid(row = 3 , column = 0)
password_entry = Entry(width=21 )
password_entry.grid(row= 3 , column= 1)

# PASSWORD GENERATOR
generate_button = Button(text="Generate" , width=10 , command=generate_password )
generate_button.grid(row= 3 , column = 2)

# ADD TO TXT FILE
add_button = Button(text="Add" , width=36 , command=save)
add_button.grid(row= 4 , column = 1 , columnspan= 2)

# SEARCH BUTTON
search = Button(text= "search" , width=10 , command= find_password)
search.grid(row = 1 , column = 2)

window.mainloop()
