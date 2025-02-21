class Expense:
    def __init__(self,amount,name,category) -> None:
        self.amount = amount
        self.name = name
        self.category = category
    def __repr__(self):
        return f"<Expense: {self.name} , ${self.amount:.2f} , {self.category} >"