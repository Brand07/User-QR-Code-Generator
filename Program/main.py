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
        self.generate_button = Button(self, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack(pady=20)

    def generate_qr_code(self):
        user_text = self.user_entry.get()
        password_text = self.password_entry.get()
        qr_data = f"{user_text}\t{password_text}\t\t\t"
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save("qrcode.png")




app = App()
app.mainloop()