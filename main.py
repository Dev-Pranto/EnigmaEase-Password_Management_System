import json
import pyperclip
from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet
from random import randint, choices, shuffle


# ---------------------------------------- Create Key ---------------------------------------------------------------
def generate_key():
    """
    Generates a new encryption key or retrieves an existing one from 'key.key'.
    If the key is invalid or not found, it generates a new key.
    """
    try:
        with open("DON'T_Delete(Important_Files)/key.key", 'rb') as key_file:
            key = key_file.read()
            if len(key) < 5:
                raise ValueError("Invalid key found")
    except (FileNotFoundError, ValueError):
        key = Fernet.generate_key()
        with open("DON'T_Delete(Important_Files)/key.key", 'wb') as key_file:
            key_file.write(key)
    return Fernet(key)


# ---------------------------------------- Encrypt & Decrypt Functions ----------------------------------------------
def encrypt_message(message, key):
    """
    Encrypts a message using the provided key.
    :param message: The message to encrypt.
    :param key: The encryption key.
    :return: The encrypted message.
    """
    message_str = json.dumps(message)
    encrypted_message = key.encrypt(message_str.encode())
    return encrypted_message


def decrypt_message(encrypted_message, key):
    """
    Decrypts a message using the provided key.
    :param encrypted_message: The encrypted message.
    :param key: The decryption key.
    :return: The decrypted message.
    """
    decrypted_message = key.decrypt(encrypted_message).decode()
    return json.loads(decrypted_message)


# ---------------------------------------- Save Password ------------------------------------------------------------
def save_pass():
    """
    Saves a new password entry after validating the input fields.
    """
    web = title_entry.get().title().strip()
    user = username_entry.get()
    password = password_entry.get()
    url = website_entry.get()
    new_data = {
        web: {
            'Website URL': url,
            'Email/Username': user,
            'Password': password
        }
    }

    if not web or not user or not password:
        all_ok = messagebox.askretrycancel(title='Error', message='Please do not leave any field empty!')
        if not all_ok:
            reset_entries()
    else:
        is_ok = messagebox.askyesno(title=web, message=f"Website URL: {url}"
                                                       f"\nEmail/Username: {user}"
                                                       f"\nPassword: {password}"
                                                       f"\nDo you want to save it?")
        if is_ok:
            try:
                with open("DON'T_Delete(Important_Files)/data.json", "rb") as file:
                    encrypted_data = file.read()
                    if encrypted_data:
                        data = decrypt_message(encrypted_data, f)
                    else:
                        data = {}
            except FileNotFoundError:
                data = {}

            data.update(new_data)
            encrypted_data = encrypt_message(data, f)

            with open("DON'T_Delete(Important_Files)/data.json", "wb") as file:
                file.write(encrypted_data)

            reset_entries()


def reset_entries():
    """
    Resets the entry fields to default values.
    """
    title_entry.delete(0, END)
    password_entry.delete(0, END)
    username_entry.delete(0, END)
    username_entry.insert(0, '@gmail.com')
    website_entry.delete(0, END)
    website_entry.insert(0, '.com')


# ---------------------------------------- Password Generate ---------------------------------------------------------
def create_pass():
    """
    Generates a random password based on user-defined length and copies it to the clipboard.
    """
    password_size = int(password_size_scale.get())
    password_entry.delete(0, END)

    # Password Characters
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!#$%&()*+@^&-_{}[]=/'

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


# ---------------------------------------- Search -------------------------------------------------------------------
def search():
    """
    Searches for a password entry by website title.
    """
    search_element = title_entry.get().title().strip()
    try:
        with open("DON'T_Delete(Important_Files)/data.json", "rb") as file:
            encrypted_data = file.read()
            if encrypted_data:
                data = decrypt_message(encrypted_data, f)
            else:
                data = {}
    except FileNotFoundError:
        messagebox.showinfo(title='File Not Found', message='Please save your details first!')
    else:
        if search_element in data:
            messagebox.showinfo(title=search_element,
                                message=f'Email/Username: {data[search_element]["Email/Username"]}'
                                        f'\nWebsite URL: {data[search_element]["Website URL"]}'
                                        f'\nPassword: {data[search_element]["Password"]}')
            pyperclip.copy(data[search_element]["Password"])
        else:
            messagebox.showinfo(title='Invalid Input', message=f'There is no title with '
                                                               f'"{search_element}"\nTry with another title?')
    finally:
        title_entry.delete(0, END)


# ---------------------------------------- UI Setup ------------------------------------------------------------------
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

# creating key by function calling
f = generate_key()

# creating object
window = Tk()

# window setup
window.title('EnigmaEase-Password Management System')
window.config(bg=background_color)
window.geometry('1000x800')

# canvas setup
canvas = Canvas(width=1000, height=400, highlightthickness=0, bg='black')
img = PhotoImage(file='Image/logo.png')
canvas.create_image(500, 200, image=img)
canvas.grid(column=0, row=0, columnspan=7)

# All Buttons
generate_password = Button(text='Generate Password', font=button_font, width=18,
                           fg=button_text_color, bg=button_color, command=create_pass)
generate_password.grid(column=2, row=5, padx=10, pady=10)

search_pass = Button(text='Search', font=button_font, width=18,
                     fg=button_text_color, bg=button_color, command=search)
search_pass.grid(column=2, row=2, padx=10, pady=10)

add_pass_into_file = Button(text='Add', font=button_font, width=53,
                            fg=button_text_color, bg=button_color, command=save_pass)
add_pass_into_file.grid(column=1, row=6, columnspan=2, padx=10, pady=10)

# All Labels
heading_title = Label(text="Let's Start", font=label_font, fg=label_color, bg=background_color)
heading_title.config(pady=50)
heading_title.grid(column=0, row=1, columnspan=5)

website = Label(text='Website: ', font=label_font, fg=label_color, bg=background_color)
website.config(padx=10, pady=10)
website.grid(column=0, row=2)

username = Label(text='Email/Username: ', font=label_font, fg=label_color, bg=background_color)
username.config(padx=10, pady=10)
username.grid(column=0, row=4)

password_title = Label(text='Password: ', font=label_font, fg=label_color, bg=background_color)
password_title.config(padx=10, pady=10)
password_title.grid(column=0, row=5)

url_title = Label(text='Website URL: ', font=label_font, fg=label_color, bg=background_color)
url_title.config(padx=10, pady=10)
url_title.grid(column=0, row=3)

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
username_entry.grid(column=1, row=4, columnspan=2, padx=5, pady=5)

website_entry = Entry(width=60, font=entry_font, fg=entry_fg_color, bg=entry_bg_color)
website_entry.insert(0, '.com')
website_entry.grid(column=1, row=3, columnspan=2, padx=5, pady=5)

password_entry = Entry(width=36, font=entry_font, fg=entry_fg_color, bg=entry_bg_color)
password_entry.grid(column=1, row=5, padx=5, pady=5)

# All Scales
password_size_scale = Scale(from_=8, to=16, length=120)
password_size_scale.grid(column=4, row=3, rowspan=4, padx=30)

window.mainloop()
