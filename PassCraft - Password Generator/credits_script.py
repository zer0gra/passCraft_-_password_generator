import tkinter as tk
from tkinter import PhotoImage

def close_credits_window():
    credits_window.destroy()

# Window Setup
credits_window = tk.Tk()
credits_window.title("PassCraft - Credits")
credits_window.geometry('500x400')
credits_window.iconbitmap("image_res/icon.ico")


# Load images

exit_credits_img = PhotoImage(file='image_res/exit_credits_img.png')

# Label
credits_label = tk.Label(credits_window, text="Credits: _puls3, zerogravity._.", font=('Helvetica', 20))
credits_label.pack(pady=20)


# Close button
close_button = tk.Button(credits_window, image=exit_credits_img, command=close_credits_window)
close_button.place(x=55, y=230)

credits_window.mainloop()
