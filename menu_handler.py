import menu_options as opts
from user import User


class MenuHandler:
    options = [
        opts.AddBudgetOption(),
        opts.PrintFormattedOption(),
        opts.SetBudgetOption(),
        opts.DelCategoryOption(),
        opts.NewCategoryOption()
    ]

    def handle(self, session_user: User):

        while True:

            index = 0

            for option in self.options:
                print(f"{index} - {option.__class__.__name__}: {option.get_desc()}")
                index += 1

            choice = int(input("Insert your choice:\n"))

            if choice < 0 or choice > index:
                print("Invalid choice.")
                continue

            self.options[choice].run(session_user)
