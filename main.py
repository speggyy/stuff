from CharacterSystem import CharacterSystem
from HealthSystem import HealthSystem
from WeaponSystem import WeaponSystem

playerHealth = HealthSystem(5, 6)
dagger = WeaponSystem("Dagger", 1)
character = CharacterSystem("Ethan", playerHealth, dagger)

playerHealth.pmaxHealth()
playerHealth.pcurrentHealth()
character.printCharacter()