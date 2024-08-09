class Category:
    name: str
    description: str

    balance: float  # Category's balance

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

        self.balance = 0.0

    def __str__(self):
        result = f"Category name: {self.name}\n"

        result += f"Category Description: {self.description}\n"

        result += f"Category Balance: ${self.balance}\n"

        return result
