import calendar
import time
from datetime import datetime

from category import Category


class User:
    _categories: dict
    _entries: dict

    def __init__(self):
        self._categories = {}
        self._entries = {}

    @property
    def entries(self):
        return self._entries

    def add_entry(self, entry):

        if isinstance(entry, Entry):
            target_category: Category | None = self._categories.get(entry.category_name, None)

            if target_category is None:
                print(f"No category found by the name {entry.category_name}")
                return

            if target_category.name not in self._entries:
                self._entries |= {target_category.name: []}

            current_entries: list = self._entries[target_category.name]

            current_entries.append(entry)
            self.edit_budget(target_category.name, entry.amount)

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

            result += "\n" + category.__str__()

        return result


class Entry:
    name: str
    description: str
    category_name: str
    amount: float
    timestamp: int

    def __init__(self, name, description, category_name, amount: float = 0.0):
        self.name = name
        self.description = description
        self.category_name = category_name
        self.amount = amount

        gmt = time.gmtime()
        self.timestamp = calendar.timegm(gmt)

    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nCategory: {self.category_name}\nAmount: ${self.amount}\nDate: {datetime.fromtimestamp(self.timestamp)}\n"
