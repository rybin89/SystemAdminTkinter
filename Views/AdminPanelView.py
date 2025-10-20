from tkinter import *
from tkinter import ttk

class AdminPanelView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Окно администратора Информационной системы")
        self.geometry('800x500')
        # frame registration
        self.registration_frame = ttk.Frame(
            self,
            borderwidth=1,
            relief=SOLID,
            padding = [8,10], # 8 - слева и справо, 10 сверху и снизу

        )
        self.registration_frame.pack(fill=X, pady=10, padx=10)
        # Login
        self.login = Label(self.registration_frame, text="Введите логин")
        self.login.pack()
        # Input Login
        self.input_login = Entry(self.registration_frame)
        self.input_login.pack()
        # Password
        self.password = Label(self.registration_frame, text="Введите пароль")
        self.password.pack()
        # Input Password
        self.input_password = Entry(self.registration_frame, show="*")
        self.input_password.pack()
        # Message
        self.message = Label(self.registration_frame, text="Тут будет сообщение")
        self.message.pack()
        # Button
        self.button = Button(self.registration_frame, text="Добавить пользователя", command=self.clicked)
        self.button.pack()

        # Table
        self.table_frame = ttk.Frame(self,
            borderwidth=1,
            relief=SOLID,
            padding = [8,10], # 8 - слева и справо, 10 сверху и снизу
        )
        self.table_frame.pack(fill=X, pady=10, padx=10)
        # method for button
        #Опредилить название столбцов
        self.columns = ("login", "password","ban")
        self.table = ttk.Treeview(self.table_frame,columns=self.columns, show="headings")
        self.table.pack()
        #Заголовки таблицы
        self.table.heading("login",text="Логин")
        self.table.heading("password",text="Пароль")
        self.table.heading("ban",text="Заблокирован")
        self.button_update = ttk.Button(self.table_frame,text="Обновить таблицу")
        self.button_update.pack(pady=10)
    def clicked(self):
        self.message['text'] = "Я нажал на кнопку"


if __name__ == "__main__":
    window = AdminPanelView()
    window.mainloop()