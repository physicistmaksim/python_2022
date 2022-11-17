import math
from random import choice
import random
import pygame


FPS = 144

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

ACCELERATION = 0.05


class Ball:
    def __init__(self, screen_1, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen_1 = screen_1
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        self.x += self.vx
        self.y -= self.vy
        self.vy -= ACCELERATION

    def draw(self):
        pygame.draw.circle(
            self.screen_1,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        l1 = (self.x - obj.x)**2+(self.y-obj.y)**2
        l2 = (self.r + obj.r)**2
        if l1 <= l2:
            return True
        return False


class Gun:
    def __init__(self, screen_1):
        self.screen_1 = screen_1
        self.f2_power = 1
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self):
        self.f2_on = 1

    def fire2_end(self, event_1):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen_1)
        new_ball.r += 5
        self.an = math.atan2((event_1.pos[1]-new_ball.y), (event_1.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 1

    def targetting(self, event_1):
        """Прицеливание. Зависит от положения мыши."""
        if event_1:
            self.an = math.atan((event_1.pos[1]-450) / (event_1.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.line(self.screen_1, self.color, (20, 450), (20 + 10 * self.f2_power * math.cos(self.an), 450 +
                                                                10 * self.f2_power * math.sin(self.an)), 6)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 10:
                self.f2_power += 0.1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def __init__(self, screen_1, width, height, type_1: int):
        self.x = width - 250 + 100 * type_1
        self.y = random.randint(50, height - 50)
        self.r = random.randint(15, 50)
        self.color = RED
        self.points = 0
        self.live = 1
        self.screen_1 = screen_1
        if random.randint(0, 9) > 5:
            self.v = random.randint(20, 50)/50
        else:
            self.v = -random.randint(20, 50)/50

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(self.screen_1, self.color, (self.x, self.y), self.r)

    def move(self, height):
        self.y = self.y + self.v
        if (self.y + self.v >= height - self.r) or (self.y + self.v <= self.r):
            self.v = -self.v


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target_1 = Target(screen, WIDTH, HEIGHT, 1)
target_2 = Target(screen, WIDTH, HEIGHT, 2)
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target_1.draw()
    target_2.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
    target_1.move(HEIGHT)
    target_2.move(HEIGHT)
    for b in balls:
        b.move()
        if b.hittest(target_1) and target_1.live:
            target_1.live = 0
            target_1.hit()
            target_1 = Target(screen, WIDTH, HEIGHT, 1)
        if b.hittest(target_2) and target_2.live:
            target_2.live = 0
            target_2.hit()
            target_2 = Target(screen, WIDTH, HEIGHT, 2)
    gun.power_up()

pygame.quit()
