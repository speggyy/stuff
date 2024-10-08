class WeaponSystem:
    def __init__(self, weaponName, damage):
        self.weaponName = weaponName
        self.damage = damage

    def printWeapon(self):
        print("Weapon: " + self.weaponName)
        print("Weapon Damage: " + self.damage)