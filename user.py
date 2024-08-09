from category import Category


class User:

    _categories: dict

    def __init__(self):
        self._categories = {}

    @property
    def budgets(self) -> dict:
        return self._budgets

    @budgets.setter
    def set_budgets(self, budgets: dict):
        self._budgets = budgets

    def set_budget(self, category_name: str, amount: float) -> None:
        self._budgets |= {category: amount}

    def edit_budget(self, category_name: str, amount: float) -> float | None:

        category: Category = self.get_or_default(self._categories, category_name, self.create_category(category_name))

    def create_category(self, name: str, description: str = "No Description") -> Category:
        result = Category(name, description, )
        self._categories |= {name: result}

        return result


    def delete_category(self, name: str) -> None:
        target_category: Category | None = User.get_or_default(self._categories, name, None)

        if target_category is None:
            print(f"Cannot delete category {target_category}")
            return

        print("Deleting category...")
        for category in self._categories:

            if category == target_category:  # Recursive deletion
                del self._categories[category]

        del self._categories[name]

        print(f"...deleted successfully {target_category.name} along with its own budgets")

    @staticmethod
    def get_or_default(dictionary: dict, key, default_value):
        value = dictionary.get(key)

        if value is None:
            return default_value

        return value
