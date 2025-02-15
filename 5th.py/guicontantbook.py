import json
import os
import tkinter as tk
from tkinter import messagebox, scrolledtext

ALL_BOOK = "content.json"

def load_content():
    if os.path.exists(ALL_BOOK):
        with open(ALL_BOOK, "r") as file:
            return json.load(file)
    return []

def add_content():
    title = title_entry.get()
    content = content_text.get("1.0", tk.END).strip()
    
    if title and content:
        contents = load_content()
        contents.append({"title": title, "content": content})
        save_content(contents)
        update_listbox()
        title_entry.delete(0, tk.END)
        content_text.delete("1.0", tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both Title and Content.")

def save_content(contents):
    with open(ALL_BOOK, "w") as file:
        json.dump(contents, file, indent=4)

def update_listbox():
    content_listbox.delete(0, tk.END)
    contents = load_content()
    for item in contents:
        content_listbox.insert(tk.END, item['title'])

def view_content():
    try:
        selected_index = content_listbox.curselection()[0]
        contents = load_content()
        selected_item = contents[selected_index]
        title_entry.delete(0, tk.END)
        content_text.delete("1.0", tk.END)
        title_entry.insert(0, selected_item['title'])
        content_text.insert("1.0", selected_item['content'])
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select an entry to view.")

def delete_content():
    try:
        selected_index = content_listbox.curselection()[0]
        contents = load_content()
        del contents[selected_index]
        save_content(contents)
        update_listbox()
        title_entry.delete(0, tk.END)
        content_text.delete("1.0", tk.END)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select an entry to delete.")

root = tk.Tk()
root.title("Simple Content Book")

tk.Label(root, text="Title:").grid(row=0, column=0, sticky="w")
title_entry = tk.Entry(root, width=30)
title_entry.grid(row=0, column=1)

tk.Label(root, text="Content:").grid(row=1, column=0, sticky="nw")
content_text = scrolledtext.ScrolledText(root, width=30, height=10)
content_text.grid(row=1, column=1)

tk.Button(root, text="Add Content", command=add_content).grid(row=2, column=0, columnspan=2)
tk.Button(root, text="View Content", command=view_content).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="Save Content", command=save_content).grid(row=3, column=0, columnspan=2)
tk.Button(root, text="Delete Content", command=delete_content).grid(row=4, column=0, columnspan=2)

content_listbox = tk.Listbox(root, width=50)
content_listbox.grid(row=5, column=0, columnspan=2)

update_listbox()

root.mainloop()
