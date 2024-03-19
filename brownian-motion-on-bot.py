import random
import numpy as np
import pygame

class Robot:
    def __init__(self, arena_size, start_pos=(0.5, 0.5), start_dir=0):
        self.arena_size = arena_size
        self.position = np.array(start_pos)
        self.direction = start_dir
        self.collision = False

    def move(self, speed):
        new_position = self.position + speed * np.array([np.cos(self.direction), np.sin(self.direction)])

        self.collision = False
        if new_position[0] < 0:
            new_position[0] = 0
            self.collision = True 
        elif new_position[0] > self.arena_size:
            new_position[0] = self.arena_size
            self.collision = True
        if new_position[1] < 0:
            new_position[1] = 0
            self.collision = True
        elif new_position[1] > self.arena_size:
            new_position[1] = self.arena_size
            self.collision = True

        self.position = new_position

    def rotate(self, min_angle=-45, max_angle=45):
        angle = random.uniform(min_angle, max_angle) * np.pi / 180
        self.direction += angle
        self.collision = False  


arena_size = 1.0
num_steps = 1000
speed = 0.001

robot = Robot(arena_size)

pygame.init()

screen_width = int(arena_size * 500)
screen_height = screen_width
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Brownian Motion Simulation")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not robot.collision:
        robot.move(speed)
    else:
        robot.rotate()

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLACK, (0, 0, screen_width, screen_height), 5)

    robot_pos = (int(robot.position[0] * screen_width), int(robot.position[1] * screen_height))
    pygame.draw.circle(screen, RED, robot_pos, 7)

    pygame.display.flip()

pygame.quit()
