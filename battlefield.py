from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot_name = 'Optimus Prime'
        self.dinosaur_name = 'Maximal Wrex'
        self.robot_weapon = 'Sword'
        self.dinosaur = 'Bite'
        

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

        elif user_input == int(2):
            print(f'It looks like {self.robot_name} is going to make the first attack!')    
   


    def display_winner(self):

        

