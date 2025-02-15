import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def _init_(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")
        root.configure(background="blue")

        self.title_label = tk.Label(self.root, text="To-Do List", font=("Times New Roman", 16, "bold"))
        self.title_label.pack(pady=10)

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)

        self.task_listbox = tk.Listbox(self.frame, width=40, height=15, font=("Times New Roman", 12))
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.task_entry = tk.Entry(self.root, width=30, font=("Times New Roman", 12))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", width=15, command=self.add_task)
        self.add_button.pack(pady=5)

        self.remove_button = tk.Button(self.root, text="Remove Selected Task", width=20, command=self.remove_task)
        self.remove_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Selected Task", width=20, command=self.update_task)
        self.update_button.pack(pady=5)

        self.clear_button = tk.Button(self.root, text="Clear All Tasks", width=15, command=self.clear_tasks)
        self.clear_button.pack(pady=5)

        self.tasks = []

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)  
            self.update_listbox()   
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_task_index]  
            self.update_listbox()
            messagebox.showwarning("Warning", "No task selected!")
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")
    
    def update_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            new_task = self.task_entry.get().strip()
            if new_task:  
                self.tasks[selected_task_index] = new_task  
                self.update_listbox()  
                self.task_entry.delete(0, tk.END) 
            else:
                messagebox.showwarning("Warning", "Task cannot be empty!")
        except IndexError:
            messagebox.showwarning("Warning", "No task selected!")
    
    def update_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:  
            self.task_listbox.insert(tk.END, task)

    def clear_tasks(self):
        if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?"):
            self.tasks.clear()  
            self.update_listbox()  

if __name__ == "_main_":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()