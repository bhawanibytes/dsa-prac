class Bird:
    def sound(self):
        print("Chirp chirp")


class Cat:
    def sound(self):
        print("Meow")

# Same method, different behavior
for _ in [Bird(), Cat()]:
    _.sound()
