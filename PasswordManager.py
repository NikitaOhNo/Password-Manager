import tkinter as tk

from Passwords import PasswordManager
from config import password, options


class GuiPasswordManager(tk.Frame, PasswordManager):
    def __init__(self, window):
        super().__init__(window)
        PasswordManager.__init__(self)


if __name__ == '__main__':
    window = tk.Tk()
    app = GuiPasswordManager(window)
    window.title('Password Manager')
    window.geometry('650x450+300+200')
    window.resizable(False, False)
    window.mainloop()
