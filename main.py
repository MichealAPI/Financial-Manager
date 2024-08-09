from login_handler import LoginHandler
from menu_handler import MenuHandler

users: dict = {}


def handle_menu() -> None:
    handler = MenuHandler()

    handler.handle(users)


LoginHandler.handle_login(users)
handle_menu()


