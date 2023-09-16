import tkinter as tk
import customtkinter as ctk

class Settings: 
    def __init__(self):
        self.root = ctk.CTk()
        self.root.geometry("500x250")

        self.label = ctk.CTkLabel(self.root, text="Settings", font=('Arial', 20))
        self.label.pack(padx=10, pady=10)

        self.gridd = ctk.CTkFrame(self.root)
        self.gridd.columnconfigure(0, weight=1)
        self.gridd.columnconfigure(1, weight=1)

        self.time = ctk.CTkLabel(self.gridd, text="take picture every:", font=('Arial', 10))
        self.time.grid(row=0, column=0)

        self.values = ["1 min", "10 min", "1hr"]
        self.var = tk.StringVar( self.gridd, "1min")
        self.menu = ctk.CTkOptionMenu(self.gridd, self.var, *self.values)
        self.menu.grid(row=0, column=1)

        self.time = ctk.CTkLabel(self.gridd, text="accuracy", font=('Arial', 10))
        self.time.grid(row=1, column=0)

        self.values2 = ["strict", "regular", "linient"]
        self.var2 = tk.StringVar(self.gridd, "regular")
        self.menu = ctk.CTkOptionMenu(self.gridd, self.var2, *self.values2)
        self.menu.grid(row=1, column=1)

        self.values2 = ["setting 1", "setting 2", "setting 3"]
        self.var3 = tk.StringVar(self.gridd, "setting 1")
        self.menu = ctk.CTkOptionMenu(self.gridd, self.var3, *self.values2)
        self.menu.grid(row=2, column=1)

        self.name = ctk.CTkLabel(self.gridd, text="presets", font=('Arial', 10) )
        self.name.grid(row=2, column=0)

        self.name = ctk.CTkLabel(self.gridd, text="name:", font=('Arial', 10))
        self.name.grid(row=3, column=0)
        
        self.textbox = tk.Text(self.gridd, width=8, height=1)
        self.textbox.grid(row=3, column=1)


        self.gridd.pack()

        self.root.mainloop()

        
Settings()