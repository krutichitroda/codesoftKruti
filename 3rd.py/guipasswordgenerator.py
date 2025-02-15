import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 1:
            messagebox.showerror("Error", "Password length must be at least 1 character.")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length.")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")

def Reset_password():
    password_entry.delete(0, tk.END)
    length_entry.delete(0, tk.END)
    length_entry.insert(0, 12)
    password_entry.insert(0, "")
    messagebox.showinfo("Reset", "Password and length fields have been reset.")

def Exit():
    root.destroy()
    exit()


# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#f0f0f0")
root.geometry("600x500")

title_label = tk.Label(root, text="Password Generator", font=("Arial", 16, "bold"), fg="black")
title_label.pack()

tk.Label(root, text="Enter your Password Length").pack()
length_entry = tk.Entry(root)
length_entry.pack()
length_entry.insert(0, "12")

password_entry = tk.Entry(root, width=30)
password_entry.pack(pady=5)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=2)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.pack(pady=2)

reset_btn = tk.Button(root, text="Reset your password", command=Reset_password)
reset_btn.pack(pady=2)

exit_btn = tk.Button(root, text="Exit to App", command=Exit)
exit_btn.pack(pady=2)

root.mainloop()