import tkinter as tk
from tkinter import PhotoImage
import random
import string
import pyperclip
import subprocess

def on_password_length_change(*args):
    new_length = password_length_var.get()
    if new_length.isdigit():
        password_length_var.set(min(int(new_length), 128))
    else:
        password_length_var.set(8)

def increase_password_length():
    password_length = int(password_length_var.get())
    password_length_var.set(min(password_length + 1, 128))

def decrease_password_length():
    password_length = int(password_length_var.get())
    password_length_var.set(max(password_length - 1, 8))

def generate_password():
    password_length = int(password_length_var.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(password_length))
    generated_password_label.config(text="Generated Password:")
    generated_password_value.config(text=password)
    pyperclip.copy(password)

def exit_app():
    root.destroy()

def open_credits_script():
    subprocess.Popen(["python", "credits_script.py"])

root = tk.Tk()
root.title("PassCraft")
root.geometry('500x700')
root.iconbitmap("image_res/icon.ico")
root.configure(bg='#34495e')

password_length_var = tk.StringVar(value="8")
password_length_var.trace_add("write", on_password_length_change)

# Load images
copy_img = PhotoImage(file='image_res/copy_img.png')
pwd_gen_img = PhotoImage(file='image_res/pwd_gen_img.png')
exit_img = PhotoImage(file='image_res/exit_img.png')

# Header
header_label = tk.Label(root, text="PassCraft - Password Generator", font=('Segoe UI', 18, 'bold'), bg='#34495e', fg='#ecf0f1')
header_label.pack(pady=20)

# Password length entry and buttons
password_length_frame = tk.Frame(root, bg='#34495e')
password_length_frame.pack(pady=10)

password_length_label = tk.Label(password_length_frame, text="Password Length (8-128):", font=('Segoe UI', 12), bg='#34495e', fg='#ecf0f1')
password_length_label.pack(side='left', padx=10)

password_length_entry = tk.Entry(password_length_frame, textvariable=password_length_var, font=('Segoe UI', 12))
password_length_entry.pack(side='left', padx=10)

plus_button = tk.Button(password_length_frame, text='+', command=increase_password_length, font=('Segoe UI', 10))
plus_button.pack(side='left')

minus_button = tk.Button(password_length_frame, text='-', command=decrease_password_length, font=('Segoe UI', 10))
minus_button.pack(side='left')

# Generate password button
generate_button = tk.Button(root, image=pwd_gen_img, command=generate_password, bg='#34495e', borderwidth=0)
generate_button.pack(pady=20)


# Generated password
generated_password_label = tk.Label(root, text="Generated Password:", font=('Segoe UI', 12), bg='#34495e', fg='#ecf0f1')
generated_password_label.pack()

generated_password_value = tk.Label(root, text="", font=('Segoe UI', 14, 'bold'), bg='#34495e', fg='#27ae60')
generated_password_value.pack()

# Copy password button
copy_button = tk.Button(root, image=copy_img, command=pyperclip.copy, bg='#34495e', borderwidth=0)
copy_button.pack(pady=10)

# Exit button
exit_button = tk.Button(root, image=exit_img, command=exit_app, bg='#34495e', borderwidth=0)
exit_button.pack(pady=20)

# Credits button
credits_button = tk.Button(root, text="Credits", font=('Segoe UI', 10), fg="#ffffff", bg="#2980b9", command=open_credits_script)
credits_button.pack(side='bottom', fill='x')

root.mainloop()

