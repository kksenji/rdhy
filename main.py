import random

import self


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.mood = 0
        self.car_condition = 0
        self.money = 100
        self.c = 0
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car
    def chill(self):
        self.mood += 10
        self.c += 5

    def clean_home(self):
        self.mood -= 5
        self.c = 0

    def to_repair(self):
        self.car_condition += 100
        self.money -= 50

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
    def __init__(self, mood, c, money, car_condition):
        self.mood = mood
        self.c = c
        self.money = money
        self.car_condition = car_condition

    def chill(self):
        self.mood += 10
        self.c += 5

    def clean_home(self):
        self.mood -= 5
        self.c = 0

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
