from tkinter import *

from Views.EditPasswordView import EditPasswordView


class AuthView(Tk):
    def __init__(self):
        super().__init__()
        # Конфигурацию окна
        self.title("Войти в Информационную ситему")
        self.geometry("500x500")

        # Login
        self.login = Label(self, text="Введите логин")
        self.login.pack()

        # Input Login

        self.input_login = Entry(self)
        self.input_login.pack()
        # Password
        self.password = Label(self, text="Введиет пароль")
        self.password.pack()
        # Input Password
        self.input_password = Entry(self, show="*")
        self.input_password.pack()
        # Message
        self.message = Label(self, text="Тут будет сообщение")
        self.message.pack()
        # Button
        self.button = Button(self, text="Войти", command=self.clicked)
        self.button.pack()

        # method for button

    def clicked(self):
        self.message['text'] = "Я нажал на кнопку"
        edit = EditPasswordView()


if __name__ == "__main__":
    window = AuthView()
    window.mainloop()
