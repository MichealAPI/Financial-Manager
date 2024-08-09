class Category:
    name: str
    description: str

    balance: float  # Category's balance

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

        self.balance = 0.0
