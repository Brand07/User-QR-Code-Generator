import customtkinter
import pandas as pd
import qrcode
from gui import Button, Entry

customtkinter.set_appearance_mode("light")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("GSN - QR Code Generator")
        self.geometry("600x400")
        self.resizable(False, False)
        self.user_entry = Entry(self, placeholder_text="Username")
        self.user_entry.pack(pady=20)
        self.password_entry = Entry(self, placeholder_text="Password")
        self.password_entry.pack(pady=20)
        self.generate_button = Button(self, text="Generate QR Code")
        self.generate_button.pack(pady=20)




app = App()
app.mainloop()