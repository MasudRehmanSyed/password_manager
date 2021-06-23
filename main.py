from tkinter import *
from tkinter import messagebox
import random
import pyperclip
LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
default_email = "masud@fb.com"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
nr_letters = random.randint(8, 10)
nr_symbols = random.randint(2, 4)
nr_numbers = random.randint(2, 4)

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50, bg='white')

canvas = Canvas(window, width=200, height=200, bg='white', highlightthickness=0)


def popupmsg(msg):
    popup = Tk()
    popup.wm_title("Status")
    label = Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    b1 = Button(popup, text="Okay", command=popup.destroy)
    b1.pack()
    popup.mainloop()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for char in range(nr_numbers)]
    random.shuffle(password_list)
    random_password = "".join(password_list)

    password_entry.insert(0, random_password)
    password_list.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    w = website_entry.get()
    e = email_entry.get()
    p = password_entry.get()
    if len(w) * len(p) == 0:
        messagebox.showinfo(title='Error', message='Information missing')
    else:
        if messagebox.askokcancel(title='Information', message=f"{w} website is okay to save \n email:{e}\n"
                                                               f"password:{p}"):
            with open('data.txt', 'a') as f:
                f.write(f'{w} | {e} | {p}\n')

                website_entry.delete(0, END)
                password_entry.delete(0, END)
            popupmsg('Saved')


# ---------------------------- UI SETUP ------------------------------- #
mypass_image = PhotoImage(file='logo.png')
canvas.create_image(50, 100, image=mypass_image)
canvas.grid(row=0, column=1)

# Labels only
website = Label(text='Website:')
website.grid(row=1, column=0)

username = Label(text='Email/Username:')
username.grid(row=2, column=0)

password = Label(text='Password:')
password.grid(row=3, column=0)

# Entry box
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, default_email)
password_entry = Entry(width=17)
password_entry.grid(row=3, column=1)

# Button
generate_button = Button(window, text='Generate Password', width=14, command=generate_password)
generate_button.grid(row=3, column=2, sticky='w')

add_button = Button(window, text='Add', width=30, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
