import random
from robot import Robot
class Fleet:
    
    def __init__(self, name) -> None:
        self.name = name
        self.robots = [Robot('Optimus Prime'), Robot('Bumble Bee'), Robot('Jazz')]
        self.active_robot = None
        self.total_fleet_health = 300
        self.living_robots = []

    def select_active_robot(self):
        self.calculate_living_robots()
        if len(self.robots) >= 1:
            self.active_robot = random.choice(self.robots)
            print(f'{self.active_robot.name} is going to attack.')

    def calculate_fleet_health(self):
        self.total_fleet_health = 0
        for robot in self.robots:
            self.total_fleet_health += robot.health
    
    def calculate_living_robots(self):
        for robot in self.robots:
            if robot.health == 0:
                self.robots.remove(robot)
                print(f'{robot.name} has been detroyed in battle, please help the auto bots.')