class Toy:
    def __init__(self, name, color, height):
        self.name = name
        self.color = color
        self.height = height

    def __str__(self):
        return f"This is a {self.color} {self.name} toy."

    def __len__(self):
        return self.height


toy_figure = Toy("barbie", "pink", 5)

print(toy_figure)       # calls __str__
print(len(toy_figure))  # calls __len__