import json
import pyperclip
from random import *
from tkinter import *
from tkinter import messagebox


# ----------------------------------------Save Password---------------------------------------------------------------
def save_pass():
    web = title_entry.get().title().strip()
    user = username_entry.get()
    password = password_entry.get()
    new_data = {
        web:
            {
                'Email/Username': user,
                'Password': password
            }
    }

    if len(web) < 1 or len(user) < 1 or len(password) < 1:
        all_ok = messagebox.askretrycancel(title='Error', message='Please do not left any filed empty !')
        if not all_ok:
            title_entry.delete(0, END)
            password_entry.delete(0, END)
            username_entry.delete(0, END)
            username_entry.insert(0, '@gmail.com')

    else:
        is_ok = messagebox.askyesno(title=web, message=f"Email/Username: {user}\nPassword: {password}\n"
                                                       f"Do you want to save it ?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)  # Reading data from the existing file
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)  # updating existing data with the new data
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)  # Saving Updated data in the file in json data formate
            finally:
                title_entry.delete(0, END)
                password_entry.delete(0, END)
                username_entry.delete(0, END)
                username_entry.insert(0, '@gmail.com')


# ----------------------------------------Password Generate-----------------------------------------------------------
def create_pass():
    password_size = int(password_size_scale.get())
    password_entry.delete(0, END)

    # Password Characters
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # Characters quantity calculation
    letters_count = randint(4, password_size - 4)
    symbols_count = randint(2, int((password_size - letters_count) / 2))
    numbers_count = password_size - letters_count - symbols_count

    password_list = ([] + choices(population=letters, k=letters_count) +
                     choices(population=symbols, k=symbols_count) +
                     choices(population=numbers, k=numbers_count))

    shuffle(password_list)
    passwords = ''.join(password_list)
    password_entry.insert(END, passwords)
    pyperclip.copy(passwords)


# ----------------------------------------Search--------------------------------------------------------------------
def search():
    search_element = title_entry.get().title().strip()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)  # Reading data from the existing file
    except FileNotFoundError:
        messagebox.showinfo(title='File Not Fount',
                            message='Please save your details first!')
    else:
        if search_element in data:
            messagebox.showinfo(title=search_element,
                                message=f'Email/Username: {data[search_element]["Email/Username"]}\n'
                                        f'Password: {data[search_element]["Password"]}')
        else:
            messagebox.showinfo(title='Invalid Input',
                                message=f'There is no title with "{search_element}"\n'
                                        f'Try with another title?')
    finally:
        title_entry.delete(0, END)
        password_entry.delete(0, END)
        username_entry.delete(0, END)
        username_entry.insert(0, '@gmail.com')


# ----------------------------------------UI Setup--------------------------------------------------------------------
# Define the color scheme
background_color = "#2E4053"  # Navy blue color for the background
label_color = "#FDFEFE"  # Crisp white color for labels to contrast the background
entry_bg_color = "#AEB6BF"  # Light silver color for entry widgets for a modern feel
entry_fg_color = "#17202A"  # Dark blue color for text in entry widgets for readability
button_color = "#D35400"  # Pumpkin orange color for buttons to stand out
button_text_color = "#FDFEFE"  # White text color for buttons for readability
canvas_color = "#CCD1D1"  # Off-white color for canvas to keep it neutral and professional

# Define custom fonts
label_font = ("Helvetica", 12)
entry_font = ("Helvetica", 12)
button_font = ("Courier", 12, "bold")

# window setup
window = Tk()
window.title('EnigmaEase-Password Management System')
window.config(bg=background_color)
window.geometry('1000x800')

# canvas setup
canvas = Canvas(width=1000, height=400, highlightthickness=0, bg='black')
img = PhotoImage(file='logo.png')
canvas.create_image(500, 200, image=img)
canvas.grid(column=0, row=0, columnspan=7)

# All Buttons
generate_password = Button(text='Generate Password', font=button_font, width=18,
                           fg=button_text_color, bg=button_color, command=create_pass)
generate_password.grid(column=2, row=4, padx=10, pady=10)

search_pass = Button(text='Search', font=button_font, width=18,
                     fg=button_text_color, bg=button_color, command=search)
search_pass.grid(column=2, row=2, padx=10, pady=10)

add_pass_into_file = Button(text='Add', font=button_font, width=53,
                            fg=button_text_color, bg=button_color, command=save_pass)
add_pass_into_file.grid(column=1, row=5, columnspan=2, padx=10, pady=10)

# All Labels

heading_title = Label(text="Let's Start", font=label_font, fg=label_color, bg=background_color)
heading_title.config(pady=50)
heading_title.grid(column=0, row=1, columnspan=5)

website = Label(text='Website: ', font=label_font, fg=label_color, bg=background_color)
website.config(padx=10, pady=10)
website.grid(column=0, row=2)

username = Label(text='Email/Username: ', font=label_font, fg=label_color, bg=background_color)
username.config(padx=10, pady=10)
username.grid(column=0, row=3)

password_title = Label(text='Password: ', font=label_font, fg=label_color, bg=background_color)
password_title.config(padx=10, pady=10)
password_title.grid(column=0, row=4)

size = Label(text='Password Size:\n(For Generating Password)',
             font=("Helvetica", 8), fg=label_color, bg=background_color)
size.config(padx=40, pady=10)
size.grid(column=4, row=2)

# All Entries
title_entry = Entry(width=36, font=entry_font, fg=entry_fg_color, bg=entry_bg_color)
title_entry.focus()
title_entry.grid(column=1, row=2, padx=5, pady=5)

username_entry = Entry(width=60, font=entry_font, fg=entry_fg_color, bg=entry_bg_color)
username_entry.insert(0, '@gmail.com')
username_entry.grid(column=1, row=3, columnspan=2, padx=5, pady=5)

password_entry = Entry(width=36, font=entry_font, fg=entry_fg_color, bg=entry_bg_color)
password_entry.grid(column=1, row=4, padx=5, pady=5)

# All Scales
password_size_scale = Scale(from_=8, to=16, length=120)
password_size_scale.grid(column=4, row=3, rowspan=4, padx=30)

window.mainloop()
