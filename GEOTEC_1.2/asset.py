"""asset.py is where the assets of the GEOTEC game engine are held. Examples are, the location of tiles, tile movement,
 and generally all the boring things that would clutter up the main files of my previous game engimes."""

import pygame
import json

#json stuff
opn = open(str("data.txt"))
loc = json.load(opn)
fil = open(str("colors.txt"))
clr = json.load(fil)

#font stuff
pygame.font.init()
font = pygame.font.Font("Grand9k Pixel.ttf", 30)

#pos tracker
global posx
global posy
posx = 0
posy = 0

#gui
dics = pygame.image.load("savepos.png")
nums = pygame.image.load("s#.png")
cmds = pygame.image.load("cmd.png")
pain = pygame.image.load("tastetherainbow.png")

#surfaces
centre = pygame.Surface((50, 50)) #this is permenantly broken reminder to try and fix
s1 = pygame.Surface((50, 50))
s2 = pygame.Surface((50, 50))
s3 = pygame.Surface((50, 50))
s4 = pygame.Surface((50, 50))
s5 = pygame.Surface((50, 50))
s6 = pygame.Surface((50, 50))
s7 = pygame.Surface((50, 50))
s8 = pygame.Surface((50, 50))
s9 = pygame.Surface((50, 50))
s10 = pygame.Surface((50, 50))
s11 = pygame.Surface((50, 50))
s12 = pygame.Surface((50, 50))
s13 = pygame.Surface((50, 50))
s14 = pygame.Surface((50, 50))
s15 = pygame.Surface((50, 50))
s16 = pygame.Surface((50, 50))
s17 = pygame.Surface((50, 50))
s18 = pygame.Surface((50, 50))
s19 = pygame.Surface((50, 50))
s20 = pygame.Surface((50, 50))
s21 = pygame.Surface((50, 50))
s22 = pygame.Surface((50, 50))
s23 = pygame.Surface((50, 50))

#rectangles
center = centre.get_rect(bottomright = (320, 240))
s1r = s1.get_rect(center = (320, 240))
s2r = s1.get_rect(center = (loc[0], loc[1]))
s3r = s1.get_rect(center = (loc[2], loc[3]))
s4r = s1.get_rect(center = (loc[4], loc[5]))
s5r = s1.get_rect(center = (loc[6], loc[7]))
s6r = s1.get_rect(center = (loc[8], loc[9]))
s7r = s1.get_rect(center = (loc[10], loc[11]))
s8r = s1.get_rect(center = (loc[12], loc[13]))
s9r = s1.get_rect(center = (loc[14], loc[15]))
s10r = s1.get_rect(center = (loc[16], loc[17]))
s11r = s1.get_rect(center = (loc[18], loc[19]))
s12r = s1.get_rect(center = (loc[20], loc[21]))
s13r = s1.get_rect(center = (loc[22], loc[23]))
s14r = s1.get_rect(center = (loc[24], loc[25]))
s15r = s1.get_rect(center = (loc[26], loc[27]))
s16r = s1.get_rect(center = (loc[28], loc[29]))
s17r = s1.get_rect(center = (loc[30], loc[31]))
s18r = s1.get_rect(center = (loc[32], loc[33]))
s19r = s1.get_rect(center = (loc[34], loc[35]))
s20r = s1.get_rect(center = (loc[36], loc[37]))
s21r = s1.get_rect(center = (loc[38], loc[39]))
s22r = s1.get_rect(center = (loc[40], loc[41]))
s23r = s1.get_rect(center = (loc[42], loc[43]))

#colors
centre.fill((255, 255, 255))
s2.fill(clr[0])
s3.fill(clr[1])
s4.fill(clr[2])
s5.fill(clr[3])
s6.fill(clr[4])
s7.fill(clr[5])
s8.fill(clr[6])
s9.fill(clr[7])
s10.fill(clr[8])
s11.fill(clr[9])
s12.fill(clr[10])
s13.fill(clr[11])
s14.fill(clr[12])
s15.fill(clr[13])
s16.fill(clr[14])
s17.fill(clr[15])
s18.fill(clr[16])
s19.fill(clr[17])
s20.fill(clr[18])
s21.fill(clr[19])
s22.fill(clr[20])
s23.fill(clr[21])

#font stuff
s2t = font.render("s2", False, (255, 255, 0))
s3t = font.render("s3", False, (255, 255, 0))
s4t = font.render("s4", False, (255, 255, 0))
s5t = font.render("s5", False, (255, 255, 0))
s6t = font.render("s6", False, (255, 255, 0))
s7t = font.render("s7", False, (255, 255, 0))
s8t = font.render("s8", False, (255, 255, 0))
s9t = font.render("s9", False, (255, 255, 0))
s10t = font.render("s10", False, (255, 255, 0))
s11t = font.render("s11", False, (255, 255, 0))
s12t = font.render("s12", False, (255, 255, 0))
s13t = font.render("s13", False, (255, 255, 0))
s14t = font.render("s14", False, (255, 255, 0))
s15t = font.render("s15", False, (255, 255, 0))
s16t = font.render("s16", False, (255, 255, 0))
s17t = font.render("s17", False, (255, 255, 0))
s18t = font.render("s18", False, (255, 255, 0))
s19t = font.render("s19", False, (255, 255, 0))
s20t = font.render("s20", False, (255, 255, 0))
s21t = font.render("s21", False, (255, 255, 0))
s22t = font.render("s22", False, (255, 255, 0))
s23t = font.render("s23", False, (255, 255, 0))

