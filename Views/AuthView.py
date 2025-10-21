from tkinter import *

from Views.AdminPanelView import AdminPanelView
from Views.EditPasswordView import EditPasswordView
from Controllers.UserController import UserController

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
        '''
        Должен получить данные из self.input_login и self.input_password
        Эти данные передать в UserController в метод auth_list
        :returns:
            если данные пустые - вывести сообщение "Введите логин и пароль",
            если неверный логин или пароль - вывести сообщение "Вы ввели неверный логин и пароль",
            если логин и пароль верный и  first_autch == True- открыть окно класса EditPasswordView,
            если логин и пароль верный и role == admin - открыть окно класса AdminPanelView,
        '''
        login = self.input_login.get()
        password = self.input_password.get()

        if login == '' or password == '':
            self.message['text'] = "Введите логин и пароль"
        user = UserController() # создаём экземпляр класса UserController
        data_user = user.auth_list(login, password)

        if data_user is None:
            self.message['text'] = "Вы ввели неверный логин или пароль"
        if data_user and data_user['first_autch']:# data_user not None and  first_autch == True
            window = EditPasswordView()
        if data_user['role'] == 'admin':
            window = AdminPanelView()
        self.message['text'] = f"{login} Вы вошли в систему"

if __name__ == "__main__":
    window = AuthView()
    window.mainloop()
