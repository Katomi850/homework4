import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 1
        self.alive = True
        self.money = 20

    def to_study(self):
        self.progress += 0.12
        self.gladness -= 5
        print("Time to study")

    def to_sleep(self):
        self.gladness += 3
        print("Time to sleep")

    def to_chill(self):
        self.gladness += 5
        self.progress -= 0.1
        self.money -= 0.1
        print("Time to chill")

    def to_work(self):
        self.gladness -= 0.5
        self.money += 50
        print("Time to work")

    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness < 0:
            print("Depression")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally ...")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {self.progress}")
        print(f"Money = {self.money}")

    def live(self, day):
        day = "Day " + str(day) + " of " + self.name + " life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 4)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        elif live_cube == 4:
            self.to_work()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Nick")

for day in range(1, 365):  # 364 дні
    nick.live(day)
