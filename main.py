from user import User
from menu_handler import MenuHandler

users = {}
session_user: User | None = None


def handle_login() -> None:
    global users, session_user

    username = str(input("Insert your username"))

    if username in users:
        session_user = users[username]
    else:
        users |= {username: User()}
        session_user = users[username]


def handle_menu() -> None:
    global session_user

    handler = MenuHandler()

    handler.handle(session_user)


handle_login()
handle_menu()
