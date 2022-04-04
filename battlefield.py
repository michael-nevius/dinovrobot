from dinosaur import Dinosaur
from robot import Robot

class Battlefield:
    def __init__(self):
        self.robot_name = Robot
        self.dinosaur_name = Dinosaur
               

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()   

    def display_welcome(self):
        print(f'Welcome to Robot vs Dinosaur! Who will be the winner {self.robot_name} or {self.dinosaur_name}?')
            

    def battle_phase(self):
        while self.robot_name and self.dinosaur_name:
            if len(self.robot_name) >= 1:
                self.robot_name.attack_dinosaur
            else:
                break
            if len(self.dinosaur_name) >= 1:
                self.dinosaur_name.attack_robot
            else:
                break
                
    

    def display_winner(self):
        if len(self.dinosaur_name) == 0:
            print(f"{self.dinosaur_name} has defeated {self.robot_name}.")
        else:
            print(f"{self.robot_name} has defeated {self.dinosaur_name}.")
