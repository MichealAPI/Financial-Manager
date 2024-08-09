from abc import ABC, abstractmethod
from user import User, Entry
from login_handler import LoginHandler


class MenuOption(ABC):

    @abstractmethod
    def run(self, user: User, sessions: dict) -> None:
        pass

    @abstractmethod
    def get_desc(self) -> str:
        pass


class NewCategoryOption(MenuOption):

    def run(self, user: User, sessions: dict) -> None:
        category_name = str(input("Insert the new category name:\n"))
        category_desc = str(input("Insert the new category description:\n"))

        user.create_category(category_name, category_desc)

    def get_desc(self) -> str:
        return "Creates a new category with a target name"


class DelCategoryOption(MenuOption):

    def run(self, user: User, sessions: dict) -> None:
        target_category_name = str(input("Insert the target category name:\n"))

        user.delete_category(target_category_name)

    def get_desc(self) -> str:
        return "Deletes a specific category"


class AddBudgetOption(MenuOption):

    def run(self, user: User, sessions: dict) -> None:
        target_category_name = str(input("Insert the target category name:\n"))
        amount = float(input(f"Insert the amount you want to add to category {target_category_name}:\n"))

        user.edit_budget(target_category_name, amount)

    def get_desc(self) -> str:
        return "Modifies a Category's balance by a given amount"


class SetBudgetOption(MenuOption):

    def run(self, user: User, sessions: dict) -> None:
        target_category_name = str(input("Insert the target category name:\n"))
        amount = float(input(f"Set the balance for category {target_category_name}"))

        SetBudgetOption.reset_balance(target_category_name, user)

        user.edit_budget(target_category_name, amount)

    def get_desc(self) -> str:
        return "Sets a specific Category's balance to a specific amount"

    @staticmethod
    def reset_balance(category_name: str, user: User):
        balance: float | None = user.get_balance(category_name)

        if balance is not None:
            user.edit_budget(category_name, -balance)


class PrintFormattedOption(MenuOption):

    def run(self, user: User, sessions: dict) -> None:
        print(user)

    def get_desc(self) -> str:
        return "Categories Overview"


class LogoutOption(MenuOption):

    def run(self, user: User, sessions: dict) -> None:
        LoginHandler.handle_login(sessions)

    def get_desc(self) -> str:
        return "Logs out from the current session"


class ShowEntries(MenuOption):

    def run(self, user: User, sessions: dict) -> None:

        category_name = str(input("Insert the category you're looking for:\n"))

        if category_name == "":
            self.show_entries(user, True)
            return

        self.show_entries(user, False, category_name)

    @staticmethod
    def show_entries(user: User, global_view: bool, category_name: str = ""):

        if not global_view:

            entries = user.entries.get(category_name)
            print(f"Entries for category {category_name}:")

            if entries is None:
                return None

            for entry in entries:
                print(entry)

            return

        for category in user.entries:

            entries = user.entries[category]

            for entry in entries:
                print(entry)

    def get_desc(self) -> str:
        return "Show entries for a category, if selected"


class AddEntry(MenuOption):

    def run(self, user: User, sessions: dict) -> None:
        name = str(input("Input the entry name: "))
        desc = str(input("Input the description for this entry: "))
        amount = float(input("Input the amount for this entry, could be negative: "))
        category_name = str(input("Input the category for this entry: "))

        user.add_entry(Entry(name, desc, category_name, amount))

    def get_desc(self) -> str:
        return "Adds a new entry to a category"
