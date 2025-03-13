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

#Player
player_img = pygame.image.load('siplayer.png')
player_x = player_start_x
player_y = player_start_y
player_x_change = 0

#Enemy Setup
enemy_img = []
enemy_x = []
enemy_y = []
enemy_x_change = []
enemy_y_change = []
num_of_enemy = 6

for _ in range(num_of_enemy):
    enemy_img.append(pygame.image.load('sienemy.png'))
    enemy_x.append(random.randint(0,screen_width-64))
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

def player(x,y):
    screen.blit(player_img,(x,y))

def enemy(x,y,i):
    screen.blit(enemy_img[i],(x,y))   

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_tmg,(x+16,y+10))

def isCollision(enemy_x,enemy_y,bullet_x,bullet_y):
    distance = math.sqrt((enemy_x - bullet_x)**2 + (enemy_x - bullet_y)**2)
    return distance < collision_distance

running = True
background = pygame.image.load('sibg.png')

while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x_change = -5
            if event.key == pygame.K_RIGHT:
                player_x_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x
                fire_bullet(bullet_x,bullet_y)
        if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
            player_x_change = 0
    player_x += player_x_change
    player_y = max(0,min(player_x,screen_width-64))

    for i in range(num_of_enemy):
        if enemy_y[i] > 340:
            for j in range(num_of_enemy):
                enemy_y[j] = 2000
            game_over_text()
            break
        enemy_x[i] += enemy_x_change[i]
        if enemy_x[i] <= 0 or enemy_x[i] >= screen_width - 64:
            enemy_x_change *= -1
            enemy_y[i] += enemy_y_change[i]
        if isCollision(enemy_x[i],enemy_y[i],bullet_x,bullet_y):
            bullet_y = player_start_y
            bullet_state = "ready"
            score_value += 1
            enemy_x[i] = random.randint(0,screen_width-64)
            enemy_y[i] = random.randint(enemy_start_y_min,eneme_start_y_max)
        enemy(enemy_x[i],enemy_y[i],i)
    if bullet_y <= 0:
        bullet_y = player_start_y
        bullet_state == "ready"
    elif bullet_state == "fire":
        fire_bullet(bullet_x,bullet_y)
        bullet_y -= bullet_y_change
    player(player_x,player_y)
    show_score(text_x,text_y)

    pygame.display.update()