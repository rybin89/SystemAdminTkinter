class RoleController:

    def __init__(self):
        self.__roles = [
            {"role_id": 1, "role": "Администратор", "description": "Управляет всей системой"},
            {"role_id": 2, "role": "Пользователь", "description": "Ограниченный доступ"},
            {"role_id": 3, "role": "Менеджер", "description": "Ограниченный доступ"},
        ]  # список ролей по умолчанию
        self.__next_id = 4 # нумерация новых role_id

    # CRUD - Create, Read, Update, Delete
    # Create - Создать запись в список
    def add(self, role, description='', **kwargs):
        # Название ролей уникальные
        for element in self.__roles:
            if element['role'] == role:
                return f'Роль с таким именем уже существует'
            # Добавить роль в спиок словарей

        self.__roles.append(
                {
                    "role_id": self.__next_id,
                    "role":role,
                    "description" :description,
                    **kwargs # "любой ключ":"значение этого ключа" в формте: любой ключ ="значение этого ключа"
                }
            )
        self.__next_id +=1
        return True

    #  Read
    #1 Вывести все записи
    # Гетер
    @property
    def roles(self):
        return self.__roles
    #2 Вывести одну запись по id
    def show(self,role_id):
        for dict in self.__roles:
            if dict['role_id'] == role_id:
                return dict
    #3 Вывести одну запись по названию роли
    def show_role(self,role):
        for dict in self.__roles:
            if dict['role'] == role:
                return dict
    # Update
    def update(self,role_id,**kwargs):
        for dict in self.__roles:
            if dict['role_id'] == role_id:
                if 'role' in kwargs:
                    if self.show_role(kwargs['role']) is not None:
                        return f'Роль с таким именем уже существует'
                dict.update(kwargs)

    # Delete
    def delete(self,role_id):
        for dict in self.__roles:
            if dict['role_id'] == role_id:
                self.__roles.remove(dict)




if __name__ == "__main__":
    role = RoleController()
    print(role.roles)
    print(role.add(role='Студент',description="Ну это студент", discilines =['Математика', 'Физика'] ,access="Сетевой город",))
    print(role.roles)
    print(role.add(role='Студент', description="Ну это студент"))
    print(role.show(2))
    print(role.update(2,role="Администратор2",description=""))
    print(role.show(2))
    role.delete(2)
    print(role.show(2))
    print(role.roles)

