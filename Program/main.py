import customtkinter
import pandas as pd
import qrcode

customtkinter.set_appearance_mode("light")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("GSN - QR Code Generator")
        self.geometry("600x400")
        self.resizable(False, False)



app = App()
app.mainloop()