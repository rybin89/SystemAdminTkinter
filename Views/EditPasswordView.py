from tkinter import *


class EditPasswordView(Tk):
    def __init__(self):
        super().__init__()
        # Конфигурацию окна
        self.title("Войти в Информационную ситему")
        self.geometry("500x500")

        # Old Password
        self.old_password = Label(self, text="Введите пароль")
        self.old_password.pack()
        # Input Password
        self.input_old_password = Entry(self)
        self.input_old_password.pack()
        # New Password
        self.new_password = Label(self, text="Введите новый пароль")
        self.new_password.pack()
        self.input_new_password = Entry(self)
        self.input_new_password.pack()
        # New NEW Password
        self.second_new_password = Label(self,text="Повторите новый пароль")
        self.second_new_password.pack()
        #Input Password
        self.input_second_new_password = Entry(self,show="*")
        self.input_second_new_password.pack()
        # Message
        self.message = Label(self, text="Тут будет сообщение")
        self.message.pack()
        # Button
        self.button = Button(self, text="Войти", command=self.clicked)
        self.button.pack()

        # method for button
    def clicked(self):
        self.message['text'] = "Я нажал на кнопку"
        self.destroy()




if __name__ == "__main__":
    window = EditPasswordView()
    window.mainloop()
