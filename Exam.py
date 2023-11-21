import random

class Action:
    def __init__(self, name, money, mood, health):
        self.name = name
        self.money = money
        self.mood = mood
        self.health = health

class Work(Action):
    pass

class Rest(Action):
    pass

class Person:
    def __init__(self, name="Тарас", health=100, mood=100, money=50.0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return f' - {self.name} -\n' \
               f' Здоров\'я: {self.health}\n' \
               f' Настрій: {self.mood}\n' \
               f' Капітал: {self.money}'

    def change_state(self, action):
        self.health += action.health
        self.mood += action.mood
        self.money += action.money

        # Перевіряємо, чи значення не впали нижче нуля
        if self.health < 0:
            return f"{self.name} скончався."
        if self.mood < 0:
            return f"{self.name} впав в депресію."
        if self.money < 0:
            return f"{self.name} обанкротився."

        return f"{self.name} змінив стан після {action.name}.\n{self}"

    def do(self, action):
        if type(action) == Action:
            return self.change_state(action)
        elif type(action) == Work:
            if self.mood > 90:
                action.money *= 1.1
            return self.change_state(action)
        elif type(action) == Rest:
            if self.health < 40:
                action.mood *= 0.8
            return self.change_state(action)

# Пример использования:
go_to_factory = Work(name='Пойти на завод', money=50, mood=-10, health=-3)
go_to_park = Rest(name='Сходить в парк', money=0, mood=15, health=3)
go_to_hospital = Action(name='Пойти в больницу', money=-20, mood=-5, health=20)

person = Person()

actions = [go_to_factory, go_to_park, go_to_hospital]

for _ in range(10):
    action = random.choice(actions)
    result = person.do(action)
    print(result)

    if "скончався" in result or "впав в депресію" in result or "обанкротився" in result:
        break
