import tkinter as tk
from tkinter import ttk

def add_contact():
    name = name_entry.get()
    email = email_entry.get()
    contact = contact_entry.get()
    optional_args = optional_args_entry.get()

    # You can add code here to save the contact data to a database or list

    # Clear the input fields
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    optional_args_entry.delete(0, tk.END)

def clear_fields():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    contact_entry.delete(0, tk.END)
    optional_args_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Contacts Manager")

# Create and pack a frame for inputs
input_frame = ttk.Frame(root, padding=10)
input_frame.grid(column=0, row=0, sticky=(tk.W, tk.E))

# Create input labels and entry fields
name_label = ttk.Label(input_frame, text="Name:")
name_label.grid(column=0, row=0, sticky=tk.W)

name_entry = ttk.Entry(input_frame, width=40)
name_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))

email_label = ttk.Label(input_frame, text="Email:")
email_label.grid(column=0, row=1, sticky=tk.W)

email_entry = ttk.Entry(input_frame, width=40)
email_entry.grid(column=1, row=1, sticky=(tk.W, tk.E))

contact_label = ttk.Label(input_frame, text="Contact:")
contact_label.grid(column=0, row=2, sticky=tk.W)

contact_entry = ttk.Entry(input_frame, width=40)
contact_entry.grid(column=1, row=2, sticky=(tk.W, tk.E))

optional_args_label = ttk.Label(input_frame, text="Optional Args:")
optional_args_label.grid(column=0, row=3, sticky=tk.W)

optional_args_entry = ttk.Entry(input_frame, width=40)
optional_args_entry.grid(column=1, row=3, sticky=(tk.W, tk.E))

# Create buttons for adding and clearing entries
add_button = ttk.Button(input_frame, text="Add Contact", command=add_contact)
add_button.grid(column=0, row=4, columnspan=2)

clear_button = ttk.Button(input_frame, text="Clear Fields", command=clear_fields)
clear_button.grid(column=0, row=5, columnspan=2)

# Start the application
root.mainloop()
