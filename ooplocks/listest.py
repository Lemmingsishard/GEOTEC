import pygame
import json
import random


pygame.init()

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
pygame.display.set_caption("listest")

font = pygame.font.Font("Grand9K Pixel.ttf", 30)

ff = open(str("test.txt"))
jf = json.load(ff)

def gui(words: str, x: int, y: int, bob = None):
    mouse_pos = pygame.mouse.get_pos()
    guy = font.render(words, False, (255, 255, 0))
    guing = guy.get_rect(topleft = (x, y))
    screen.blit(guy, guing)
    if guing.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if bob != None:
                bob()

rng = font.render("generate number", False, (255, 255, 0))
rectng = rng.get_rect(topright = (320, 430))
rn = 0
list = []
otehrlist = []

def save():
    with open("test.txt", "w") as fufa:
        json.dump((list, otehrlist), fufa)
        fufa.close()

def load():
    list.clear()
    otehrlist.clear()
    list.extend(jf[0])
    otehrlist.extend(jf[1])

def varify():
    global rn
    rn = list
    print(otehrlist, list)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if rectng.collidepoint((mouse_pos)):
                rn = random.randrange(0, 2137)
                orn = random.randrange(0, 420)
                otehrlist.append(orn)
                list.append(rn)

    rnd = font.render(str(rn), False, (255, 255, 0))
    rectnd = rnd.get_rect(center = (320, 240))

    pygame.draw.rect(screen, (0, 0, 0), (0, 0, 640, 480))

    screen.blit(rng, rectng)
    screen.blit(rnd, rectnd)
    gui("load", 20, 0, load)
    gui("save", 540, 0, save)
    gui("varify", 330, 430, varify)

    pygame.display.flip()
    clock.tick(30)