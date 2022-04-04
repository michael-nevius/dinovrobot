from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot_name = 'Optimus Prime'
        self.dinosaur_name = 'Maximal Wrex'
        self.weapon = "Sword"
        

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()   

    def display_welcome(self):
        print(f'Welcome to Robot vs Dinosaur! Who will be the winner {self.robot_name} or {self.dinosaur_name}?')
            

    def battle_phase(self):
        user_input = input(int)('The choice is yours please enter "1" for Optimus Prime or "2" for Maximal Wrex: ')
        

