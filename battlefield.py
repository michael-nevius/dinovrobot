from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot_name = 'Optimus Prime'
        self.dinosaur_name = 'Maximal Wrex'
        self.robot_weapon = 'Sword'
        self.dinosaur = 'Bite'
        self.power = 100

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()   

    def display_welcome(self):
        print(f'Welcome to Robot vs Dinosaur! Who will be the winner {self.robot_name} or {self.dinosaur_name}?')
            

    def battle_phase(self):
        user_input = input(int)('The choice is yours please enter "1" for Optimus Prime or "2" for Maximal Wrex: ')

        if user_input == int(1):
            print(f'It looks like {self.dinosaur_name} is going to make the first attack!')
            self.energy > 10:
            print(f'{self.name} attacked {self.robot_name}')
            self.energy -= 10
            self.robot_name.health -= self.attackpower
            print(f'{self.dinosaur_name} energy is now {self.energy}')
            print(f'{self.robot_name} health is now {self.robot_name.health}')
        
        elif user_input == int(2):
            self.power > 10:
            print(f'{self.robot_name} attacked {self.dinosaur_name}')
            self.power -= 10
            self.dinosaur_name.health -= self.weapon.attackpower
            print(f'{self.dinosaur_name} power level is now {self.power}')
            print(f'{self.dinosaur_name} health is now {self.dinosaur_name.health}')


    def display_winner(self):

        

