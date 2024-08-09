from user import User


class LoginHandler:

    session_user: User

    @classmethod
    def handle_login(cls, users_dict: dict) -> None:
        username = str(input("Insert your username\n"))

        new_account = str(input("Creating a new Account? (Y/n) "))

        if new_account == "Y" or new_account == "y":
            print("Creating a new Account...")
            users_dict |= {username: User()}

        cls.session_user = users_dict[username]
