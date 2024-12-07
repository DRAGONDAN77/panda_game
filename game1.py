import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.money = 1
        self.previous_gladness = 50
        self.previous_progress = 0
        self.previous_money = 1
        self.alive = True
    def to_study(self):
        print("Time to study")
        self.previous_gladness = self.gladness
        self.previous_progress = self.progress
        self.progress += 0.10
        self.gladness -= 3
    def to_sleep(self):
        print("Time to sleep")
        self.previous_gladness = self.gladness
        self.gladness += 3
    def to_chill(self):
        print("Time to chill")
        self.previous_gladness = self.gladness
        self.previous_progress = self.progress
        self.previous_money = self.money
        self.gladness += 5
        self.progress -= 0.5
        self.money -= 3
    def to_work(self):
        print("Time to sleep")
        self.previous_gladness = self.gladness
        self.previous_progress = self.progress
        self.progress += 2
        self.money += 5
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression...")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally...")
            self.alive = False
        elif self.money <= -5:
            print("Homeless")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
        print(f"Money = {self.money}")
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        import random

        if ((self.previous_progress - self.progress) <= (self.previous_money - self.money)) or (
                (self.previous_progress - self.progress) <= (self.previous_gladness - self.gladness)):
            a = random.randint(0, 1)
            if a == 1:
                self.to_sleep()
            else:
                self.to_study()

        elif (self.previous_gladness - self.gladness) <= (self.previous_money - self.money):
            a = random.randint(0, 1)
            if a == 1:
                self.to_sleep()
            else:
                self.to_chill()
        else:
            self.to_work()

        self.end_of_day()
        self.is_alive()
nick = Student(name="Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)