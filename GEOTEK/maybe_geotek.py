# DO NOT TOUCH
import random
import pygame
from sys import exit

# important screen variables
pygame.init()
screen = pygame.display.set_mode([640,480])
pygame.display.set_caption("Geotek Maybe")
Clock = pygame.time.Clock()
font = pygame.font.Font("Grand9K Pixel.ttf", 50)

def show_score():
    score = pygame.time.get_ticks()
    score_surface = font.render(str (score), False, (255,255,0))
    score_rect = score_surface.get_rect(center = (0,0))
    screen.blit(score_surface, score_rect)
    print(score)

# images
#test_surf = pygame.Surface((100,200))
screen.fill((255,0,0))
surface_x = pygame.Surface((100,200))
#buildnumber
ver = font.render("1.1", False, (255,255,0))
text_surface =font.render("Score: ", False, (255,255,0))
Player = pygame.Surface((50,50))
Tary = pygame.Surface((100,100))
title = font.render("Play", False, (255,255,0,))
#Tary_x_position = 0
#on launch
score = 0
surface_x.set_alpha(0)
text_surface.set_alpha(0)
Player.set_alpha(0)
Tary.set_alpha(0)
previous_x, previous_y = 0, 0
x_change, y_change = 0, 0
speed = 10
Previous_tx, previous_ty = 0, 0
tx_change, ty_change = 0, 0

#rectangle
x_rect = surface_x.get_rect(center = (320, 240))
Title_rect = title.get_rect(center = (320, 230))
Ver_rect = ver.get_rect(bottomright = (620, 460))
Player_rect = Player.get_rect(topleft = (0, 0))
Tary_rect = Tary.get_rect(topleft = (10, 360))
Score_rect = text_surface.get_rect(midtop = (320, 0))
#block_rect = test_surf.get_rect(topleft = (250,125))
#image_test = pygame.image.load("ScratchCat.png").convert_alpha()

# how the game updates itself
while True:

    # how to close the game & mouse motion
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #keybord input
        if event.type == pygame.KEYDOWN:
             
            if event.key == pygame.K_LEFT:
                x_change = -speed
                y_change = 0

            if event.key == pygame.K_RIGHT:
                x_change = speed
                y_change = 0

            if event.key == pygame.K_UP:
                y_change = -speed
                x_change = 0

            if event.key == pygame.K_DOWN:
                y_change = speed
                x_change = 0

        if event.type == pygame.KEYUP:
            x_change = 0
            y_change = 0
        #if event.type == pygame.MOUSEMOTION:
            #if Player_rect.collidepoint(event.pos): print("idk")
        #if event.type == pygame.KEYDOWN:
            #if event.key == pygame.K_UP:
                #print("hello")
        #show_score()
        #keybord input

    # making the image work
    #screen.blit(image_test,(0,0))
    screen.fill((255,0,0))
    screen.blit(Tary, Tary_rect)
    #screen.blit(test_surf, block_rect)
    Tary.fill((255,155,0))
    #test_surf.fill((255,255,255))
    pygame.draw.rect(screen, (255,255,255), Score_rect, 5,)
    screen.blit(surface_x, (x_rect))
    screen.blit(text_surface, (Score_rect))
    screen.blit(Player, Player_rect)
    Player.fill((0,255,0,))
    screen.blit(ver, Ver_rect)
    screen.blit(title, Title_rect)
    
    #borders
    if Tary_rect.right >= 640:
        Tary_rect.left = 10
    if Tary_rect.left <= 0:
        Tary_rect.right = 630
    if Tary_rect.y >= 480:
        Tary_rect.y = 10
    if Tary_rect.y <= 0:
        Tary_rect.y = 470
        
    #collision
    previous_x = Player_rect.x
    previous_y = Player_rect.y

    Player_rect.x = Player_rect.x + x_change
    Player_rect.y = Player_rect.y + y_change

    if Player_rect.colliderect(x_rect):
        print("Collision")
        Player_rect.x = previous_x
        Player_rect.y = previous_y
        print(previous_x)
        
    #input mouse
    mouse_pos = pygame.mouse.get_pos()
    if Title_rect.collidepoint((mouse_pos)):
       if pygame.mouse.get_pressed() == (1, 0, 0):
           title.set_alpha(0)
           Tary.set_alpha(255)
           Player.set_alpha(255)
           text_surface.set_alpha(255)
           surface_x.set_alpha(255)
           
    #score
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        score += 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        score += 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        score += 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        score += 1
        
    #Tary Movement
    r = random.randint(1,4)
    #print(r)
    if r == 1:
        Tary_rect.y -= 10
    if r == 2:
        Tary_rect.y += 10
    if r == 3:
        Tary_rect.x += 10
    if r == 4:
        Tary_rect.x -= 10
    
    pygame.display.update()
    Clock.tick(30)