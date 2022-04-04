from weapon import Weapon
class Robot:
    def __init__(self, name,) -> None:
        self.name = name
        self.health = 100
        self.active_weapon = None
        self.weapons =  [Weapon('Sword', 30) Weapon('Plasma Rifle', 50) Weapon('Tackle', 15)]
        
    def attack_dinosaur(self, dinosaur):
        self.active_weapon()
        if dinosaur.health > self.active_weapon.attack_power:
            dinosaur.health -= self.active_weapon.attack_power
            print(f'{self.name} attacked {dinosaur.name} using a {self.active_weapon.name} causing {self.active_weapon.attack_power} damage. {dinosaur.health} remaining.')

        else:
            dinosaur.health = 0

    def choose_weapon(self):
        user_input=100
        max_attacks = len(self.weapons) -1
        while user_input > max_attacks:
            n = 0
            for attack in self.weapons:
                print(f"{n} : {attack.name}")
                n += 1
            user_input = abs(int(input("Choose an attack by its number : ")))
        print("You chose " + str(self.weapons[user_input].name) + ".")
        self.active_weapon = self.weapons[user_input]

 


   
