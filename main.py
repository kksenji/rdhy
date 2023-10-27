# class a:
# total_a = 0

# def __init__(self, name, swim=False, fly=False, walk=True):

# self.name = name
# self.can_swim = swim
# self.can_fly = fly
# self.can_walk = walk


# def swim(self):
#    if self.can_swim:
#       return f"{self.name} може плавати"
#  else:
#     return f"{self.name} не може плавати."

# def fly(self):
#   if self.can_fly:
#      return f"{self.name} може літати"
#  else:
#     return f"{self.name} не може літати"

# def walk(self):
#   if self.can_walk:
#      return f"{self.name} може ходити"
# else:
#    return f"{self.name} не може ходити."


# tiger = a("Тигр", swim=False, fly=False, walk=True)
# fish = a("Риба", swim=True, fly=False, walk=False)
# duck = a("Качка", fly=True, swim=True, walk=True)

# print(tiger.swim())
# print(duck.walk())
# print(fish.fly())

# print(f"тварин у зоопарку: {a.total_a}")


class Car:
    brand = "Без назви"

    def __init__(self, color, year, speed=0, c=False, lights=False, ):
        self.color = color
        self.year = year
        self.speed = speed
        self.c = c
        self.lights = lights

    def onlights(self):
        self.lights = True
        print(f"ого я щось бачу")

    def offlights(self):
        self.lights = False
        print(f" я нічого не бачу")

    def onc(self):
        self.c = True
        print(f"холодно")

    def offc(self):
        self.c = False
        print(f"душно")

    def ride(self):
        if self.speed == 0:
            print(f"{self.color} автомобіль марки {self.brand} року {self.year} зупинився")
        else:
            print(f"{self.color} автомобіль марки {self.brand} року {self.year} їде")


car1 = Car("Cиній", 2009, c=True, lights=False)
car1.brand = "Volvo"

car2 = Car("Сшрий", 2011, lights=True, c=False)
car2.brand = "Honda"

car1.onlights()
car1.offc()
car1.ride(0)

car2.offlights()
car2.onc()
car2.ride(23)
