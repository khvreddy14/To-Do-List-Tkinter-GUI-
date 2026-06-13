import tkinter as tk
from tkinter import messagebox
import os

DATA_FILE = "data/tasks.txt"

os.makedirs("data", exist_ok=True)

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        pass

def save_tasks():
    tasks = task_list.get(0, tk.END)

    with open(DATA_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            for task in f.readlines():
                task_list.insert(tk.END, task.strip())

def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a task!"
        )
        return

    task_list.insert(tk.END, task)
    task_entry.delete(0, tk.END)
    save_tasks()

def delete_task():
    try:
        selected = task_list.curselection()[0]
        task_list.delete(selected)
        save_tasks()

    except:
        messagebox.showwarning(
            "Warning",
            "Select a task first!"
        )

def clear_tasks():
    confirm = messagebox.askyesno(
        "Confirm",
        "Delete all tasks?"
    )

    if confirm:
        task_list.delete(0, tk.END)
        save_tasks()

# GUI Window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("500x500")
root.resizable(False, False)

title = tk.Label(
    root,
    text="📝 To-Do List",
    font=("Arial", 20, "bold")
)
title.pack(pady=10)

task_entry = tk.Entry(
    root,
    width=40,
    font=("Arial", 12)
)
task_entry.pack(pady=10)

add_btn = tk.Button(
    root,
    text="Add Task",
    width=15,
    command=add_task
)
add_btn.pack(pady=5)

task_list = tk.Listbox(
    root,
    width=50,
    height=15,
    font=("Arial", 12)
)
task_list.pack(pady=15)

delete_btn = tk.Button(
    root,
    text="Delete Selected",
    width=15,
    command=delete_task
)
delete_btn.pack(pady=5)

clear_btn = tk.Button(
    root,
    text="Clear All",
    width=15,
    command=clear_tasks
)
clear_btn.pack(pady=5)

load_tasks()

root.mainloop()
