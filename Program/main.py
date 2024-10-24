import customtkinter
import pandas as pd
import qrcode
from gui import Button, Entry
from PIL import Image, ImageWin, ImageTk
import win32print
import win32ui

customtkinter.set_appearance_mode("light")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("GSN - QR Code Generator v0.1")
        self.geometry("600x500")
        self.resizable(False, False)
        self.user_entry = Entry(self, placeholder_text="Username")
        self.user_entry.pack(pady=20)
        self.password_entry = Entry(self, placeholder_text="Password", show="*")
        self.password_entry.pack(pady=20)
        self.print_option = customtkinter.CTkCheckBox(self, text="Print QR Code")
        self.print_option.pack(pady=20)
        self.generate_button = Button(self, text="Generate QR Code", command=self.generate_qr_code)
        self.generate_button.pack(pady=20)
        self.label_width = 150
        self.label_height = 150



        #Display the QR Code Image
        self.qr_label = customtkinter.CTkLabel(self, text="")
        self.qr_label.pack()



    def generate_qr_code(self):
        user_text = self.user_entry.get()
        if user_text == "":
            print("Username is required.")
        password_text = self.password_entry.get()
        if password_text == "":
            print("Password is required.")
        qr_data = f"{user_text}\t{password_text}\t\t\t\t"
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(qr_data)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        img.save(f"QR_Codes/{user_text}.png")
        self.clear_entries()

        if self.print_option.get() == 1:
            self.print_image(f"QR_Codes/{user_text}.png", self.label_width, self.label_height)
            img_tk = ImageTk.PhotoImage(img)
            # Display the QR Code in the GUI
            self.qr_label.configure(image=img_tk)
            self.qr_label.image = img_tk
        else:
            print("QR Code generated but not printed.")
            # Display the QR Code in the GUI
            img_tk = ImageTk.PhotoImage(img)
            self.qr_label.configure(image=img_tk)
            self.qr_label.image = img_tk




    def clear_entries(self):
        """Clears the username and password entry fields"""
        self.user_entry.delete(0, "end")
        self.password_entry.delete(0, "end")

    def print_image(self, file_name, label_width, label_height):
        """Prints the image to the default Windows printer"""
        try:
            printer_name = win32print.GetDefaultPrinter()
            hDC = win32ui.CreateDC()
            hDC.CreatePrinterDC(printer_name)

            # Define the label size in pixels
            label_size = (label_width, label_height)

            bmp = Image.open(file_name)
            bmp = bmp.resize(label_size, Image.LANCZOS)

            hDC.StartDoc(file_name)
            hDC.StartPage()
            dib = ImageWin.Dib(bmp)
            dib.draw(hDC.GetHandleOutput(), (0, 0, label_size[0], label_size[1]))
            hDC.EndPage()
            hDC.EndDoc()
            hDC.DeleteDC()
        except Exception as e:
            print(f"Error printing image: {e}")
            pass





app = App()
app.mainloop()