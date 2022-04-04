import random
import dinosaur
import robot
import weapon

class Battlefield:
    def __init__(self):
        self.welcome = display_welcome
        self.battle = battle_phase
        self.winner = display_winner

    def welcome(self):
        print('Welcome to Robot vs Dinosaur!')
        print('Each Robot and Dinosaur begin with 100 health.')
        print('Each begins with 100 energy/power level points')
        print('and attacking requires 10 energy/power level points.')

    def battle(self):
        first_turn = random.randint(1, 2)
        if first_turn == 1:
            print('Optimus Prime is up first, Prepare to meet your match Maximal Wrex!')
            first_turn = 1
        if first_turn == 2:
            print('Maximal Wrex is up first, Optimus Prime I have been waiting a long time for this!')
            first_turn = 2

    def dinosaur_attack(self):
        pass   

    def robot_attack(self):
        pass       
