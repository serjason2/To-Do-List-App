import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Task List
        self.tasks = []

        # Create Widgets
        self.create_widgets()

    def create_widgets(self):
        # Entry widget for new tasks
        self.entry = tk.Entry(self.root, width=40)
        self.entry.pack(pady=10)

        # Button to add task
        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        # Listbox to display tasks
        self.listbox = tk.Listbox(self.root, height=10, width=50)
        self.listbox.pack(pady=10)

        # Buttons for deleting and marking tasks
        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.entry.get()
        if task:
            self.tasks.append(task)
            self.listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task")

    def delete_task(self):
        try:
            selected_task_index = self.listbox.curselection()[0]
            self.listbox.delete(selected_task_index)
            del self.tasks[selected_task_index]
        except IndexError:
            messagebox.showwarning("Delete Error", "No task selected")

# Create the main application window
root = tk.Tk()
app = ToDoApp(root)
root.mainloop()