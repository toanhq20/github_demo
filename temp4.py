import pygame
from pygame.locals import *

# init

pygame.init()

screen_width = 600
screen_height = 500

fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

# define font
font = pygame.font.SysFont('Constantia', 30)

# define game variables
margin = 50
cpu_score = 0
player_score = 0
fps = 60
winner = 0
live_ball = False
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
        self.ai_speed = 5

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_UP] and self.rect.top > margin:
            self.rect.move_ip(0, -1*self.speed)
        if key[pygame.K_DOWN] and self.rect.bottom < screen_height:
            self.rect.move_ip(0, 1*self.speed)

    def draw(self):
        pygame.draw.rect(screen, white, self.rect)

    def ai(self):
        # ai to move the paddle automatically
        # move down
        if self.rect.centery < pong.rect.top and self.rect.bottom < screen_height:
            self.rect.move_ip(0, self.ai_speed)
        # move up
        if self.rect.centery > pong.rect.bottom and self.rect.top > margin:
            self.rect.move_ip(0, -1 * self.ai_speed)
# creat paddles


class ball():
    def __init__(self, x, y):
        # self.x = x
        # self.y = y
        # self.ball_rad = 8
        # self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        # self.speed_x = -4
        # self.speed_y = 4
        # self.winner = 0  # 1 means player 1 has scored, -1 means CPU has scored
        self.reset(x, y)

    def move(self):
        # add collision dectection
        # check collision with top margin
        if self.rect.top < margin:
            self.speed_y *= -1
        # check collision with bottom of the screen
        if self.rect.bottom > screen_height:
            self.speed_y *= -1

        if self.rect.colliderect(player_paddle) or self.rect.colliderect(cpy_paddle):
            self.speed_x *= -1

        # check for out of bounds
        if self.rect.left < 0:
            self.winner = 1
        if self.rect.right > screen_width:
            self.winner = -1

        # update ball position
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.winner

    def draw(self):
        pygame.draw.circle(screen, white, (self.rect.x + self.ball_rad,
                           self.rect.y + self.ball_rad), self.ball_rad)

    def reset(self, x, y):
        self.x = x
        self.y = y
        self.ball_rad = 8
        self.rect = Rect(self.x, self.y, self.ball_rad * 2, self.ball_rad * 2)
        self.speed_x = -4
        self.speed_y = 4
        self.winner = 0  # 1 means player 1 has scored, -1 means CPU has scored


# create pong ball
pong = ball(screen_width - 60, screen_height // 2 + 50)
player_paddle = paddle(screen_width - 40, screen_height // 2)
cpy_paddle = paddle(20, screen_height // 2)

run = True
while run:
    fpsClock.tick(fps)
    draw_board()
    draw_text('CPU: ' + str(cpu_score), font, white, 20, 15)
    draw_text('P1: ' + str(player_score), font, white, screen_width - 100, 15)

    # draw paddle
    player_paddle.draw()
    cpy_paddle.draw()

    if live_ball == True:
        # move ball
        winner = pong.move()
        if winner == 0:
           # move paddle
            player_paddle.move()
            cpy_paddle.ai()

            # draw ball
            pong.draw()

        else:
            live_ball = False
            if winner == 1:
                player_score += 1
            elif winner == -1:
                cpu_score += 1

    print(winner)
    for event in pygame.event.get():  # all events
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN and live_ball == False:
            live_ball = True
            pong.reset(screen_width - 60, screen_height // 2 + 50)

    pygame.display.update()
pygame.quit()
# kkkk
