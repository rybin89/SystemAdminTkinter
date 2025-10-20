class UserController:
    '''
    Данный класс содаёт словари с Пользователями
    '''

    def __init__(self):
        self.users = {}  # Словарь для хранения пользователей
        self.next_id = 1  # Счётчик для генерации ID (идентификатор пользователя)

    # метод создания пользователей
    def add(self, login, password, role, **kwargs):
        # Проверка логина на уникальность
        for user_id, user_data in self.users.items():
            if user_data['login'] == login:
                return f"Пользователь с логином {login} уже существут."
        # Создать пользователя
        user_id = self.next_id
        self.users[user_id] = {
            "user_id": user_id,
            "login": login,
            "password": password,
            "role": role,
            **kwargs  # дополнительные поля словаря {"gender":"М"},
        }
        self.next_id += 1
        return user_id

    # ВЫВЕСТИ пользователя по user_id
    def show(self, user_id):
        return self.users.get(user_id)

    # ВЫВЕСТИ пользователя по login
    def show_login(self, login):
        "Получить логин пользователя"
        for user_id, user_data in self.users.items():
            if user_data['login'] == login:
                return user_data
        return None

    def update_user(self, user_id,
                    **kwargs):  # **kwargs - login = 'new_login' / password = 'new_pssword', role = 'new_role'
        if user_id not in self.users:
            return f"Пользователь с ид {user_id} не существует."
        user = self.users[user_id]
        # проверка логина на уникальность
        if 'login' in kwargs:
            for user_id, user_data in self.users.items():
                if user_data['login'] == kwargs['login']:
                    return f"Пользователь с логином {kwargs['login']} уже существут."

        user.update(kwargs)  # {"login" : 'new_login'}  user["login"] = "new_login"
        return True

    # удалить пользователя
    def delete_user(self, user_id):
        if user_id not in self.users:
            return f"Пользователь с ид {user_id} не существует."
        else:
            del self.users[user_id]
            return True

    # Аутентификация - проверка пользователя на существование в словаре и если он там есть, то соотвесвует его пароль данному логину
    def auth(self,login, password):
        user = self.show_login(login)
        if user and user["password"] == password:
            return user
        return None


if __name__ == "__main__":
    user = UserController()

    user_1 = user.add(
        login="admin",
        password="111111",
        role="admin",
        age=35
    )
    user_2 = user.add(
        login="user",
        password="222222",
        role="user",
        status=True
    )
    print("**************")
    user_3 = user.add(
        login="manager",
        password="3333",
        role="user",
    )

    print(user.auth('admin1','111111'))
    print(user.users)
