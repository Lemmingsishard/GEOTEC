import pygame
import json
import sys
pygame.init()

#important, this engine supports only 160 tiles more tiles will be added with time

#using tile editor 0 = yes
var = 0

#new data, dont touch unless you are willing to loose all tile data! 1 = loose data
nd = 0

#tile in use
tiu = 0

#something archaic
tick = 1

screen = pygame.display.set_mode((650, 500))
pygame.display.set_caption("GEOTEC")

font = pygame.font.Font("Grand9K Pixel.ttf", 30)

data = {
    "t1d" : 0,
    "t2d" : 0,
    "t3d" : 0,
    "t4d" : 0,
    "t5d" : 0,
    "t6d" : 0,
    "t7d" : 0,
    "t8d" : 0,
    "t9d" : 0,
    "t10d" : 0,
    "t11d" : 0,
    "t12d" : 0,
    "t13d" : 0,
    "t14d" : 0,
    "t15d" : 0,
    "t16d" : 0,
    "t17d" : 0,
    "t18d" : 0,
    "t19d" : 0,
    "t20d" : 0,
    "t21d" : 0,
    "t22d" : 0,
    "t23d" : 0,
    "t24d" : 0,
    "t25d" : 0,
    "t26d" : 0,
    "t27d" : 0,
    "t28d" : 0,
    "t29d" : 0,
    "t30d" : 0,
    "t31d" : 0,
    "t32d" : 0,
    "t33d" : 0,
    "t34d" : 0,
    "t35d" : 0,
    "t36d" : 0,
    "t37d" : 0,
    "t38d" : 0,
    "t39d" : 0,
    "t40d" : 0,
    "t41d" : 0,
    "t42d" : 0,
    "t43d" : 0,
    "t44d" : 0,
    "t45d" : 0,
    "t46d" : 0,
    "t47d" : 0,
    "t48d" : 0,
    "t49d" : 0,
    "t50d" : 0,
    "t51d" : 0,
    "t52d" : 0,
    "t53d" : 0,
    "t54d" : 0,
    "t55d" : 0,
    "t56d" : 0,
    "t57d" : 0,
    "t58d" : 0,
    "t59d" : 0,
    "t60d" : 0,
    "t61d" : 0,
    "t62d" : 0,
    "t63d" : 0,
    "t64d" : 0,
    "t65d" : 0,
    "t66d" : 0,
    "t67d" : 0,
    "t68d" : 0,
    "t69d" : 0,
    "t70d" : 0,
    "t71d" : 0,
    "t72d" : 0,
    "t73d" : 0,
    "t74d" : 0,
    "t75d" : 0,
    "t76d" : 0,
    "t77d" : 0,
    "t78d" : 0,
    "t79d" : 0,
    "t80d" : 0,
    "t81d" : 0,
    "t82d" : 0,
    "t83d" : 0,
    "t84d" : 0,
    "t85d" : 0,
    "t86d" : 0,
    "t87d" : 0,
    "t88d" : 0,
    "t89d" : 0,
    "t90d" : 0,
    "t91d" : 0,
    "t92d" : 0,
    "t93d" : 0,
    "t94d" : 0,
    "t95d" : 0,
    "t96d" : 0,
    "t97d" : 0,
    "t98d" : 0,
    "t99d" : 0,
    "t100d" : 0,
    "t101d" : 0,
    "t102d" : 0,
    "t103d" : 0,
    "t104d" : 0,
    "t105d" : 0,
    "t106d" : 0,
    "t107d" : 0,
    "t108d" : 0,
    "t109d" : 0,
    "t110d" : 0,
    "t111d" : 0,
    "t112d" : 0,
    "t113d" : 0,
    "t114d" : 0,
    "t115d" : 0,
    "t116d" : 0,
    "t117d" : 0,
    "t118d" : 0,
    "t119d" : 0,
    "t120d" : 0,
    "t121d" : 0,
    "t122d" : 0,
    "t123d" : 0,
    "t124d" : 0,
    "t125d" : 0,
    "t126d" : 0,
    "t127d" : 0,
    "t128d" : 0,
    "t129d" : 0,
    "t130d" : 0,
    "t131d" : 0,
    "t132d" : 0,
    "t133d" : 0,
    "t134d" : 0,
    "t135d" : 0,
    "t136d" : 0,
    "t137d" : 0,
    "t138d" : 0,
    "t139d" : 0,
    "t140d" : 0,
    "t141d" : 0,
    "t142d" : 0,
    "t143d" : 0,
    "t144d" : 0,
    "t145d" : 0,
    "t146d" : 0,
    "t147d" : 0,
    "t148d" : 0,
    "t149d" : 0,
    "t150d" : 0,
    "t151d" : 0,
    "t152d" : 0,
    "t153d" : 0,
    "t154d" : 0,
    "t155d" : 0,
    "t156d" : 0,
    "t157d" : 0,
    "t158d" : 0,
    "t159d" : 0,
    "t160d" : 0,
    "t1r" : 255,
    "t1g" : 255,
    "t1b" : 255,
    "t2r" : 255,
    "t2g" : 255,
    "t2b" : 255,
    "t3r" : 255,
    "t3g" : 255,
    "t3b" : 255,
    "t4r" : 255,
    "t4g" : 255,
    "t4b" : 255,
    "t5r" : 255,
    "t5g" : 255,
    "t5b" : 255,
    "t6r" : 255,
    "t6g" : 255,
    "t6b" : 255,
    "t7r" : 255,
    "t7g" : 255,
    "t7b" : 255,
    "t8r" : 255,
    "t8g" : 255,
    "t8b" : 255,
    "t9r" : 255,
    "t9g" : 255,
    "t9b" : 255,
    "t10r" : 255,
    "t10g" : 255,
    "t10b" : 255,
    "t11r" : 255,
    "t11g" : 255,
    "t11b" : 255,
    "t12r" : 255,
    "t12g" : 255,
    "t12b" : 255,
    "t13r" : 255,
    "t13g" : 255,
    "t13b" : 255,
}

