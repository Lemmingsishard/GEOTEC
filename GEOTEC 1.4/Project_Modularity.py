#the killers of our auto industry
import pygame
import random
import json
pygame.init()

#important game running details
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
pygame.display.set_caption("GEOTEC_1.4")
ico = pygame.image.load("assets/GEOTECLOGO.ico")
pygame.display.set_icon(ico)

#json decription
rawfig = open(str("config.json"))
figgy = json.load(rawfig)

gdf = open(str(f"{figgy[0]}/modularity.json"))
gdl = json.load(gdf)

pth = open(str(f"{figgy[0]}/portals.json"))
gaj = json.load(pth)

txt = open(str(f"{figgy[0]}/text.json"))
use = json.load(txt)

#some random crap I have to put at the beginning since computers are fussy
delmode = 0

tiledata = {
    "savepos": {
        "x" : [10, 100, 440, 18],
        "y" : [400, 200, 30, 300],
        "w" : 50,
        "h" : 50,
        "tags": [0, 1, 2, 3],
        "color": None,
        "texture": "savepos.png",
        "collision": True,
    },

    "bigcheese": {
        "x": [100],
        "y": [100],
        "w": 100,
        "h": 100,
        "tags": [0],
        "color": [255, 255, 0],
        "texture": None,
        "collision": True,
    },

    "grass": {
        "x": [600, 550, 420, 287],
        "y": [320, 240, 197, 468],
        "w": 50,
        "h": 50,
        "tags": [0, 1, 2, 3],
        "color": None,
        "texture": "plant texture.png",
        "collision": False,
    },
} 

portals = {
    "basic": {
        "x1": [100],
        "y1": [0],
        "x2": [100],
        "y2": [400],
        "w": 50,
        "h": 50,
        "tags": [0],
        "color": [0, 0, 255],
        "texture": None,
    },
}

#random yet incredibly important variables
tiledata = gdl
cooldown = 0
wordata = use

#a moment of slience to all programmers that have had to make portals in 3d ...
portals = gaj

#gravity controls - Gravity is very buggy
velocity = 1
Enable_Gravity = figgy[1]
fall_countdown = 0
allow_jump = False

class text:
    def __init__(self, words, x, y, tags, isgui, bkground_color = None, clickable = None):
        #definitions
        global delmode
        self.tags = tags
        self.isgui = isgui
        self.localtag = wordata[i]["tags"]
        #background color things
        if bkground_color != None:
            self.guy = font.render(words, False, (255, 255, 0), bkground_color)
        else:
            self.guy = font.render(words, False, (255, 255, 0))
        #drawing
        self.guing = self.guy.get_rect(topleft = (x, y))
        screen.blit(self.guy, self.guing)
        #clicking - this is a bit broken at the momenet as I have no idea how to incorporate scripts
        #if clickable == True:
        #    self.func = getattr(scripts, i)
        #    mouse_pos = pygame.mouse.get_pos()
        #    if self.guing.collidepoint((mouse_pos)):
        #        if pygame.mouse.get_pressed() == (1, 0, 0):
        #            self.func()
        #deletion
        if delmode == 1:
            if self.tags[yoll] == self.localtag[yoll]:
                mouse_pos = pygame.mouse.get_pos()
                if self.guing.collidepoint((mouse_pos)):
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        wordata[i]["tags"].pop(yoll)
                        wordata[i]["x"].pop(yoll)
                        wordata[i]["y"].pop(yoll)
                        delmode = 0

