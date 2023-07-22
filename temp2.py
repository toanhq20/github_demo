import pygame
from pygame.locals import *

# init

pygame.init()

screen_width = 600
screen_height = 500

# fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# define font
font = pygame.font.SysFont('Constantia', 30)

# define game variables
margin = 50
cpu_score = 0
player_score = 0
# fps = 60
# define colors
bg = (50, 25, 50)
white = (255, 255, 255)


def draw_board():
    screen.fill(bg)
    pygame.draw.line(screen, white, (0, margin), (screen_width, margin))


def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))


class paddle():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = Rect(self.x, self.y, 20, 100)
        self.speed = 5

    # def move(self):
    #     key = pygame.key.get_pressed()
    #     if key[pygame.K_UP] and self.rect.top > margin:
    #         self.rect.move_ip(0, -1*self.speed)
    #     if key[pygame.K_DOWN] and self.rect.bottom < screen_height:
    #         self.rect.move_ip(0, 1*self.speed)

    def draw(self):
        pygame.draw.rect(screen, white, self.rect)
# creat paddles


player_paddle = paddle(screen_width - 40, screen_height // 2)
cpy_paddle = paddle(20, screen_height // 2)

run = True
while run:
    # fpsClock.tick(fps)
    draw_board()
    draw_text('CPU: ' + str(cpu_score), font, white, 20, 15)
    draw_text('P1: ' + str(player_score), font, white, screen_width - 100, 15)

    # draw paddle
    player_paddle.draw()
    cpy_paddle.draw()

    # move paddle
    # player_paddle.move()
    for event in pygame.event.get():  # all events
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()
