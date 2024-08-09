from abc import ABC, abstractmethod
from user import User


class MenuOption(ABC):

    @abstractmethod
    def run(self, user: User) -> None:
        pass

    @abstractmethod
    def get_desc(self) -> str:
        pass


class NewCategoryOption(MenuOption):

    def run(self, user: User) -> None:
        category_name = str(input("Insert the new category name:\n"))
        category_desc = str(input("Insert the new category description:\n"))

        user.create_category(category_name, category_desc)

    def get_desc(self) -> str:
        return "Creates a new category with a target name"


class DelCategoryOption(MenuOption):

    def run(self, user: User) -> None:
        target_category_name = str(input("Insert the target category name:\n"))

        user.delete_category(target_category_name)

    def get_desc(self) -> str:
        return "Deletes a specific category"


class AddBudgetOption(MenuOption):

    def run(self, user: User) -> None:
        target_category_name = str(input("Insert the target category name:\n"))
        amount = float(input(f"Insert the amount you want to add to category {target_category_name}:\n"))

        user.edit_budget(target_category_name, amount)

    def get_desc(self) -> str:
        return "Modifies a Category's balance by a given amount"


class SetBudgetOption(MenuOption):

    def run(self, user: User) -> None:
        target_category_name = str(input("Insert the target category name:\n"))
        amount = float(input(f"Set the balance for category {target_category_name}"))

        self.reset_balance(target_category_name, user)

        user.edit_budget(target_category_name, amount)

    def get_desc(self) -> str:
        return "Sets a specific Category's balance to a specific amount"

    def reset_balance(self, category_name: str, user: User):
        balance: float | None = user.get_balance(category_name)

        if balance is not None:
            user.edit_budget(category_name, -balance)


class PrintFormattedOption(MenuOption):

    def run(self, user: User) -> None:
        print(user)

    def get_desc(self) -> str:
        return "Categories Overview"
