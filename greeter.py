import tkinter as tk
from tkinter import messagebox

# A top-level window
root = tk.Tk()
root.title("Greeter")
# omit this to create the smallest window that fits components
#root.geometry("400x150")


def greet_handler(*args):
    """Event handler that is invoked by events on Button and Entry field."""
    message = f"Hello, {username.get()}"
    title = "Greetings"
    messagebox.showinfo(title, message)
    # clear the input field
    username.set("")

# Add components to the layout
label = tk.Label(root, text="Your name?")
# A variable to get the value from the namefield
username = tk.StringVar()
namefield = tk.Entry(root, width=12, textvariable=username)
greet_button = tk.Button(root, text="Greet Me", command=greet_handler)

# position the components
label.grid(row=0, column=0, padx=5, pady=5)
namefield.grid(row=0, column=1, padx=5, pady=5)
greet_button.grid(row=0, column=2, padx=5, pady=5)

# style the components - there are many ways to do this.
options = {'font': ('Arial',16)}
namefield['foreground'] = 'blue'
namefield['font'] = ('Monospace', 16)
label.config(**options)
greet_button.config(**options)

# display the root window and listen for events
root.mainloop()