if nd == 0:
    with open("tiledata.txt") as DATA:
        data = json.load(DATA)

#tiles
tile1 = pygame.Surface((50, 50))
tile2 = pygame.Surface((50, 50))
tile3 = pygame.Surface((50, 50))
tile4 = pygame.Surface((50, 50))
tile5 = pygame.Surface((50, 50))
tile6 = pygame.Surface((50, 50))
tile7 = pygame.Surface((50, 50))
tile8 = pygame.Surface((50, 50))
tile9 = pygame.Surface((50, 50))
tile10 = pygame.Surface((50, 50))
tile11 = pygame.Surface((50, 50))
tile12 = pygame.Surface((50, 50))
tile13 = pygame.Surface((50, 50))

# tile locatioons
t1x = 0
t1y = 0
t2x = 50
t2y = 0
t3x = 100
t3y = 0
t4x = 150
t4y = 0
t5x = 200
t5y = 0
t6x = 250
t6y = 0
t7x = 300
t7y = 0
t8x = 350
t8y = 0
t9x = 400
t9y = 0
t10x = 450
t10y = 0
t11x = 500
t11y = 0
t12x = 550
t12y = 0
t13x = 600
t13y = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if var == 0:
                with open("tiledata.txt", "w") as DATA:
                    json.dump(data, DATA)
            pygame.quit()
            sys.exit(0)
    
    #possibly important tile data | this is where you add tile data
    t1r = f"{data['t1r']}"
    t1g = f"{data['t1g']}"
    t1b = f"{data['t1b']}"
    t2r = f"{data['t2r']}"
    t2g = f"{data['t2g']}"
    t2b = f"{data['t2b']}"
    t3r = f"{data['t3r']}"
    t3g = f"{data['t3g']}"
    t3b = f"{data['t3b']}"
    t4r = f"{data['t4r']}"
    t4g = f"{data['t4g']}"
    t4b = f"{data['t4b']}"
    t5r = f"{data['t5r']}"
    t5g = f"{data['t5g']}"
    t5b = f"{data['t5b']}"
    t6r = f"{data['t6r']}"
    t6g = f"{data['t6g']}"
    t6b = f"{data['t6b']}"
    t7r = f"{data['t7r']}"
    t7g = f"{data['t7g']}"
    t7b = f"{data['t7b']}"
    t8r = f"{data['t8r']}"
    t8g = f"{data['t8g']}"
    t8b = f"{data['t8b']}"
    t9r = f"{data['t9r']}"
    t9g = f"{data['t9g']}"
    t9b = f"{data['t9b']}"
    t10r = f"{data['t10r']}"
    t10g = f"{data['t10g']}"
    t10b = f"{data['t10b']}"
    t11r = f"{data['t11r']}"
    t11g = f"{data['t11g']}"
    t11b = f"{data['t11b']}"
    t12r = f"{data['t12r']}"
    t12g = f"{data['t12g']}"
    t12b = f"{data['t12b']}"
    t13r = f"{data['t13r']}"
    t13g = f"{data['t13g']}"
    t13b = f"{data['t13b']}"
    
    screen.fill((0, 0, 0))

    tile1r = tile1.get_rect(topleft = (t1x, t1y))
    tile2r = tile1.get_rect(topleft = (t2x, t2y))
    tile3r = tile1.get_rect(topleft = (t3x, t3y))
    tile4r = tile1.get_rect(topleft = (t4x, t4y))
    tile5r = tile1.get_rect(topleft = (t5x, t5y))
    tile6r = tile1.get_rect(topleft = (t6x, t6y))
    tile7r = tile1.get_rect(topleft = (t7x, t7y))
    tile8r = tile1.get_rect(topleft = (t8x, t8y))
    tile9r = tile1.get_rect(topleft = (t9x, t9y))
    tile10r = tile1.get_rect(topleft = (t10x, t10y))
    tile11r = tile1.get_rect(topleft = (t11x, t11y))
    tile12r = tile1.get_rect(topleft = (t12x, t12y))
    tile13r = tile1.get_rect(topleft = (t13x, t13y))
    screen.blit(tile1, tile1r)
    screen.blit(tile2, tile2r)
    screen.blit(tile3, tile3r)
    screen.blit(tile4, tile4r)
    screen.blit(tile5, tile5r)
    screen.blit(tile6, tile6r)
    screen.blit(tile7, tile7r)
    screen.blit(tile8, tile8r)
    screen.blit(tile9, tile9r)
    screen.blit(tile10, tile10r)
    screen.blit(tile11, tile11r)
    screen.blit(tile12, tile12r)
    screen.blit(tile13, tile13r)
    tile1.fill((int(t1r), int(t1g), int(t1b)))
    tile2.fill((int(t2r), int(t2g), int(t2b)))
    tile3.fill((int(t3r), int(t3g), int(t3b)))
    tile4.fill((int(t4r), int(t4g), int(t4b)))
    tile5.fill((int(t5r), int(t5g), int(t5b)))
    tile6.fill((int(t6r), int(t6g), int(t6b)))
    tile7.fill((int(t7r), int(t7g), int(t7b)))
    tile8.fill((int(t8r), int(t8g), int(t8b)))
    tile9.fill((int(t9r), int(t9g), int(t9b)))
    tile10.fill((int(t10r), int(t10g), int(t10b)))
    tile11.fill((int(t11r), int(t11g), int(t11b)))
    tile12.fill((int(t12r), int(t12g), int(t12b)))
    tile13.fill((int(t13r), int(t13g), int(t13b)))
    
    #below is screen gui
    if var == 0:
        colour = font.render("red", False, (255, 255, 0))
        colour1 = font.render("ora", False, (255, 255, 0))
        colour2 = font.render("yel", False, (255, 255, 0))
        colour3 = font.render("gre", False, (255, 255, 0))
        colour4 = font.render("blu", False, (255, 255, 0))
        colour5 = font.render("pur", False, (255, 255, 0))
        colour6 = font.render("whi", False, (255, 255, 0))
        colour7 = font.render("bla", False, (255, 255, 0))
        color = colour.get_rect(topright = (640, 0))
        color1 = colour.get_rect(topright = (640, 40))
        color2 = colour.get_rect(topright = (640, 80))
        color3 = colour.get_rect(topright = (640, 120))
        color4 = colour.get_rect(topright = (640, 160))
        color5 = colour.get_rect(topright = (640, 200))
        color6 = colour.get_rect(topright = (640, 240))
        color7 = colour.get_rect(topright = (640, 280))
        screen.blit(colour, color)
        screen.blit(colour1, color1)
        screen.blit(colour2, color2)
        screen.blit(colour3, color3)
        screen.blit(colour4, color4)
        screen.blit(colour5, color5)
        screen.blit(colour6, color6)
        screen.blit(colour7, color7)
        
    #tile movment FIXES ISSUES WITH THE TIU NOT BEING CORRECT THIS INFORMATION IS NOT STORED
    if var == 0:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            t1y -= 1
            t2y -= 1
            t3y -= 1
            t4y -= 1 
            t5y -= 1 
            t6y -= 1   
            t7y -= 1  
            t8y -= 1   
            t9y -= 1 
            t10y -= 1 
            t11y -= 1  
            t12y -= 1 
            t13y -= 1 
        if keys[pygame.K_DOWN]:
            t1y += 1
            t2y += 1
            t3y += 1
            t4y += 1 
            t5y += 1 
            t6y += 1   
            t7y += 1  
            t8y += 1   
            t9y += 1 
            t10y += 1 
            t11y += 1  
            t12y += 1 
            t13y += 1 
        if keys[pygame.K_LEFT]:
            t1x -= 1
            t2x -= 1
            t3x -= 1
            t4x -= 1 
            t5x -= 1 
            t6x -= 1   
            t7x -= 1  
            t8x -= 1   
            t9x -= 1 
            t10x -= 1 
            t11x -= 1  
            t12x -= 1 
            t13x -= 1 
        if keys[pygame.K_RIGHT]:
            t1x += 1
            t2x += 1
            t3x += 1
            t4x += 1 
            t5x += 1 
            t6x += 1   
            t7x += 1  
            t8x += 1   
            t9x += 1 
            t10x += 1 
            t11x += 1  
            t12x += 1 
            t13x += 1 

    
    #this is where the tile editing magic occurs
    mouse_pos = pygame.mouse.get_pos()
    if tile1r.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (0, 0, 1):
            tiu = 1
    if tile2r.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (0, 0, 1):
            tiu = 2
    if tile3r.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (0, 0, 1):
            tiu = 3
    if tile4r.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (0, 0, 1):
            tiu = 4
    if tile5r.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (0, 0, 1):
            tiu = 5
    if tile6r.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (0, 0, 1):
            tiu = 6
    if tile7r.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (0, 0, 1):
            tiu = 7
    if tile8r.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (0, 0, 1):
            tiu = 8
    if tile9r.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (0, 0, 1):
            tiu = 9
    if tile10r.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (0, 0, 1):
            tiu = 10
    if tile11r.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (0, 0, 1):
            tiu = 11
    if tile12r.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (0, 0, 1):
            tiu = 12
    if tile13r.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (0, 0, 1):
            tiu = 13
    
    if tiu == 1:
        if color.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t1r"] = 255
                data["t1g"] = 0
                data["t1b"] = 0
                
    if tiu == 1:
        if color1.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t1r"] = 255
                data["t1g"] = 128
                data["t1b"] = 0
                
    if tiu == 1:
        if color2.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t1r"] = 255
                data["t1g"] = 255
                data["t1b"] = 0
                
    if tiu == 1:
        if color3.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t1r"] = 0
                data["t1g"] = 255
                data["t1b"] = 0
                
    if tiu == 1:
        if color4.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t1r"] = 0
                data["t1g"] = 0
                data["t1b"] = 255
                
    if tiu == 1:
        if color5.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t1r"] = 255
                data["t1g"] = 0
                data["t1b"] = 255
                
    if tiu == 1:
        if color6.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t1r"] = 255
                data["t1g"] = 255
                data["t1b"] = 255
                
    if tiu == 1:
        if color7.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t1r"] = 0
                data["t1g"] = 0
                data["t1b"] = 0
                
    if tiu == 2:
        if color.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t2r"] = 255
                data["t2g"] = 0
                data["t2b"] = 0
                
    if tiu == 2:
        if color1.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t2r"] = 255
                data["t2g"] = 128
                data["t2b"] = 0
                
    if tiu == 2:
        if color2.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t2r"] = 255
                data["t2g"] = 255
                data["t2b"] = 0
                
    if tiu == 2:
        if color3.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t2r"] = 0
                data["t2g"] = 255
                data["t2b"] = 0
                
    if tiu == 2:
        if color4.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t2r"] = 0
                data["t2g"] = 0
                data["t2b"] = 255
                
    if tiu == 2:
        if color5.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t2r"] = 255
                data["t2g"] = 0
                data["t2b"] = 255
                
    if tiu == 2:
        if color6.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t1r"] = 255
                data["t1g"] = 255
                data["t1b"] = 255
                
    if tiu == 2:
        if color7.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t2r"] = 0
                data["t2g"] = 0
                data["t2b"] = 0
                
    if tiu == 3:
        if color.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t3r"] = 255
                data["t3g"] = 0
                data["t3b"] = 0
                
    if tiu == 3:
        if color1.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t3r"] = 255
                data["t3g"] = 128
                data["t3b"] = 0
                
    if tiu == 3:
        if color2.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t3r"] = 255
                data["t3g"] = 255
                data["t3b"] = 0
                
    if tiu == 3:
        if color3.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t3r"] = 0
                data["t3g"] = 255
                data["t3b"] = 0
                
    if tiu == 3:
        if color4.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t3r"] = 0
                data["t3g"] = 0
                data["t3b"] = 255
                
    if tiu == 3:
        if color5.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t3r"] = 255
                data["t3g"] = 0
                data["t3b"] = 255
                
    if tiu == 3:
        if color6.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t3r"] = 255
                data["t3g"] = 255
                data["t3b"] = 255
                
    if tiu == 3:
        if color7.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t3r"] = 0
                data["t3g"] = 0
                data["t3b"] = 0
                
    if tiu == 4:
        if color.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t4r"] = 255
                data["t4g"] = 0
                data["t4b"] = 0
                
    if tiu == 4:
        if color1.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t4r"] = 255
                data["t4g"] = 128
                data["t4b"] = 0
                
    if tiu == 4:
        if color2.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t4r"] = 255
                data["t4g"] = 255
                data["t4b"] = 0
                
    if tiu == 4:
        if color3.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t4r"] = 0
                data["t4g"] = 255
                data["t4b"] = 0
                
    if tiu == 4:
        if color4.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t4r"] = 0
                data["t4g"] = 0
                data["t4b"] = 255
                
    if tiu == 4:
        if color5.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t4r"] = 255
                data["t4g"] = 0
                data["t4b"] = 255
                
    if tiu == 4:
        if color6.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t4r"] = 255
                data["t4g"] = 255
                data["t4b"] = 255
                
    if tiu == 4:
        if color7.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t4r"] = 0
                data["t4g"] = 0
                data["t4b"] = 0
    
    if tiu == 5:
        if color.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t5r"] = 255
                data["t5g"] = 0
                data["t5b"] = 0
                
    if tiu == 5:
        if color1.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t5r"] = 255
                data["t5g"] = 128
                data["t5b"] = 0
                
    if tiu == 5:
        if color2.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t5r"] = 255
                data["t5g"] = 255
                data["t5b"] = 0
                
    if tiu == 5:
        if color3.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t5r"] = 0
                data["t5g"] = 255
                data["t5b"] = 0
                
    if tiu == 5:
        if color4.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t5r"] = 0
                data["t5g"] = 0
                data["t5b"] = 255
                
    if tiu == 5:
        if color5.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t5r"] = 255
                data["t5g"] = 0
                data["t5b"] = 255
                
    if tiu == 5:
        if color6.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t5r"] = 255
                data["t5g"] = 255
                data["t5b"] = 255
                
    if tiu == 5:
        if color7.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t5r"] = 0
                data["t5g"] = 0
                data["t5b"] = 0
                
    if tiu == 6:
        if color.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t6r"] = 255
                data["t6g"] = 0
                data["t6b"] = 0
                
    if tiu == 6:
        if color1.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t6r"] = 255
                data["t6g"] = 128
                data["t6b"] = 0
                
    if tiu == 6:
        if color2.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t6r"] = 255
                data["t6g"] = 255
                data["t6b"] = 0
                
    if tiu == 6:
        if color3.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t6r"] = 0
                data["t6g"] = 255
                data["t6b"] = 0
                
    if tiu == 6:
        if color4.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t6r"] = 0
                data["t6g"] = 0
                data["t6b"] = 255
                
    if tiu == 6:
        if color5.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t6r"] = 255
                data["t6g"] = 0
                data["t6b"] = 255
                
    if tiu == 6:
        if color6.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t6r"] = 255
                data["t6g"] = 255
                data["t6b"] = 255
                
    if tiu == 6:
        if color7.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t6r"] = 0
                data["t6g"] = 0
                data["t6b"] = 0
                
    if tiu == 7:
        if color.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t7r"] = 255
                data["t7g"] = 0
                data["t7b"] = 0
                
    if tiu == 7:
        if color1.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t7r"] = 255
                data["t7g"] = 128
                data["t7b"] = 0
                
    if tiu == 7:
        if color2.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t7r"] = 255
                data["t7g"] = 255
                data["t7b"] = 0
                
    if tiu == 7:
        if color3.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t7r"] = 0
                data["t7g"] = 255
                data["t7b"] = 0
                
    if tiu == 7:
        if color4.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t7r"] = 0
                data["t7g"] = 0
                data["t7b"] = 255
                
    if tiu == 7:
        if color5.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t7r"] = 255
                data["t7g"] = 0
                data["t7b"] = 255
                
    if tiu == 7:
        if color6.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t7r"] = 255
                data["t7g"] = 255
                data["t7b"] = 255
                
    if tiu == 7:
        if color7.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t7r"] = 0
                data["t7g"] = 0
                data["t7b"] = 0
                
    if tiu == 8:
        if color.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t8r"] = 255
                data["t8g"] = 0
                data["t8b"] = 0
                
    if tiu == 8:
        if color1.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t8r"] = 255
                data["t8g"] = 128
                data["t8b"] = 0
                
    if tiu == 8:
        if color2.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t8r"] = 255
                data["t8g"] = 255
                data["t8b"] = 0
                
    if tiu == 8:
        if color3.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t8r"] = 0
                data["t8g"] = 255
                data["t8b"] = 0
                
    if tiu == 8:
        if color4.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t8r"] = 0
                data["t8g"] = 0
                data["t8b"] = 255
                
    if tiu == 8:
        if color5.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t8r"] = 255
                data["t8g"] = 0
                data["t8b"] = 255
                
    if tiu == 8:
        if color6.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t8r"] = 255
                data["t8g"] = 255
                data["t8b"] = 255
                
    if tiu == 8:
        if color7.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t8r"] = 0
                data["t8g"] = 0
                data["t8b"] = 0
                
    if tiu == 9:
        if color.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t9r"] = 255
                data["t9g"] = 0
                data["t9b"] = 0
                
    if tiu == 9:
        if color1.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t9r"] = 255
                data["t9g"] = 128
                data["t9b"] = 0
                
    if tiu == 9:
        if color2.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t9r"] = 255
                data["t9g"] = 255
                data["t9b"] = 0
                
    if tiu == 9:
        if color3.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t9r"] = 0
                data["t9g"] = 255
                data["t9b"] = 0
                
    if tiu == 9:
        if color4.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t9r"] = 0
                data["t9g"] = 0
                data["t9b"] = 255
                
    if tiu == 9:
        if color5.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t9r"] = 255
                data["t9g"] = 0
                data["t9b"] = 255
                
    if tiu == 9:
        if color6.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t9r"] = 255
                data["t9g"] = 255
                data["t9b"] = 255
                
    if tiu == 9:
        if color7.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t9r"] = 0
                data["t9g"] = 0
                data["t9b"] = 0
                
    if tiu == 10:
        if color.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t10r"] = 255
                data["t10g"] = 0
                data["t10b"] = 0
                
    if tiu == 10:
        if color1.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t10r"] = 255
                data["t10g"] = 128
                data["t10b"] = 0
                
    if tiu == 10:
        if color2.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t10r"] = 255
                data["t10g"] = 255
                data["t10b"] = 0
                
    if tiu == 10:
        if color3.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t10r"] = 0
                data["t10g"] = 255
                data["t10b"] = 0
                
    if tiu == 10:
        if color4.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t10r"] = 0
                data["t10g"] = 0
                data["t10b"] = 255
                
    if tiu == 10:
        if color5.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t10r"] = 255
                data["t10g"] = 0
                data["t10b"] = 255
                
    if tiu == 10:
        if color6.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t10r"] = 255
                data["t10g"] = 255
                data["t10b"] = 255
                
    if tiu == 10:
        if color7.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t10r"] = 0
                data["t10g"] = 0
                data["t10b"] = 0
                
    if tiu == 11:
        if color.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t11r"] = 255
                data["t11g"] = 0
                data["t11b"] = 0
                
    if tiu == 11:
        if color1.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t11r"] = 255
                data["t11g"] = 128
                data["t11b"] = 0
                
    if tiu == 11:
        if color2.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t11r"] = 255
                data["t11g"] = 255
                data["t11b"] = 0
                
    if tiu == 11:
        if color3.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t11r"] = 0
                data["t11g"] = 255
                data["t11b"] = 0
                
    if tiu == 11:
        if color4.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t11r"] = 0
                data["t11g"] = 0
                data["t11b"] = 255
                
    if tiu == 11:
        if color5.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t11r"] = 255
                data["t11g"] = 0
                data["t11b"] = 255
                
    if tiu == 11:
        if color6.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t11r"] = 255
                data["t11g"] = 255
                data["t11b"] = 255
                
    if tiu == 11:
        if color7.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t11r"] = 0
                data["t11g"] = 0
                data["t11b"] = 0
    
    if tiu == 12:
        if color.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t12r"] = 255
                data["t12g"] = 0
                data["t12b"] = 0
                
    if tiu == 12:
        if color1.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t12r"] = 255
                data["t12g"] = 128
                data["t12b"] = 0
                
    if tiu == 12:
        if color2.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t12r"] = 255
                data["t12g"] = 255
                data["t12b"] = 0
                
    if tiu == 12:
        if color3.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t12r"] = 0
                data["t12g"] = 255
                data["t12b"] = 0
                
    if tiu == 12:
        if color4.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t12r"] = 0
                data["t12g"] = 0
                data["t12b"] = 255
                
    if tiu == 12:
        if color5.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t12r"] = 255
                data["t12g"] = 0
                data["t12b"] = 255
                
    if tiu == 12:
        if color6.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t12r"] = 255
                data["t12g"] = 255
                data["t12b"] = 255
                
    if tiu == 12:
        if color7.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t12r"] = 0
                data["t12g"] = 0
                data["t12b"] = 0
                
    if tiu == 13:
        if color.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t13r"] = 255
                data["t13g"] = 0
                data["t13b"] = 0
                
    if tiu == 13:
        if color1.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t13r"] = 255
                data["t13g"] = 128
                data["t13b"] = 0
                
    if tiu == 13:
        if color2.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t13r"] = 255
                data["t13g"] = 255
                data["t13b"] = 0
                
    if tiu == 13:
        if color3.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t13r"] = 0
                data["t13g"] = 255
                data["t13b"] = 0
                
    if tiu == 13:
        if color4.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t13r"] = 0
                data["t13g"] = 0
                data["t13b"] = 255
                
    if tiu == 13:
        if color5.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t13r"] = 255
                data["t13g"] = 0
                data["t13b"] = 255
                
    if tiu == 13:
        if color6.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t13r"] = 255
                data["t13g"] = 255
                data["t13b"] = 255
                
    if tiu == 13:
        if color7.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["t13r"] = 0
                data["t13g"] = 0
                data["t13b"] = 0

    clock = pygame.time.Clock()
    pygame.display.flip()
    clock.tick(30)