#!/usr/bin/python

import time
import random
from sense_hat import SenseHat
from Screen import Screen


class Snake:
    def __init__(self):
        self.sense = SenseHat()
        self.screen = Screen(self.sense)

        self.lastDirection = ''
        self.directionX = 0
        self.directionY = 0
        self.snakeLen = 0
        self.segments = []
        self.foods = []
        self.new_game()

    def new_game(self):
        self.lastDirection = ''
        self.directionX = 0
        self.directionY = 0
        self.snakeLen = 3
        self.segments = [(0, 0)]
        self.foods = []
        self.create_food(self.get_free_spaces())

    def loop(self):
        frame_count = 0
        while True:
            time.sleep(0.04)

            difficulty_skip = 6
            if self.snakeLen > 5:
                difficulty_skip = 5
            elif self.snakeLen > 15:
                difficulty_skip = 4
            elif self.snakeLen > 30:
                difficulty_skip = 3

            if frame_count % difficulty_skip == 0:
                self.update()
            self.draw()
            frame_count += 1

    def update(self):
        evts = self.sense.stick.get_events()
        for event in evts:
            self.handle_input(event.direction, event.action)

        position = (self.segments[0][0] + self.directionX, self.segments[0][1] + self.directionY)
        free_spaces = self.get_free_spaces()

        # check endgame
        if position[0] < 0 or position[1] < 0 or position[0] >= 8 or position[1] >= 8:
            self.new_game()
            return

        self.handle_food_eat(position)
        if len(self.foods) == 0:
            self.create_food(free_spaces)

        # check collision with self
        if self.lastDirection != '':
            if position not in free_spaces:
                self.new_game()
                return

        self.segments.insert(0, position)
        if len(self.segments) > self.snakeLen:
            self.segments.pop()

    def draw(self):
        self.screen.clear()
        for seg in self.segments:
            self.screen.set_pixel(255, 0, 0, seg[0], seg[1])
        for food in self.foods:
            self.screen.set_pixel(0, 255, 0, food[0], food[1])
        self.screen.update()

    def handle_input(self, direction, action):
        # ignore direction if not possible to go
        if (self.lastDirection == "up" and direction == "down") or \
                (self.lastDirection == "down" and direction == "up") or \
                (self.lastDirection == "left" and direction == "right") or \
                (self.lastDirection == "right" and direction == "left"):
            return

        if action == "pressed" or action == "held":
            if direction == "up":
                self.directionY = -1
                self.directionX = 0
            elif direction == "down":
                self.directionY = 1
                self.directionX = 0
            elif direction == "left":
                self.directionY = 0
                self.directionX = -1
            elif direction == "right":
                self.directionY = 0
                self.directionX = 1
        self.lastDirection = direction

    def handle_food_eat(self, snake_pos):
        for food in self.foods:
            if food[0] == snake_pos[0] and food[1] == snake_pos[1]:
                self.snakeLen += 1
                self.foods.remove(food)
                return

    def create_food(self, free_spaces):
        space = random.choice(free_spaces)
        self.foods.append(space)

    def get_free_spaces(self):
        spaces = []
        for x in range(0, 8):
            for y in range(0, 8):
                if self.is_space_free((x, y)):
                    spaces.append((x, y))
        return spaces

    def is_space_free(self, pos):
        for seg in self.segments:
            if seg[0] == pos[0] and seg[1] == pos[1]:
                return False
        return True


if __name__ == '__main__':
    print "SNAKE!"
    Snake().loop()
