from weapon import Weapon

class Robot:
    def __init__(self, name, Weapon):
        self.name = "Optimus Prime"
        self.health = int(100)
        self.power = int(100)
        self.weapon = Weapon
        
    def attack_dinosaur(self, dinosaur_to_attack):
        if self.power > 20:
            print(f'{self.name} attacked{dinosaur_to_attack.name}')
            self.power -= 20
            dinosaur_to_attack.health -= self.weapon.attackpower
            print(f'{self.name} power level is now {self.power}')
   
