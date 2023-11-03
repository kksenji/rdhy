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


# class Car:
#   brand = "Без назви"

#  def __init__(self, color, year, speed=0, c=False, lights=False, ):
# self.color = color
# self.year = year
# self.speed = speed
# self.c = c
# self.lights = lights

# def onlights(self):
#   self.lights = True
#  print(f"ого я щось бачу")

# def offlights(self):
#   self.lights = False
#  print(f" я нічого не бачу")

# def onc(self):
#   self.c = True
#  print(f"холодно")

# def offc(self):
#   self.c = False
#  print(f"душно")

# def ride(self):
#   if self.speed == 0:
#      print(f"{self.color} автомобіль марки {self.brand} року {self.year} зупинився")
# else:
#    print(f"{self.color} автомобіль марки {self.brand} року {self.year} їде")


# car1 = Car("Cиній", 2009, c=True, lights=False)
# car1.brand = "Volvo"

# car2 = Car("Сшрий", 2011, lights=True, c=False)
# car2.brand = "Honda"

# car1.onlights()
# car1.offc()
# car1.ride(0)

# car2.offlights()
# car2.onc()
# car2.ride(23)


import random

import self


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

    def home(self):
        self.home = House

    def car(self):
        self.car = Auto(brands)

    def job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = self.job(job_list)


h = Human('Alex', True)
print(h.job)


class House:
    def __init__(self):
        mess = 0
        food = 0


class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("The car cannot move!")
            return False


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']


class Sims:
    def __init__(self, mood, clutter, money, car_condition):
        self.mood = mood
        self.clutter = clutter
        self.money = money
        self.car_condition = car_condition

    def chill(self):
        self.mood += 10
        self.clutter += 5

    def clean_home(self):
        self.mood -= 5
        self.clutter = 0

    def to_repair(self):
        self.car_condition += 100
        self.money -= 50


job_list = {
    "Java developer": {"salary": 50, "gladness_less": 10},
    "Python developer": {"salary": 40, "gladness_less": 3},
    "C++ developer": {"salary": 60, "gladness_less": 25},
    "Rust developer": {"salary": 70, "gladness_less": 15},
}

brands = {
    "BMW": {"fuel": 100, "strength": 100, "consumption": 6},
    "Lada": {"fuel": 50, "strength": 40, "consumption": 10},
    "Volvo": {"fuel": 80, "strength": 150, "consumption": 8},
    "Ferrari": {"fuel": 80, "strength": 120, "consumption": 14}
}
