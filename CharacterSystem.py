from HealthSystem import HealthSystem
from WeaponSystem import WeaponSystem
class CharacterSystem:

    def __init__(self, name, health_system, weapon_system):
        self.name = name
        self.health = HealthSystem
        self.weapon = WeaponSystem
    def printCharacter(self):
        print(self.name)
        self.health.pcurrentHealth()
        print(self.weapon)


