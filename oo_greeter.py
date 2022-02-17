"""Object-oriented style application extends Tk.tk"""

import tkinter as tk
from tkinter import messagebox

class GreeterApp(tk.Tk):

    def __init__(self):
        # call the superclass constructor FIRST
        super().__init__()
        self.title("Greeter")
        # use geometry to define a window size (this is hacky)
        #self.geometry("400x150")

        # add components. DO NOT write lots of tkinter code in __init__.
        self.init_components()

    def init_components(self):
        """Define components, layout the UI, and add event handlers."""
        self.username = tk.StringVar()

        label = tk.Label(self, text="Your name?")
        namefield = tk.Entry(self, width=12, textvariable=self.username)
        greet_button = tk.Button(self, text="Greet Me", command=self.greet_handler)
        # add this to also handle ENTER press on the Entry field
        #namefield.bind('<Return>', self.greet_handler)
        
        # position the components
        label.grid(row=0, column=0, padx=5, pady=5)
        namefield.grid(row=0, column=1, padx=5, pady=5)
        greet_button.grid(row=0, column=2, padx=5, pady=5)
        # make the grid stretchable
        self.columnconfigure(1, weight=1)
        namefield.grid(sticky=tk.EW)
        
        # style the components
        options = {'font': ('Arial',16)}
        namefield['foreground'] = 'blue'
        namefield['font'] = ('Monospace', 16)
        label.config(**options)
        greet_button.config(**options)


    def greet_handler(self, *args):
        """Action to perform when user presses "Greet Me" button."""
        who = self.username.get().strip()
        # clear input field for next use
        self.username.set("")
        if who:
            message = f"Hello, {who}"
            title = "Greetings"
            messagebox.showinfo(title, message)


if __name__ == '__main__':
    """Launch the application."""
    app = GreeterApp()
    app.mainloop()
