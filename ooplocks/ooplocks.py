#the killers of our auto industry
import pygame
import random
import json
pygame.init()

#important game running details
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
pygame.display.set_caption("ooplocks")
ico = pygame.image.load("ooplocks.ico")
pygame.display.set_icon(ico)

#json decription
gdf = open(str("gamedata.txt"))
gdl = json.load(gdf)
#below is legacy code which should only be used if I royaly f#ck up
#que = open(str("game data/Xpos.txt"))
#datx = json.load(que)
#por_que = open(str("game data/Ypos.txt"))
#daty = json.load(por_que)
#tiene = open(str("game data/tags.txt"))
#tago = json.load(tiene)
#randomtags = open(str("game data/rtags.txt"))
#randomx = open(str("game data/rx.txt"))
#randomy = open(str("game data/ry.txt"))
#rt = json.load(randomtags)
#rx = json.load(randomx)
#ry = json.load(randomy)

class blocks:
    def __init__(self, x, y, w, h, ltag, image = None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.thing = pygame.Rect(self.x, self.y, self.w, self.h)
        self.tag = ltag
        if image != None:
            self.image = pygame.image.load(image)
            self.irect = self.image.get_rect(center = (x, y))
    
    #this code chunck is grass
    def grass(self):
        self.thing.center = (self.x, self.y)
        pygame.draw.rect(screen, (0, 255, 0), self.thing)
        if bob.colliderect(self.thing):
            if direction == "w":
                bob.y += 10
            elif direction == "a":
                bob.x += 10
            elif direction == "s":
                bob.y -= 10
            elif direction == "d":
                bob.x -= 10
        if self.tag == tag[tagil]:
            mouse_pos = pygame.mouse.get_pos()
            if self.thing.collidepoint((mouse_pos)):
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    tag.pop(tagil)
                    ucx.pop(tagil)
                    ucy.pop(tagil)
    def create(gx, gy, gw, gh, ltag):
        block = blocks(gx, gy, gw, gh, ltag)
        block.grass()

    #this code chunck is random
    def random(self):
        r = random.randrange(0, 255)
        g = random.randrange(0, 255)
        b = random.randrange(0, 255)
        pygame.draw.rect(screen, (r, g, b), self.thing)
        if bob.colliderect(self.thing):
            if direction == "w":
                bob.y += 10
            elif direction == "a":
                bob.x += 10
            elif direction == "s":
                bob.y -= 10
            elif direction == "d":
                bob.x -= 10
        if self.tag == gat[bop]:
            mouse_pos = pygame.mouse.get_pos()
            if self.thing.collidepoint((mouse_pos)):
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    gat.pop(bop)
                    dalist.pop(bop)
                    tsilad.pop(bop)
    def reate(gx, gy, gw, gh, ltag):
        block = blocks(gx, gy, gw, gh, ltag)
        block.random()

    def water(self):
        self.thing.center = (self.x, self.y)
        pygame.draw.rect(screen, (0, 0, 255), self.thing)
        if bob.colliderect(self.thing):
            if direction == "w":
                bob.y += 10
            elif direction == "a":
                bob.x += 10
            elif direction == "s":
                bob.y -= 10
            elif direction == "d":
                bob.x -= 10
        if self.tag == wtag[wltag]:
            mouse_pos = pygame.mouse.get_pos()
            if self.thing.collidepoint((mouse_pos)):
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    wtag.pop(wltag)
                    wdx.pop(wltag)
                    wdy.pop(wltag)
    def wreate(gx, gy, gw, gh, ltag):
        block = blocks(gx, gy, gw, gh, ltag)
        block.water()

    def diskette(self):
        self.thing.center = (self.x, self.y)
        pygame.draw.rect(screen, (0, 0, 255), self.thing)
        screen.blit(self.image, (self.x - 25, self.y - 25))
        if bob.colliderect(self.thing):
            if direction == "w":
                bob.y += 10
            elif direction == "a":
                bob.x += 10
            elif direction == "s":
                bob.y -= 10
            elif direction == "d":
                bob.x -= 10
        if self.tag == dtag[dltag]:
            mouse_pos = pygame.mouse.get_pos()
            if self.thing.collidepoint((mouse_pos)):
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    dtag.pop(dltag)
                    ddx.pop(dltag)
                    ddy.pop(dltag)
    def dreate(gx, gy, gw, gh, ltag):
        block = blocks(gx, gy, gw, gh, ltag, "savepos.png")
        block.diskette()

#variables, too many variables
gx = 200
gy = 200
gw = 50
gh = 50
#the four above are old and don't matter

#player
bobert = pygame.Surface((50, 50))
bob = pygame.Surface.get_rect(bobert, topleft = (1, 0))
bobert.fill((244, 255, 220))

direction = "" #important collision thing
background = pygame.Surface((1000, 1000))#read the name of the variable
#this is how we know where to draw blocks, their coordinates are stored in these lists
dalist = [-65535]
tsilad = [-65535]
ucx = [-65535]
ucy = [-65535]
tag = [-65535]
gat = [-65535]
#below this line are the things that I know are important but I don't know what they do
#water variables
wdx = [-65535] #x pos
wdy = [-65535] #y pos
wtag = [-65535] #tags
wltag = 0 #tag pos
wctag = 0 #tag counter

#diskette variables
ddx = [-65535] #x pos
ddy = [-65535] #y pos
dtag = [-65535] #tags
dltag = 0 #tag pos
dctag = 0 #tag counter

tagile = 0
hold = 0
fattius = pygame.Rect(0, 0, 640, 480)#more background things
thanx = 0
thany = 0
tagil = 0
bop = 0
pob = 0
title = 1
lines = 0
pb = pygame.Surface((65, 50))
tbnrfrags = pb.get_rect(center = (320, 240)) #the last time I watched this channel was in 2022
lobdo = pygame.image.load("newerrlogo.png") #TEH EPIK LOOGO
tile = "grass"

font = pygame.font.Font("Grand9K Pixel.ttf", 30) #yes

block = blocks(gx, gy, gw, gh, tag[tagil]) #I don't know what this does

#loading all save data into the lists
ucx.clear()
ucy.clear()
tag.clear()
dalist.clear()
tsilad.clear()
gat.clear()
wdx.clear()
wdy.clear()
wtag.clear()
ddx.clear()
ddy.clear()
dtag.clear()

ucx.extend(gdl[0])
ucy.extend(gdl[1])
tag.extend(gdl[2])
dalist.extend(gdl[3])
tsilad.extend(gdl[4])
gat.extend(gdl[5])
wdx.extend(gdl[6])
wdy.extend(gdl[7])
wtag.extend(gdl[8])
ddx.extend(gdl[9])
ddy.extend(gdl[10])
dtag.extend(gdl[11])

#below is legacy code which should only be used if I royaly f#ck up
#ucx.extend(datx)
#ucy.extend(daty)
#tag.extend(tago)
#gat.extend(rt)
#dalist.extend(rx)
#tsilad.extend(ry)

#text based gui builder
def gui(words: str, x: int, y: int, bob = None):
    mouse_pos = pygame.mouse.get_pos()
    guy = font.render(words, False, (255, 255, 0))
    guing = guy.get_rect(topleft = (x, y))
    screen.blit(guy, guing)
    if guing.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if bob != None:
                bob()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

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
        gui("Geotec 1.3 and built on pygame,", 0, 90)
        gui("press escape to exit.", 0, 135)

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
            bob.y -= 10
            direction = "w"
        elif keys[pygame.K_a]:
            bob.x -= 10
            direction = "a"
        elif keys[pygame.K_s]:
            bob.y += 10
            direction = "s"
        elif keys[pygame.K_d]:
            bob.x += 10
            direction = "d"
        elif keys [pygame.K_ESCAPE]:
            title = 1

        #the main flaw of my gui non-library
        def switchgrass():
            global tile
            tile = "grass"
        def switchwater():
            global tile
            tile = "water"
        def switchdisk():
            global tile
            tile = "disk"

        #text based gui
        gui("Grass", 0, 0, switchgrass)
        gui("Water", 0, 50, switchwater)
        gui("disk", 0, 100, switchdisk)


        screen.blit(bobert, bob) #player

        #the only thing that makes map editing not impossible
        if lines == 1:
            scanline = 50
            for i in range(13):
                pygame.draw.line(screen, (255, 255, 255), (scanline * i + 1, 0), (scanline * i + 1, 480))
                pygame.draw.line(screen, (255, 255, 255), (0, scanline * i + 1), (640, scanline * i + 1))

        #reset for variables
        listx = 0
        listy = 0
        bop = 0

        #below is how map drawing works dont ask me how, it just does
        while listx != len(dalist) and listy != len(tsilad):
            if listx > len(dalist) or listy > len(tsilad) or bop > len(gat):
                listx = 0
                listy = 0
                bop = 0
            blocks.reate(dalist[listx], tsilad[listy], 50, 50, gat[bop])
            listx += 1
            listy += 1
            bop += 1

        #more variable resets
        thany = 0
        thanx = 0
        tagil = 0

        #the definition of boberick is zero and you would know that if you could read the text below moron
        boberick = 0
        hendy = 0
        pescado = 0
        miska = 0

        #camera funcionality easier to understand than the drawing
        if bob.x + 50 > 640:
            bob.x -= 50
            for i in ucx:
                ucx[boberick] = i - 50
                boberick += 1
            for i in dalist:
                dalist[hendy] = i - 50
                hendy += 1
            for i in wdx:
                wdx[pescado] = i - 50
                pescado += 1
            for i in ddx:
                ddx[miska] = i - 50
                miska += 1
        miska = 0
        pescado = 0
        hendy = 0
        boberick = 0

        if bob.x < 0:
            bob.x += 50
            for i in ucx:
                ucx[boberick] = i + 50
                boberick += 1
            for i in dalist:
                dalist[hendy] = i + 50
                hendy += 1
            for i in wdx:
                wdx[pescado] = i + 50
                pescado += 1
            for i in ddx:
                ddx[miska] = i + 50
                miska += 1
        miska = 0
        pescado = 0
        hendy = 0
        boberick = 0

        if bob.y + 50 > 480:
            bob.y -= 50
            for i in ucy:
                ucy[boberick] = i - 50
                boberick += 1
            for i in tsilad:
                tsilad[hendy] = i - 50
                hendy += 1
            for i in wdy:
                wdy[pescado] = i - 50
                pescado += 1
            for i in ddy:
                ddy[miska] = i - 50
                miska += 1
        miska = 0
        pescado = 0
        hendy = 0
        boberick = 0

        if bob.y < 0:
            bob.y += 50
            for i in ucy:
                ucy[boberick] = i + 50
                boberick += 1
            for i in tsilad:
                tsilad[hendy] = i + 50
                hendy += 1
            for i in wdy:
                wdy[pescado] = i + 50
                pescado += 1
            for i in ddy:
                ddy[miska] = i + 50
                miska += 1
        miska = 0
        pescado = 0
        hendy = 0
        boberick = 0

        #more pythonic black magic that I thought up and wrote and still have no idea how it works
        while thanx != len(ucx) and thany != len(ucy):
            if thanx > len(ucx) or thany > len(ucy) or tagil > len(tag):
                thanx = 0
                thany = 0
                tagil = 0
            blocks.create(ucx[thanx], ucy[thany], 50, 50, tag[tagil])
            thanx += 1
            thany += 1
            tagil += 1

        #so many d@mn resets
        tagil = 0
        thany = 0
        thanx = 0

        while thanx != len(wdx) and thany != len(wdy):
            if thanx > len(wdx) or thany > len(wdy) or wltag > len(wtag):
                thanx = 0
                thany = 0
                wltag = 0
            blocks.wreate(wdx[thanx], wdy[thany], 50, 50, wtag[wltag])
            thanx += 1
            thany += 1
            wltag += 1
        
        wltag = 0
        thany = 0
        thanx = 0

        while thanx != len(ddx) and thany != len(ddy):
            if thanx > len(ddx) or thany > len(ddy) or dltag > len(dtag):
                thanx = 0
                thany = 0
                dltag = 0
            blocks.dreate(ddx[thanx], ddy[thany], 50, 50, dtag[dltag])
            thanx += 1
            thany += 1
            dltag += 1

        dltag = 0
        thany = 0
        thanx = 0

        #gui
        button = pygame.draw.circle(screen, (255, 128, 0), (600, 440), 30)
        futton = pygame.draw.circle(screen, (128, 255, 0), (530, 440), 30)
        lutton = pygame.draw.circle(screen, (0, 128, 255), (460, 440), 30)
        cutton = pygame.draw.circle(screen, (255, 128, 128), (390, 440), 30)

        #random button
        if button.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                rx = random.randrange(0, 640)
                ry = random.randrange(0, 480)
                dalist.append(rx)
                tsilad.append(ry)
                gat.append(pob)
                pob += 1

        #tile button
        if futton.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if tile == "grass":
                    hold = 1
                elif tile == "water":
                    hold = 2
                elif tile == "disk":
                    hold = 3

        #lines button
        if lutton.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                if lines == 0:
                    lines = 1
                elif lines == 1:
                    lines = 0
        
        #file opening protocall | Legacy feature
        def fop(file: str, list):
            with open(file, "w") as fufa:
                json.dump(list, fufa)
                fufa.close()

        #save button
        if cutton.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                with open("gamedata.txt", "w") as fufa:
                    json.dump((ucx, ucy, tag, dalist, tsilad, gat, wdx, wdy, wtag, ddx, ddy, dtag), fufa)
                    fufa.close()
                #for might lord home hoyl for grace so bodly
                
        #what happens when you are holding a block
        if hold == 1:
            blocks.create(mouse_pos[0], mouse_pos[1], 50, 50, 0)
            if fattius.collidepoint((mouse_pos)):
                if pygame.mouse.get_pressed() == (0, 0, 1):
                    ucx.append(mouse_pos[0])
                    ucy.append(mouse_pos[1])
                    tag.append(tagile)
                    tagile += 1
                    hold = 0
        elif hold == 2:
            blocks.wreate(mouse_pos[0], mouse_pos[1], 50, 50, 0)
            if fattius.collidepoint((mouse_pos)):
                if pygame.mouse.get_pressed() == (0, 0, 1):
                    wdx.append(mouse_pos[0])
                    wdy.append(mouse_pos[1])
                    wtag.append(wctag)
                    wctag += 1
                    hold = 0
        elif hold == 3:
            blocks.dreate(mouse_pos[0], mouse_pos[1], 50, 50, 0)
            if fattius.collidepoint((mouse_pos)):
                if pygame.mouse.get_pressed() == (0, 0, 1):
                    ddx.append(mouse_pos[0])
                    ddy.append(mouse_pos[1])
                    dtag.append(dctag)
                    dctag += 1
                    hold = 0

    #screen refresh (30fps supremicy)
    pygame.display.flip()
    clock.tick(30)