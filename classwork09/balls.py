import pygame
from pygame.draw import *
from random import randint, random
from numpy import sqrt

WHITE = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
SCREEN_SIZE = (1000, 650)
FPS = 150
V = 5


def new_ball(colors: list[tuple[int, int, int]], screen_size: tuple[int, int]):
    """
    Create new ball and draw it on the display with random color, size and position on the screen
    :param colors: list of tuples of three ints, colors in RGB
    :param screen_size: tuple of two ints, screen size
    :return: [int, int], int, (int, int, int) : position of the ball [x, y], radius of the ball r, color of the ball
    in RGB (int, int, int)
    """
    if screen_size[0] >= screen_size[1]:
        r_max = screen_size[0] // 8
    else:
        r_max = screen_size[1] // 8
    x = randint(r_max, screen_size[0] - r_max)
    y = randint(r_max, screen_size[1] - r_max)
    r = randint(r_max // 4, r_max)
    color = colors[randint(0, len(colors) - 1)]
    circle(pygame.display.set_mode(screen_size), color, (x, y), r)
    return [x, y], r, color


def click(event_0, position: [int, int], r: int):
    """
    check if the mouse click hit the target
    :param event_0: pygame.event
    :param position: [int, int], coordinates of center of the ball
    :param r: int, radius of the ball
    :return: bool, True if mouse clicked on the target or False if mouse didn't click on the target
    """
    x_0 = event_0.pos[0]
    y_0 = event_0.pos[1]
    r_0 = sqrt((x_0 - position[0])**2+(y_0 - position[1])**2)
    if r_0 <= r:
        return True
    else:
        return False


def move_ball(vec_to_move: [int, int], screen, position: [int, int], r: int, color: tuple[int, int, int],
              v: float, dposition: [int, int], dr: int):
    """
    move ball on the screen with random reflection from borders of the window and another ball
    if the move direction is null, this method will create random direction
    :param vec_to_move: [int, int], vector which defines the move direction of the ball
    :param screen: pygame.display.set_mode()
    :param position: [int, int], position of the ball which we need to move
    :param r: int, radius of the ball which we need to move
    :param color: tuple[int, int, int], color of the ball which we need to move
    :param v: float, velocity of the balls
    :param dposition: [int, int], position of another ball
    :param dr: int, radius of another ball
    :return: [float, float], [int, int] : vector which defines the move direction of the ball, new position of the ball
    """
    if vec_to_move == [0, 0]:
        while vec_to_move[0] == 0 or vec_to_move[1] == 0:
            if random() >= 0.5:
                vec_to_move[0] = random()
            else:
                vec_to_move[0] = -random()
            if random() >= 0.5:
                vec_to_move[1] = sqrt(1 - vec_to_move[0] ** 2)
            else:
                vec_to_move[1] = -sqrt(1 - vec_to_move[0] ** 2)
    x_0 = position[0] + v * vec_to_move[0]
    y_0 = position[1] + v * vec_to_move[1]
    if (x_0 + r) >= SCREEN_SIZE[0] or (x_0 - r) <= 0:
        if vec_to_move[0] >= 0:
            vec_to_move[0] = -random()
        else:
            vec_to_move[0] = random()
        if random() >= 0.5:
            vec_to_move[1] = sqrt(1 - vec_to_move[0] ** 2)
        else:
            vec_to_move[1] = -sqrt(1 - vec_to_move[0] ** 2)
    elif (y_0 + r) >= SCREEN_SIZE[1] or (y_0 - r) <= 0:
        if vec_to_move[1] >= 0:
            vec_to_move[1] = -random()
        else:
            vec_to_move[1] = random()
        if random() >= 0.5:
            vec_to_move[0] = sqrt(1 - vec_to_move[1] ** 2)
        else:
            vec_to_move[0] = -sqrt(1 - vec_to_move[1] ** 2)
    elif (position[0] - dposition[0])**2 + (position[1] - dposition[1])**2 <= (r + dr)**2:
        vec_mod = sqrt((position[0] - dposition[0])**2 + (position[1] - dposition[1])**2)
        vec_to_move[0] = (position[0] - dposition[0]) / vec_mod
        vec_to_move[1] = (position[1] - dposition[1]) / vec_mod
    position[0] = position[0] + v * vec_to_move[0]
    position[1] = position[1] + v * vec_to_move[1]
    circle(screen, color, (position[0], position[1]), r)
    return vec_to_move, position


def game_balls(screen_size: tuple[int, int], fps: int, v: int, colors: list[tuple[int, int, int]]):
    """
    Game main function
    :param screen_size: tuple of two ints, screen size
    :param fps: int, frames per second
    :param v: int, speed of balls
    :param colors: list of tuples of three ints, colors in RGB
    """
    screen = pygame.display.set_mode(screen_size)
    pygame.init()
    pygame.font.init()
    num_of_hits = 0
    num_of_misclick = 0
    hit_1 = 0
    hit_2 = 0
    vector_to_move_1 = [0, 0]
    vector_to_move_2 = [0, 0]
    position1, position2 = ([0, 0], [0, 0])
    r1, r2, color1, color2 = (0, 0, (0, 0, 0), (0, 0, 0))
    start = 1
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False
    while not finished:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if click(event, position1, r1):
                    num_of_hits = num_of_hits + 1
                    hit_1 = 1
                elif click(event, position2, r2):
                    num_of_hits = num_of_hits + 1
                    hit_2 = 1
                else:
                    num_of_misclick = num_of_misclick + 1
        if start == 1:
            position1, r1, color1 = new_ball(colors, SCREEN_SIZE)
            vector_to_move_1 = [0, 0]
            position2, r2, color2 = new_ball(colors, SCREEN_SIZE)
            vector_to_move_2 = [0, 0]
            start = 0
        else:
            if hit_1 == 1:
                position1, r1, color1 = new_ball(colors, SCREEN_SIZE)
                hit_1 = 0
                vector_to_move_1 = [0, 0]
                if hit_2 == 0:
                    vector_to_move_2, position2 = move_ball(vector_to_move_2, screen, position2, r2, color2, v,
                                                            position1, r1)
            elif hit_2 == 1:
                position2, r2, color2 = new_ball(colors, SCREEN_SIZE)
                hit_2 = 0
                vector_to_move_2 = [0, 0]
                if hit_1 == 0:
                    vector_to_move_1, position1 = move_ball(vector_to_move_1, screen, position1, r1, color1, v,
                                                            position2, r2)
            else:
                vector_to_move_1, position1 = move_ball(vector_to_move_1, screen, position1, r1, color1, v,
                                                        position2, r2)
                vector_to_move_2, position2 = move_ball(vector_to_move_2, screen, position2, r2, color2, v,
                                                        position1, r1)
        pygame.display.update()
        screen.fill(BLACK)
    print("your score: " + str(num_of_hits))
    print("number of misclicks: " + str(num_of_misclick))
    pygame.quit()


game_balls(SCREEN_SIZE, FPS, V, COLORS)
