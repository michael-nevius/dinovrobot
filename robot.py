from weapon import Weapon
class Robot:
    def __init__(self, name,) -> None:
        self.name = "Optimus Prime"
        self.health = 100
        self.choose_weapon = None
        self.weapons = [Weapon('Sword', 30)]
        
    def attack_dinosaur(self, dinosaur):
        self.choose_weapon()
        if dinosaur.health > self.choose_weapon.attack_power:
            dinosaur.health -= self.choose_weapon.attack_power
            print(f'{self.name} attacked {dinosaur.name} using a {self.choose_weapon.name} causing {self.choose_weapon.attack_power} damage. {dinosaur.health} remaining.')

        else:
            dinosaur.health = 0

 


   