class portal:
    def __init__(self, x1, y1, x2, y2, w, h, tags, color = None, texture = None):
        global portals
        global delmode
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.w = w
        self.h = h
        self.tags = tags
        self.localtag = portals[i]["tags"]
        self.b = pygame.Rect(self.x1, self.y1, self.w, self.h)
        self.o = pygame.Rect(self.x2, self.y2, self.w, self.h)
        if color != None:
            self.color = color
            pygame.draw.rect(screen, self.color, self.b)
            pygame.draw.rect(screen, self.color, self.o)
        if texture != None:
            self.texture = texture
            self.image = pygame.image.load(self.texture)
            screen.blit(self.image, self.b)
            screen.blit(self.image, self.o)
        if delmode == 1:
            if self.tags[yoll] == self.localtag[yoll]:
                mouse_pos = pygame.mouse.get_pos()
                if self.b.collidepoint((mouse_pos)) or self.o.collidepoint((mouse_pos)):
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        portals[i]["tags"].pop(yoll)
                        portals[i]["x1"].pop(yoll)
                        portals[i]["y1"].pop(yoll)
                        portals[i]["x2"].pop(yoll)
                        portals[i]["y2"].pop(yoll)
                        delmode = 0
        portal.teleport(self)
    def teleport(self):
        global cooldown
        if cooldown == 0:
            if self.b.colliderect(bob):
                cooldown = 20
                if direction == "w":
                    bob.y = self.y2 - 50
                    bob.x = self.x2
                elif direction == "s":
                    bob.y = self.y2 + 50
                    bob.x = self.x2
                elif direction == "a":
                    bob.x = self.x2 - 50
                    bob.y = self.y2
                elif direction == "d":
                    bob.x = self.x2 + 50
                    bob.y = self.y2
            elif self.o.colliderect(bob):
                #bob.x = self.x1
                #bob.y = self.y1
                cooldown = 20
                if direction == "w":
                    bob.y = self.y1 - 50
                    bob.x = self.x1
                elif direction == "s":
                    bob.y = self.y1 + 50
                    bob.x = self.x1
                elif direction == "a":
                    bob.x = self.x1 - 50
                    bob.y = self.y1
                elif direction == "d":
                    bob.x = self.x1 + 50
                    bob.y = self.y1

class tileclass:
    def __init__(self, x, y, w, h, tags, color = None, texture = None, collision = None):
        global tiledata
        global delmode
        global direction
        global velocity
        global allow_jump
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.texture = texture
        self.collision = collision
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        if Enable_Gravity == True:
            self.rectdos = pygame.Rect(self.x, self.y, self.w, 1)
        self.tag = tags
        self.localtag = tiledata[i]["tags"]
        if color != None:
            self.color = color
            pygame.draw.rect(screen, self.color, self.rect)
        if texture != None:
            self.image = pygame.image.load(self.texture)
            self.irect = self.image.get_rect(center = (self.x + 25, self.y + 25))
            screen.blit(self.image, self.irect)
        #pygame.draw.rect(screen, (255, 255, 255), self.rectdos)
        if collision == True:
            if bob.colliderect(self.rect):
                if direction == "w":
                    if Enable_Gravity == True:
                        if bobbom.colliderect(self.rect):
                            bob.y -= 10
                        elif tobbom.colliderect(self.rect):
                            bob.y += 20
                    else:
                        bob.y += 10
                elif direction == "a":
                    if Enable_Gravity == True:
                        if bob.colliderect(self.rectdos):
                            pass
                        else:
                            bob.x += 10
                            velocity = 10
                    else:
                        bob.x += 10
                elif direction == "s":
                    bob.y -= 10
                elif direction == "d":
                    if Enable_Gravity == True:
                        if bob.colliderect(self.rectdos):
                            pass
                        else:
                            bob.x -= 10
                            velocity = 10
                    else:
                        bob.x -= 10
            if Enable_Gravity == True:
                if bobbom.colliderect(self.rectdos):
                    bob.y -= 10
                    velocity = 0
                    allow_jump = True
                else:
                    if fall_countdown == 0:
                        if velocity < 10: 
                            velocity += 1
        if delmode == 1:
            if self.tag[yoll] == self.localtag[yoll]:
                mouse_pos = pygame.mouse.get_pos()
                if self.rect.collidepoint((mouse_pos)):
                    if pygame.mouse.get_pressed() == (1, 0, 0):
                        tiledata[i]["tags"].pop(yoll)
                        tiledata[i]["x"].pop(yoll)
                        tiledata[i]["y"].pop(yoll)
                        delmode = 0

class typelist:
    def __init__(self, list):
        self.typelist = []
        self.typelistpos = 0
        for i in list:
            self.typelist.append(i)

#lil lists bein' defined. Look at how much they've grown
basictlist = typelist(tiledata)
portalist = typelist(portals)
wordlist = typelist(wordata)

#player
bobert = pygame.Surface((50, 50))
bob = pygame.Surface.get_rect(bobert, topleft = (1, 0))
bobbom = pygame.Rect(bob.x, bob.y - 25, 50, 25)
tobbom = pygame.Rect(bob.x, bob.y, 50, 25)
bobert.fill((244, 255, 220))

direction = "" #important collision thing
background = pygame.Surface((1000, 1000))#read the name of the variable

