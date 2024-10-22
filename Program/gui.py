import customtkinter as ctk

class Button(ctk.CTkButton):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(font=("Arial", 14))
        self.configure(fg_color="blue")
        self.configure(width=150)

class Entry(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(font=("Arial", 14))
        self.configure(width=150)

