import tkinter as tk

def button_click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + value)

def clear():
    entry.delete(0, tk.END)


def evaluate():
    try:
        expression = entry.get()
        result = eval(expression)  
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")


root = tk.Tk()
root.title("My calculator")
root.geometry("400x400")
root.configure(background="black")


entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(columnspan=4, padx=10, pady=10)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),
    ('0', 4, 1), ('+', 1, 3), ('-', 2, 3),
    ('*', 3, 3), ('/', 4, 3),
    ('C', 4, 0), ('=', 4, 2)
]
for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 20), command=clear)
    elif text == '=':
        button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 20), command=evaluate)
    else:
         button = tk.Button(root, text=text, width=10, height=2, font=("Arial", 20), command=lambda value=text: button_click(value))
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()