import math
import random
import pygame

#constants
screen_width = 800
screen_height = 500
player_start_x = 370
player_start_y = 380
enemy_start_y_min = 50
eneme_start_y_max = 150
enemy_speed_x = 4 
enemy_speed_y = 40
bullet_speed_y = 10
collision_distance = 27

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('siufo.png')
pygame.display.set_icon(icon)

#Enemy Setup
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemy = 6

for _ in range(num_of_enemy):
    enemy_img.append(pygame.image.load('sienemy.png'))
    enemy_x.append(random.randint(o,screen_width-64))
    enemy_y.append(random.randint(enemy_start_y_min,eneme_start_y_max))
    enemy_x_change.append(enemy_speed_x)
    enemy_y_change.append(enemy_speed_y)

#Bullet
bullet_tmg = pygame.image.load('sibullet.png')
bullet_x = 0
bullet_y = player_start_y
bullet_x_change = 0
bullet_y_change = bullet_speed_y
bullet_state = "ready"

score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
text_x = 10
text_y = 10
over_font = pygame.font.Font("freesansbold.ttf",64)

def show_score(x,y):
    display_score = font.render("Score: "+ str(score_value),True,(255,255,255))
    screen.blit(display_score,(x,y))

def game_over_text():
    over_text = over_font.render("Game Over",True,(255,255,255))
    screen.bilt(over_text,(200,250))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.display.update()