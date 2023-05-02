# topline


import sys, pygame, spritesheet
from random import randint

#! Game core function
pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("2d Adventure Runner")
clock = pygame.time.Clock()
font_test = pygame.font.Font('Pixeltype.ttf', 50)
keys = pygame.key.get_pressed
game_active = False
start_time = 0
score = 0
BLUE = (0,255,255)

#* Game Controls
enemy_speed = 5.5 #Default = 5


#! Background
Sky_surface = pygame.image.load('Images/Background-Scene/Sky.png').convert()
ground_surface = pygame.image.load('Images/Background-Scene/ground.png').convert()

#! Enemy
enemy_unit1 = pygame.image.load('Images/Sprite Enemy/Wolf(Edit).png').convert_alpha()
enemy_unit1 = pygame.transform.scale(enemy_unit1,(100,50))
nu1_x_pos = 600
nu1_y_pos = 290
enemy1_rect = enemy_unit1.get_rect(center=(nu1_x_pos,nu1_y_pos))
enenmy1_rect = enemy1_rect.inflate(-60,0)
#? if size = 150,100 then x= 600 y = 230

enemy_unit2 = pygame.image.load("Images/Sprite Enemy/Blue_Bird.png").convert_alpha()
enemy_unit2 = pygame.transform.scale(enemy_unit2,(100,50))


#! Enemy Function
obstacle_rect_list = []

#! Player
player1_surf = pygame.image.load('Images/Sprite Player/Adventurer-1.5/Individual Sprites/adventurer-idle-00.png').convert_alpha()
player1_surf = pygame.transform.scale(player1_surf,(125,100))

p1_x_pos = 80
p1_y_pos = 300

player1_rect = player1_surf.get_rect(center=(p1_x_pos,p1_y_pos))
player1_rect = player1_rect.inflate(-60,0)

player1_gravity = 0

#! Intro Screen
player1_stand = pygame.image.load('Images/Sprite Player/Adventurer-1.5/Individual Sprites/adventurer-idle-00.png').convert_alpha()
player1_stand = pygame.transform.scale(player1_stand,(200,150))
player1_stand_rect = player1_stand.get_rect(center=(400,200))

game_name = font_test.render("2d Adventure Runner", False, (111,196,169))
game_name_rect = game_name.get_rect(center=(400,80))

game_message = font_test.render("Press Space to Play", False, (111,196,169))
game_message_rect = game_message.get_rect(center=(400,320))

#! Obstacle Timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

#! Define

def Display_Score():
    current_time = int(pygame.time.get_ticks() / 1000) - start_time
    score_surf = font_test.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center=(400,50))
    screen.blit(score_surf,score_rect)
    return current_time

def Obstacle_Movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            obstacle_rect = obstacle_rect.inflate(-60,0)
            
            if obstacle_rect.bottom > 300:
                screen.blit(enemy_unit1,obstacle_rect)
            else:
                screen.blit(enemy_unit2,obstacle_rect)
                
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > - 100]
        
        return obstacle_list
    else:
        return []

def Collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect):
                return False
    return True

#! Game
while True:
    #? Controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:   
            if event.type == pygame.MOUSEBUTTONDOWN:
                if (player1_rect.collidepoint(event.pos)) and (player1_rect.bottom == 305):
                    player1_gravity = -20
                    
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE) and (player1_rect.bottom == 305):
                    player1_gravity = -20
                    
            if event.type == pygame.KEYUP:
                print("1")
                
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rect_list.append(enemy_unit1.get_rect(center=(randint(900,1100),nu1_y_pos)))
                else:
                    obstacle_rect_list.append(enemy_unit2.get_rect(center=(randint(900,1100),180)))
        else:
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_SPACE):
                    enemy1_rect.right = 600
                    game_active = True
                    start_time = int(pygame.time.get_ticks() / 1000)
                
        
    #? Controls end       
    if game_active:
        screen.blit(Sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))    
        
        
        obstacle_rect_list = Obstacle_Movement(obstacle_rect_list)
        score = Display_Score()
        
        player1_gravity += 1
        player1_rect.y += player1_gravity
        if player1_rect.bottom >= 305:
            player1_rect.bottom = 305

        screen.blit(player1_surf,player1_rect)
        game_active = Collisions(player1_rect,obstacle_rect_list)

    else:
        screen.fill((94,129,162))
        screen.blit(player1_stand,player1_stand_rect)
        obstacle_rect_list.clear()
        
        player1_rect.midbottom = (80,300)
        player1_gravity = 0
        
        message_score = font_test.render(f"Your Score: {score}",False, (111,196,169))
        message_score_rect = message_score.get_rect(center=(400,320))
        screen.blit(game_name,game_name_rect)
        
        version = font_test.render("Alpha - 0.5",False,(255,255,255))
        version_rect = version.get_rect(center=(100,380))
        screen.blit(version,version_rect)
        
        if score == 0:
            screen.blit(game_message,game_message_rect)
        else:
            screen.blit(message_score,message_score_rect)
            
    pygame.display.update()
    clock.tick(60)
    
    