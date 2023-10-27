class a:
    total_a = 0

    def __init__(self, name, swim=False, fly=False, walk=True):

        self.name = name
        self.can_swim = swim
        self.can_fly = fly
        self.can_walk = walk




    def swim(self):
        if self.can_swim:
            return f"{self.name} може плавати"
        else:
            return f"{self.name} не може плавати."

    def fly(self):
        if self.can_fly:
            return f"{self.name} може літати"
        else:
            return f"{self.name} не може літати"

    def walk(self):
        if self.can_walk:
            return f"{self.name} може ходити"
        else:
            return f"{self.name} не може ходити."


tiger = a("Тигр", swim=False, fly=False, walk=True)
fish = a("Риба", swim=True, fly=False, walk=False)
duck = a("Качка", fly=True, swim=True, walk=True)

print(tiger.swim())
print(duck.walk())
print(fish.fly())

print(f"тварин у зоопарку: {a.total_a}")
