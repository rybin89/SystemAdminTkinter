class UserController:
    '''
    Данный класс содаёт словари с Пользователями
    Меняю что-то
    '''

    def __init__(self):
        self.users = {}  # Словарь для хранения пользователей
        self.next_id = 1  # Счётчик для генерации ID (идентификатор пользователя)
        self.list_users = [
            {'user_id': 1, 'login': 'admin', 'password': '111111', 'role': 'admin','first_autch':False, 'age': 35},
            {'user_id': 2, 'login': 'user', 'password': '222222', 'role': 'user', 'first_autch':False,'status': True},
            {'user_id': 3, 'login': 'manager', 'password': '3333', 'role': 'user', 'first_autch':True}
        ] # Список словарей
        '''
        [
            {'user_id': 1, 'login': 'admin', 'password': '111111', 'role': 'admin', 'age': 35},
            {'user_id': 2, 'login': 'user', 'password': '222222', 'role': 'user', 'status': True},
            {'user_id': 3, 'login': 'manager', 'password': '3333', 'role': 'user'}
        ]
        '''
    # метод создания пользователей
    def add(self, login, password, role, **kwargs):
        # Проверка логина на уникальность
        for user_id, user_data in self.users.items():
            if user_data['login'] == login:
                return f"Пользователь с логином {login} уже существут."
        for user in self.list_users:
            if user['login'] == login:
                return f"Пользователь с логином {login} уже существут в списке."
        # Создать пользователя
        user_id = self.next_id
        self.users[user_id] = {
            "user_id": user_id,
            "login": login,
            "password": password,
            "role": role,
            **kwargs  # дополнительные поля словаря {"gender":"М"},
        }
        self.list_users.append(
            {
                "user_id": user_id,
                "login": login,
                "password": password,
                "role": role,
                **kwargs  # дополнительные поля словаря {"gender":"М"},
            }
        )
        self.next_id += 1
        return user_id

    # ВЫВЕСТИ пользователя по user_id
    def show(self, user_id): # в словаре users
        return self.users.get(user_id)

    def show_list(self,user_id): # в списке list_users
        for row in self.list_users:
            if row['user_id'] == user_id:
                return row

    # ВЫВЕСТИ пользователя по login
    def show_login(self, login):
        "Получить логин пользователя"
        for user_id, user_data in self.users.items():
            if user_data['login'] == login:
                return user_data
        return None

    def show_list_login(self,login):
        for user in self.list_users:
            if user['login'] == login:
                return user

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

    def update_user_list(self,user_id, **kwargs):
        for user in self.list_users:
            if user['user_id'] == user_id:
               # if 'login' in kwargs and self.show_list_login(kwargs['login']) is not None:
               #     return f"Пользователь с логином {kwargs['login']} уже существут."
               if 'login' in kwargs:
                   if self.show_list_login(kwargs['login']) is not None:
                        return f"Пользователь с логином {kwargs['login']} уже существут."
               user.update(kwargs)
               return True

        return f'Пользователя с id {user_id} не существует в системе.'



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

    def auth_list(self,login, password):
        user = self.show_list_login(login) # {'user_id': 4, 'login': 'manager_2', 'password': '3333', 'role': 'user'} / None
        if user and user['password'] == password:
            return user
        return None


if __name__ == "__main__":
    user = UserController()



    for row in user.list_users:
        print(row)
    print('-----------------------------')
    print(user.update_user_list(4,login = 'manager_4',password = 'manager', role= 'manager'))
    print('Аутентификация',user.auth_list('manager_4','manager'))
    print(user.show_list(4))