#more integral but random variable definitions
fattius = pygame.Rect(0, 0, 640, 480)#more background things
tagil = 0
bop = 0
title = 1
lines = 0
lobdo = pygame.image.load("assets/GeoTec_logo_large.png") #TEH EPIK LOOGO
holding = 0
frass = []
nombre = 0
yasss = []
sasss = []
tiletype = 0
nombredos = 0
part = 2
thingamabobx = 0
thingamaboby = 0
dosx = 0
dosy = 0
nombretres = 0
teXt = []
teYt = []
tetagst = []

#edit mode variables
Edit_Mode = figgy[2]

#nu move variables
Nu_Move_enabled = False

font = pygame.font.Font("assets/Grand9K Pixel.ttf", 30) #yes

#text based gui builder
def gui(words: str, x: int, y: int, bob = None, color = None):
    mouse_pos = pygame.mouse.get_pos()
    if color != None:
        guy = font.render(words, False, (255, 255, 0), color)
    else:
        guy = font.render(words, False, (255, 255, 0))
    guing = guy.get_rect(topleft = (x, y))
    screen.blit(guy, guing)
    if guing.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if bob != None:
                bob()

#gui
if Edit_Mode == True:
    button = pygame.draw.circle(screen, (255, 128, 0), (600, 440), 30)
    futton = pygame.draw.circle(screen, (128, 255, 0), (530, 440), 30)
    lutton = pygame.draw.circle(screen, (0, 128, 255), (460, 440), 30)
    cutton = pygame.draw.circle(screen, (255, 128, 128), (390, 440), 30)
    mutton = pygame.draw.circle(screen, (255, 0, 0), (40, 440), 30)
    putton = pygame.draw.circle(screen, (128, 0, 255), (320, 440), 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        #single used buttons: switcher and lines respectively
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if event.button == 1:
                if Edit_Mode == True:
                    #changes the tile listed
                    if button.collidepoint((mouse_pos)):
                        if tiletype == 0:
                            if basictlist.typelistpos == len(basictlist.typelist) - 1:
                                basictlist.typelistpos = 0
                            elif basictlist.typelistpos > len(basictlist.typelist) - 1:
                                basictlist.typelistpos = 0
                            else:
                                basictlist.typelistpos += 1
                        if tiletype == 1:
                            if portalist.typelistpos == len(portalist.typelist) - 1:
                                portalist.typelistpos = 0
                            elif portalist.typelistpos > len(portalist.typelist) - 1:
                                portalist.typelistpos = 0
                            else:
                                portalist.typelistpos += 1
                        if tiletype == 2:
                            if wordlist.typelistpos == len(wordlist.typelist) - 1:
                                wordlist.typelistpos = 0
                            elif wordlist.typelistpos > len(wordlist.typelist) - 1:
                                wordlist.typelistpos = 0
                            else:
                                wordlist.typelistpos += 1
                    #turns on or off the grid
                    if lutton.collidepoint((mouse_pos)):
                        if lines == 0:
                            lines = 1
                        elif lines == 1:
                            lines = 0
                    #thing for other thing
                    if putton.collidepoint((mouse_pos)):
                        if tiletype == 0:
                            tiletype = 1
                        elif tiletype == 1:
                            tiletype = 2
                        elif tiletype == 2:
                            tiletype = 0
                    #Idk anymore
                    if futton.collidepoint((mouse_pos)):
                        if tiletype == 1:
                            if part == 2:
                                part = 1
                            elif part == 1: 
                                part = 2
            if event.button == 3:
                if Edit_Mode == True:
                    if button.collidepoint((mouse_pos)):
                        #changes the listed tile but backwards
                        if tiletype == 0:
                            if basictlist.typelistpos == len(basictlist.typelist) - 1:
                                basictlist.typelistpos = 0
                            elif basictlist.typelistpos > len(basictlist.typelist) - 1:
                                basictlist.typelistpos = 0
                            else:
                                basictlist.typelistpos -= 1
                        if tiletype == 1:
                            if portalist.typelistpos == len(portalist.typelist) - 1:
                                portalist.typelistpos = 0
                            elif portalist.typelistpos > len(portalist.typelist) - 1:
                                portalist.typelistpos = 0
                            else:
                                portalist.typelistpos -= 1
                        if tiletype == 2:
                            if wordlist.typelistpos == len(wordlist.typelist) - 1:
                                wordlist.typelistpos = 0
                            elif wordlist.typelistpos > len(wordlist.typelist) - 1:
                                wordlist.typelistpos = 0
                            else:
                                wordlist.typelistpos -= 1
                    if putton.collidepoint((mouse_pos)):
                        if tiletype == 0:
                            tiletype = 2
                        elif tiletype == 1:
                            tiletype = 0
                        elif tiletype == 2:
                            tiletype = 1

    #things that both the title screen and gameplay need
    screen.blit(background, (0, 0))
    mouse_pos = pygame.mouse.get_pos()
    keys = pygame.key.get_pressed()
    #EAsTer EgG
    if keys[pygame.K_LCTRL] and keys[pygame.K_g] and keys[pygame.K_w]:
        title = 2

    #C above
    if title == 2:
        if keys[pygame.K_ESCAPE]:
            title = 1
        gui("Made by UPGSOFTWARE the only division of WIZARD STUDIOS,", 0, 0)
        gui("of WIZARD STUDIOS, and running on", 0, 45)
        gui("Geotec 1.4 and built on pygame,", 0, 90)
        gui("press escape to return to title.", 0, 135)

    #title screen
    if title == 1:
        screen.blit(lobdo, (25, 10))
        gui("Exit (don't plox)", 190, 320, exit)
        def t0():
            global title
            title = 0
        gui("Play", 285, 215, t0)
        gui("Fullscreen", 238, 269, pygame.display.toggle_fullscreen)

    #gameplay
    if title == 0:
        #controls
        if keys[pygame.K_w]:
            if Enable_Gravity == False:
                bob.y -= 10
            direction = "w"
            if Enable_Gravity == True:
                if allow_jump == True:
                    velocity = -15
                    fall_countdown = 15
                    allow_jump = False
        elif keys[pygame.K_a]:
            bob.x -= 10
            direction = "a"
        elif keys[pygame.K_s]:
            if Enable_Gravity == False:
                bob.y += 10
                direction = "s"
        elif keys[pygame.K_d]:
            bob.x += 10
            direction = "d"
        elif keys [pygame.K_ESCAPE]:
            title = 1

        #a slightly simpler (and more efficient) map drawing system
        yoll = 0
        for i in tiledata:
            yoll = 0  
            for x in tiledata[i]["x"]:
                yick = tiledata[i]["y"]  
                call = tileclass(x, yick[yoll], tiledata[i]["w"], tiledata[i]["h"], tiledata[i]["tags"],  tiledata[i]["color"], tiledata[i]["texture"], tiledata[i]["collision"])
                yoll += 1

        for i in portals:
            yoll = 0
            for x in portals[i]["x1"]:
                yick = portals[i]["y1"]
                xick = portals[i]["x2"]
                yusef = portals[i]["y2"]
                pall = portal(x, yick[yoll], xick[yoll], yusef[yoll], portals[i]["w"], portals[i]["h"], portals[i]["tags"], portals[i]["color"], portals[i]["texture"])
                yoll += 1
        
        for i in wordata:
            yoll = 0  
            if wordata[i]["isgui"] == False:
                for x in wordata[i]["x"]:
                    yick = wordata[i]["y"]  
                    wall = text(wordata[i]["words"], x, yick[yoll], wordata[i]["tags"], wordata[i]["isgui"], wordata[i]["bkground_color"])
                    yoll += 1

        #the only thing that makes map editing not impossible
        if lines == 1:
            scanline = 50
            scanblock = 50
            for x in range(13):
                for y in range(10):
                    ross = pygame.Rect(scanblock * x + 1, scanblock * y + 1, 50, 50)
                    if ross.collidepoint((mouse_pos)):
                        if pygame.mouse.get_pressed() == (0, 0, 1):
                            if holding == 1:
                                frass.append(ross.x)
                                sasss.append(ross.y)
                                yasss.append(nombre)
                                holding = 0
                            if holding == 2:
                                if part == 1:
                                    thingamabobx = ross.x
                                    thingamaboby = ross.y
                                    tagamabob = nombredos
                                    holding = 0
                                if part == 2:
                                    dosx = ross.x
                                    dosy = ross.y
                                    x1ss.append(thingamabobx)
                                    d1ss.append(thingamaboby)
                                    x2ss.append(dosx)
                                    d2ss.append(dosy)
                                    tass.append(tagamabob)
                                    holding = 0    
                            if holding == 3:
                                teXt.append(ross.x)
                                teYt.append(ross.y)
                                tetagst.append(nombre)
                                holding = 0
            for i in range(13):
                pygame.draw.line(screen, (255, 255, 255), (scanline * i + 1, 0), (scanline * i + 1, 480))
                pygame.draw.line(screen, (255, 255, 255), (0, scanline * i + 1), (640, scanline * i + 1))

        screen.blit(bobert, bob) #player
        bobbom = pygame.Rect(bob.x, bob.y + 25, 50, 25)
        tobbom = pygame.Rect(bob.x, bob.y, 50, 25)

        for i in wordata:
            yoll = 0  
            if wordata[i]["isgui"] == True:
                for x in wordata[i]["x"]:
                    yick = wordata[i]["y"]  
                    wall = text(wordata[i]["words"], x, yick[yoll], wordata[i]["tags"], wordata[i]["isgui"], wordata[i]["bkground_color"], wordata[i]["clickable"])
                    yoll += 1

        #important gravity engine bit
        if Enable_Gravity == True:
            bob.y += velocity
            if fall_countdown != 0:
                fall_countdown -= 1

        #temopmoryary movement system, turned out to be the permenant movement system :\
        for i in tiledata:
            if Nu_Move_enabled == False:
                xelcior = tiledata[i]["x"]
                yavaltal = tiledata[i]["y"]
                if bob.x + 50 > 590:
                    for x in range(len(xelcior)):
                        xelcior[x] -= 50
                        tiledata[i]["x"] = xelcior
                elif bob.x < 50:
                    for x in range(len(xelcior)):
                        xelcior[x] += 50
                        tiledata[i]["x"] = xelcior
                elif bob.y + 50 > 430:
                    for y in range(len(yavaltal)):
                        yavaltal[y] -= 50
                        tiledata[i]["y"] = yavaltal
                elif bob.y < 50:
                    for y in range(len(yavaltal)):
                        yavaltal[y] += 50
                        tiledata[i]["y"] = yavaltal
            else:
                print("error this part wasn't added yet since the dev got bored and left")
                exit()

        for i in portals:
            if Nu_Move_enabled == False:
                xake1 = portals[i]["x1"]
                lye1 = portals[i]["y1"]
                xake2 = portals[i]["x2"]
                lye2 = portals[i]["y2"]
                if bob.x + 50 > 590:
                    for x in range(len(xake1)):
                        xake1[x] -= 50
                        xake2[x] -= 50
                        portals[i]["x1"] = xake1
                        portals[i]["x2"] = xake2
                elif bob.x < 50:
                    for x in range(len(xake1)):
                        xake1[x] += 50
                        xake2[x] += 50
                        portals[i]["x1"] = xake1
                        portals[i]["x2"] = xake2
                elif bob.y + 50 > 430:
                    for y in range(len(lye1)):
                        lye1[y] -= 50
                        lye2[y] -= 50
                        portals[i]["y1"] = lye1
                        portals[i]["y2"] = lye2
                elif bob.y < 50:
                    for y in range(len(lye1)):
                        lye1[y] += 50
                        lye2[y] += 50
                        portals[i]["y1"] = lye1
                        portals[i]["y2"] = lye2
            else:
                print("error this part wasn't added yet since the dev got bored and left")
                exit()
            
        for i in wordata: #failed movement system rewrite counter - 2
            if wordata[i]["isgui"] == False:
                shoxtroop = wordata[i]["x"]
                shoytroop = wordata[i]["y"]
                if bob.x + 50 > 590:
                    for x in range(len(shoxtroop)):
                        shoxtroop[x] -= 50
                        wordata[i]["x"] = shoxtroop
                elif bob.x < 50:
                    for x in range(len(shoxtroop)):
                        shoxtroop[x] += 50
                        wordata[i]["x"] = shoxtroop
                elif bob.y + 50 > 430:
                    for y in range(len(shoytroop)):
                        shoytroop[y] -= 50
                        wordata[i]["y"] = shoytroop
                elif bob.y < 50:
                    for y in range(len(shoytroop)):
                        shoytroop[y] += 50
                        wordata[i]["y"] = shoytroop

        if bob.x + 50 > 590:
            bob.x -= 50
            thingamabobx -= 50
            dosx -= 50
        elif bob.x < 50:
            bob.x += 50
            thingamabobx += 50
            dosx += 50
        elif bob.y + 50 > 430:
            bob.y -= 50
            thingamaboby -= 50
            dosy -= 50
        elif bob.y < 50:
            bob.y += 50
            thingamaboby += 50
            dosy += 50

        #portal cooldown
        if cooldown > 0:
            cooldown -= 1

        #editing gui below
        if Edit_Mode == True:
            button = pygame.draw.circle(screen, (255, 128, 0), (600, 440), 30)
            futton = pygame.draw.circle(screen, (128, 255, 0), (530, 440), 30)
            lutton = pygame.draw.circle(screen, (0, 128, 255), (460, 440), 30)
            cutton = pygame.draw.circle(screen, (255, 128, 128), (390, 440), 30)
            mutton = pygame.draw.circle(screen, (255, 0, 0), (40, 440), 30)
            putton = pygame.draw.circle(screen, (128, 0, 255), (320, 440), 30)

            #textbased gui
            if tiletype == 0:
                gui("geometery", 0, 40, color = (0, 0, 0))
                gui(basictlist.typelist[basictlist.typelistpos], 0, 0, color = (0, 0, 0))
            elif tiletype == 1:
                gui("portals", 0, 40, color = (0, 0, 0))
                gui(portalist.typelist[portalist.typelistpos], 0, 0, color = (0, 0, 0))
            elif tiletype == 2:
                gui("text", 0, 40, color=(0, 0, 0))
                gui(wordlist.typelist[wordlist.typelistpos], 0, 0, color=(0, 0, 0))

            #tile button
            if futton.collidepoint((mouse_pos)):
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    if tiletype == 0:
                        frass = tiledata[basictlist.typelist[basictlist.typelistpos]].get("x")
                        sasss = tiledata[basictlist.typelist[basictlist.typelistpos]].get("y")
                        yasss = tiledata[basictlist.typelist[basictlist.typelistpos]].get("tags")
                        holding = 1
                        nombre += 1
                    elif tiletype == 1:
                        x1ss = portals[portalist.typelist[portalist.typelistpos]].get("x1")
                        d1ss = portals[portalist.typelist[portalist.typelistpos]].get("y1")
                        x2ss = portals[portalist.typelist[portalist.typelistpos]].get("x2")
                        d2ss = portals[portalist.typelist[portalist.typelistpos]].get("y2")
                        tass = portals[portalist.typelist[portalist.typelistpos]].get("tags")
                        holding = 2
                        nombredos += 1
                    elif tiletype == 2:
                        teXt = wordata[wordlist.typelist[wordlist.typelistpos]].get("x")
                        teYt = wordata[wordlist.typelist[wordlist.typelistpos]].get("y")
                        tetagst = wordata[wordlist.typelist[wordlist.typelistpos]].get("tags")
                        holding = 3
                        nombretres += 1

            #what you do when holding a tile
            if holding != 0:
                mouseoutline = pygame.Rect(mouse_pos[0], mouse_pos[1], 50, 50)
                pygame.draw.rect(screen, (0, 128, 64), mouseoutline)
                if fattius.collidepoint((mouse_pos)):
                    if pygame.mouse.get_pressed() == (0, 0, 1):
                        if holding == 1:
                            frass.append(mouse_pos[0])
                            sasss.append(mouse_pos[1])
                            yasss.append(nombre)
                            holding = 0
                        if holding == 2:
                            if part == 1:
                                thingamabobx = mouse_pos[0]
                                thingamaboby = mouse_pos[1]
                                tagamabob = nombredos
                                holding = 0
                            if part == 2:
                                dosx = mouse_pos[0]
                                dosy = mouse_pos[1]
                                x1ss.append(thingamabobx)
                                d1ss.append(thingamaboby)
                                x2ss.append(dosx)
                                d2ss.append(dosy)
                                tass.append(tagamabob)
                                holding = 0
                        if holding == 3:
                            teXt.append(mouse_pos[0])
                            teYt.append(mouse_pos[1])
                            tetagst.append(nombretres)
                            holding = 0

            #save button
            if cutton.collidepoint((mouse_pos)):
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    #print("for might lord home hoyl for grace so bodly")
                    with open(f"{figgy[0]}/modularity.json", "w") as module:
                        json.dump(tiledata, module, indent = 4)
                        module.close()
                    with open(f"{figgy[0]}/portals.json", "w") as module:
                        json.dump(portals, module, indent = 4)
                        module.close()
                    with open(f"{figgy[0]}/text.json", "w") as module:
                        json.dump(wordata, module, indent=4)
                        module.close()

            #delete button
            if mutton.collidepoint((mouse_pos)):
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    delmode = 1

    #screen refresh (30fps supremicy)
    pygame.display.flip()
    clock.tick(30)