#config.py
TITLE = "Мое первое окно"
WIDTH = 800
HEIGHT = 600
ICON = "main_window.ico"

#controller.py
import user_repository
def auth_user(login,password):
    user = user_repository.get_user_by_login(login.strip())
    message:str="Доступ запрещен"
    if user is None:
        pass
    else:
        if user.check_password(password.strip()):
            message = f"Привет - {user.get_name()}"
    print(message)

#User.py
class User:
    def __init__(self,login,password,fio):
        self._login = login
        self._password = password
        self._fio = fio
    def check_password(self,password):
        return password == self._password
    def get_name(self):
        return self._fio
    def get_login(self):
        return self._login

  #user_repository.py
from User import User
users = [
    User("admin","admin","Михаил Ануфрев"),
    User("winter", "is_near", "Джон Сноу"),
    User("jane", "password", "Джейн Смит"),
    User("bob", "secret123", "Боб Джонс"),
    User("susan", "p@ssw0rd", "Сьюзан Вонг"),
]
users_repos = {user.get_login(): user for user in users}
def get_user_by_login(login):
    return users_repos.get(login)

#view.py
import tkinter as tk
from config import *
import controller

main_window = tk.Tk()
main_window.title(TITLE)
main_window.geometry(f"{WIDTH}x{HEIGHT}")
main_window.iconbitmap(ICON)

tk.Label(main_window, text="Логин").pack()
login_text = tk.Text(main_window, width=15, height=1)
login_text.pack()

tk.Label(main_window, text="Пароль").pack()
password_text = tk.Text(main_window, width=15, height=1)
password_text.pack()

auth_button = tk.Button(main_window, text="Войти",command=lambda: controller.auth_user(login_text.get(1.0, tk.END), password_text.get(1.0, tk.END)))
auth_button.pack()
if __name__ == "__main__":
    main_window.mainloop()
