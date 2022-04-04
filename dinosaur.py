class Dinosaur:
    def __init__(self, name, attack_power):
        self.name = 'Maximal Wrex'
        self.health = int(100)
        self.energy = int(150)
        self.power = int(25)

    def attack_robot(self, robot_to_attack):
        if self.energy > 10:
            print(f'{self.name} attacked {robot_to_attack.name}')
            self.energy -= 10
            robot_to_attack.health -= self.attack_power
            print(f'{self.name} energy is now {self.energy}')