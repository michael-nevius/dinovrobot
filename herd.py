import random
from dinosaur import Dinosaur
class Herd:
    def __init__(self, name):
        self.name = name
        self.dinosaurs = [Dinosaur('Grimlock', 35), Dinosaur('Snarl', 25), Dinosaur('Sludge', 30)]
        self.active_dinosaur = None
        self.total_herd_health = 300

    def select_active_dionsaur(self):
        self.calculate_living_dinosaurs()
        if len(self.dinosaurs) >= 1:
            self.active_dinosaur = random.choice(self.dinosaurs)
    
    def calculate_herd_health(self):
        self.total_herd_health = 0
        for dinosaur in self.dinosaurs:
            self.total_herd_health += dinosaur.health

    def calculate_living_dinosaurs(self):
        for dinosaur in self.dinosaurs:
            if dinosaur.health == 0:
                self.dinosaurs.remove(dinosaur)
                print(f'{dinosaur.name} has been defeated.')