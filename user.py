from category import Category


class User:
    _categories: dict

    def __init__(self):
        self._categories = {}

    def get_categories(self) -> dict:
        return self._categories

    def get_balance(self, category_name: str) -> float | None:
        target_category: Category | None = self._categories.get(category_name, None)

        if target_category is None:
            print(f"No category found by the name {category_name}")
            return

        return target_category.balance

    def edit_budget(self, category_name: str, amount: float) -> None:

        target_category: Category | None = self._categories.get(category_name, None)

        if target_category is None:
            print(f"No category found by the name {category_name}")
            return

        target_category.balance += amount
        print(f"New balance: {target_category.balance}")

    def create_category(self, name: str, description: str = "No Description") -> Category:
        result = Category(name, description)
        self._categories |= {name: result}

        return result

    def delete_category(self, name: str) -> None:
        target_category: Category | None = self._categories.get(name, None)

        if target_category is None:
            print(f"Cannot delete category {target_category}")
            return

        print("Deleting category...")
        for category in self._categories:

            if category == target_category:  # Recursive deletion
                del self._categories[category]

        del self._categories[name]

        print(f"...deleted successfully {target_category.name} along with its own budgets")

    def __str__(self):

        result = ""

        for category_name in self._categories:

            category: Category = self._categories[category_name]

            result += category.__str__()

        return result