from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        print("Меч рубит!")

class Bow(Weapon):
    def attack(self):
        print("Стрела полетела!")

class Fighter():
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def fight(self):
        print(self.weapon.attack())

class Monster():
    pass

sword1 = Sword()
bow1 = Bow()

fighter = Fighter(sword1)
fighter.fight()
fighter.changeWeapon(bow1)
fighter.fight()