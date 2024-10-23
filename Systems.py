class Character:
    def __init__(self, name, health_system, weapon_system):
        self.name = name
        self.health = health_system
        self.weapon = weapon_system

    def printCharacter(self):
        print(f"Name: {self.name}")
        print(f"Max Health: {self.health.pmaxHealth()}")
        print(f"Current Health: {self.health.pcurrentHealth()}")
        print(f"Weapon: {self.weapon.pName()}")
        print(f"Weapon Damage: {self.weapon.pDamage()}")

class Health:
    def __init__(self, maxHealth, currentHealth):
        self.maxHealth = maxHealth
        self.currentHealth = currentHealth

    def pmaxHealth(self):
        return self.maxHealth

    def pcurrentHealth(self):
        return self.currentHealth

    def printHealth(self):

        if self.currentHealth < 1 or self.maxHealth < 1:
            print("--Dead--")
        else:
            if self.currentHealth <= self.maxHealth:
                healthFalse = self.maxHealth - self.currentHealth

                for i in range(self.currentHealth):
                    print("■", end="")

                for i in range(healthFalse):
                    print("□", end="")

                print("")
            else:
                overHealth = self.currentHealth - self.maxHealth

                for i in range(self.maxHealth):
                    print("■", end="")

                print("|", end="")

                for i in range(overHealth):
                    print("▣", end="")

                print("")

    def takeDamage(self, damageAmount):
        self.currentHealth = self.currentHealth - damageAmount

    def healHealth(self, healAmount):
        self.currentHealth = self.currentHealth + healAmount

class Weapon:
    def __init__(self, weaponName, damage):
        self.weaponName = weaponName
        self.damage = damage

    def pName(self):
        return self.weaponName

    def pDamage(self):
        return self.damage

