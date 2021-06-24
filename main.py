from tkinter import *
from tkinter import messagebox
import random, json
from letters import letters, numbers, symbols
import pyperclip

LARGE_FONT = ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)
default_email = "masud@fb.com"

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

# This pop up displays the status of the find password button
def popupmsg_search(msg):
    popup = Tk()
    popup.wm_title("Status")
    label = Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    b1 = Button(popup, text="Close", command=popup.destroy)
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
    # pyperclip.copy(random_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) * len(password) == 0:
        messagebox.showinfo(title='Error', message='Information missing')
    else:
        try: # tries to read to check if file exists
            with open('data.json', 'r') as data_file:
                # json.dump(new_data, file, indent=2) # write to json file and indent
                # reading old data
                data = json.load(data_file)


        # if no file create one
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=2)  # write to json file and indent

        else:
            # Updating old data with new data from line 76
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                # Saving updated data to json
                json.dump(data, data_file, indent=2)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            popupmsg('Saved')


# ---------------------------- SEARCH FUNCTION ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
            webkey = data[website]
    except KeyError:
        popupmsg_search('No detail for the website exists')
    except FileNotFoundError:
        popupmsg_search('No Data File Found')
    else:
        email = webkey['email']
        password = webkey['password']
        msg = f'email:{email}\npassword{password}'
        messagebox.showinfo(title=website, message=msg)


# ---------------------------- UI SETUP ------------------------------- #
mypass_image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=mypass_image)
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
search_button = Button(window, text='Search Password', width=14, command=find_password)
search_button.grid(row=1, column=3, sticky='e')

generate_button = Button(window, text='Generate Password', width=14, command=generate_password)
generate_button.grid(row=3, column=2, sticky='w')

add_button = Button(window, text='Add', width=30, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
