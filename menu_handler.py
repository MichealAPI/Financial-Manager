import menu_options as opts
from login_handler import LoginHandler


class MenuHandler:
    options = [
        opts.AddBudgetOption(),
        opts.PrintFormattedOption(),
        opts.SetBudgetOption(),
        opts.DelCategoryOption(),
        opts.NewCategoryOption(),
        opts.AddEntry(),
        opts.ShowEntries(),
        opts.LogoutOption()
    ]

    def handle(self, sessions: dict):

        while True:

            index = 0

            for option in self.options:
                print(f"{index} - {option.__class__.__name__}: {option.get_desc()}")
                index += 1

            choice = int(input("Insert your choice:\n"))

            if choice < 0 or choice > index:
                print("Invalid choice.")
                continue

            self.options[choice].run(LoginHandler.session_user, sessions)
