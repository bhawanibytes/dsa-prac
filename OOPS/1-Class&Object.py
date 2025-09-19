class car:
    # init is default function in python class for constructor
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def drive(self):
        print(f"{self.color} {self.brand} is driving")


car1 = car("Tesla", "Red")
car2 = car("Mahindra", "BlackEagle")

car1.drive()
car2.drive()
