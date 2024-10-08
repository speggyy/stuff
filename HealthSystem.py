class HealthSystem:
    def __init__(self, maxHealth, currentHealth):
        self.maxHealth = maxHealth
        self.currentHealth = currentHealth

    def pmaxHealth(self):
        print(self.maxHealth)

    def pcurrentHealth(self):
        print(self.currentHealth)

    def printHealth(self):

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