#tracker
tracker = 0
def trackitron():
    mouse_pos = pygame.mouse.get_pos()
    if tracker == 2:
        (s2r.x, s2r.y) = mouse_pos
    if tracker == 3:
        (s3r.x, s3r.y) = mouse_pos
    if tracker == 4:
        (s4r.x, s4r.y) = mouse_pos
    if tracker == 5:
        (s5r.x, s5r.y) = mouse_pos
    if tracker == 6:
        (s6r.x, s6r.y) = mouse_pos
    if tracker == 7:
        (s7r.x, s7r.y) = mouse_pos
    if tracker == 8:
        (s8r.x, s8r.y) = mouse_pos
    if tracker == 9:
        (s9r.x, s9r.y) = mouse_pos
    if tracker == 10:
        (s10r.x, s10r.y) = mouse_pos
    if tracker == 11:
        (s11r.x, s11r.y) = mouse_pos
    if tracker == 12:
        (s12r.x, s12r.y) = mouse_pos
    if tracker == 13:
        (s13r.x, s13r.y) = mouse_pos
    if tracker == 14:
        (s14r.x, s14r.y) = mouse_pos
    if tracker == 15:
        (s15r.x, s15r.y) = mouse_pos
    if tracker == 16:
        (s16r.x, s16r.y) = mouse_pos
    if tracker == 17:
        (s17r.x, s17r.y) = mouse_pos
    if tracker == 18:
        (s18r.x, s18r.y) = mouse_pos
    if tracker == 19:
        (s19r.x, s19r.y) = mouse_pos
    if tracker == 20:
        (s20r.x, s20r.y) = mouse_pos
    if tracker == 21:
        (s21r.x, s21r.y) = mouse_pos
    if tracker == 22:
        (s22r.x, s22r.y) = mouse_pos
    if tracker == 23:
        (s23r.x, s23r.y) = mouse_pos

#keyboard control
def keys():
    global posx
    global posy
    keyss = pygame.key.get_pressed()
    if keyss[pygame.K_w]:
        center.y += 10
        s2r.y += 10
        s3r.y += 10
        s4r.y += 10
        s5r.y += 10
        s6r.y += 10
        s7r.y += 10
        s8r.y += 10
        s9r.y += 10
        s10r.y += 10
        s11r.y += 10
        s12r.y += 10
        s13r.y += 10
        s14r.y += 10
        s15r.y += 10
        s16r.y += 10
        s17r.y += 10
        s18r.y += 10
        s19r.y += 10
        s20r.y += 10
        s21r.y += 10
        s22r.y += 10
        s23r.y += 10
        posy += 10
    if keyss[pygame.K_s]:
        center.y -= 10
        s2r.y -= 10
        s3r.y -= 10
        s4r.y -= 10
        s5r.y -= 10
        s6r.y -= 10
        s7r.y -= 10
        s8r.y -= 10
        s9r.y -= 10
        s10r.y -= 10
        s11r.y -= 10
        s12r.y -= 10
        s13r.y -= 10
        s14r.y -= 10
        s15r.y -= 10
        s16r.y -= 10
        s17r.y -= 10
        s18r.y -= 10
        s19r.y -= 10
        s20r.y -= 10
        s21r.y -= 10
        s22r.y -= 10
        s23r.y -= 10
        posy -= 10
    if keyss[pygame.K_a]:
        center.x += 10
        s2r.x += 10
        s3r.x += 10
        s4r.x += 10
        s5r.x += 10
        s6r.x += 10
        s7r.x += 10
        s8r.x += 10
        s9r.x += 10
        s10r.x += 10
        s11r.x += 10
        s12r.x += 10
        s13r.x += 10
        s14r.x += 10
        s15r.x += 10
        s16r.x += 10
        s17r.x += 10
        s18r.x += 10
        s19r.x += 10
        s20r.x += 10
        s21r.x += 10
        s22r.x += 10
        s23r.x += 10
        posx += 10
    if keyss[pygame.K_d]:
        center.x -= 10
        s2r.x -= 10
        s3r.x -= 10
        s4r.x -= 10
        s5r.x -= 10
        s6r.x -= 10
        s7r.x -= 10
        s8r.x -= 10
        s9r.x -= 10
        s10r.x -= 10
        s11r.x -= 10
        s12r.x -= 10
        s13r.x -= 10
        s14r.x -= 10
        s15r.x -= 10
        s16r.x -= 10
        s17r.x -= 10
        s18r.x -= 10
        s19r.x -= 10
        s20r.x -= 10
        s21r.x -= 10
        s22r.x -= 10
        s23r.x -= 10
        posx -= 10
    #print(posx, posy)