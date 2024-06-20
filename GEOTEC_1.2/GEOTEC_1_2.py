import pygame
import json
import asset
import zipfile
pygame.init

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
pygame.display.set_caption("GEOTEC")
GeotecIcon = pygame.image.load("GEOTECICON.png")
pygame.display.set_icon(GeotecIcon)

nd = 2 #nd = 1, no new data. nd = 0, reset, nd = 2, edit mode
numthing = 0

if nd == 0:
    #locations
    s2rfx = 0
    s2rfy = 0
    s3rfx = 0
    s3rfy = 0
    s4rfx = 0
    s4rfy = 0
    s5rfx = 0
    s5rfy = 0
    s6rfx = 0
    s6rfy = 0
    s7rfx = 0
    s7rfy = 0
    s8rfx = 0
    s8rfy = 0
    s9rfx = 0
    s9rfy = 0
    s10rfx = 0
    s10rfy = 0
    s11rfx = 0
    s11rfy = 0
    s12rfx = 0
    s12rfy = 0
    s13rfx = 0
    s13rfy = 0
    s14rfx = 0
    s14rfy = 0
    s15rfx = 0
    s15rfy = 0
    s16rfx = 0
    s16rfy = 0
    s17rfx = 0
    s17rfy = 0
    s18rfx = 0
    s18rfy = 0
    s19rfx = 0
    s19rfy = 0
    s20rfx = 0
    s20rfy = 0
    s21rfx = 0
    s21rfy = 0
    s22rfx = 0
    s22rfy = 0
    s23rfx = 0
    s23rfy = 0

    #colors
    s2color = (255, 100, 255)
    s3color = (255, 100, 255)
    s4color = (255, 100, 255)
    s5color = (255, 100, 255)
    s6color = (255, 100, 255)
    s7color = (255, 100, 255)
    s8color = (255, 100, 255)
    s2color = (255, 100, 255)
    s3color = (255, 100, 255)
    s4color = (255, 100, 255)
    s5color = (255, 100, 255)
    s6color = (255, 100, 255)
    s7color = (255, 100, 255)
    s8color = (255, 100, 255)
    s9color = (255, 100, 255)
    s10color = (255, 100, 255)
    s11color = (255, 100, 255)
    s12color = (255, 100, 255)
    s13color = (255, 100, 255)
    s14color = (255, 100, 255)
    s15color = (255, 100, 255)
    s16color = (255, 100, 255)
    s17color = (255, 100, 255)
    s18color = (255, 100, 255)
    s19color = (255, 100, 255)
    s20color = (255, 100, 255)
    s21color = (255, 100, 255)
    s22color = (255, 100, 255)
    s23color = (255, 100, 255)
if nd == 2:
    s2rfx = asset.loc[0]
    s2rfy = asset.loc[1]
    s3rfx = asset.loc[2]
    s3rfy = asset.loc[3]
    s4rfx = asset.loc[4]
    s4rfy = asset.loc[5]
    s5rfx = asset.loc[6]
    s5rfy = asset.loc[7]
    s6rfx = asset.loc[8]
    s6rfy = asset.loc[9]
    s7rfx = asset.loc[10]
    s7rfy = asset.loc[11]
    s8rfx = asset.loc[12]
    s8rfy = asset.loc[13]
    s9rfx = asset.loc[14]
    s9rfy = asset.loc[15]
    s10rfx = asset.loc[16]
    s10rfy = asset.loc[17]
    s11rfx = asset.loc[18]
    s11rfy = asset.loc[19]
    s12rfx = asset.loc[20]
    s12rfy = asset.loc[21]
    s13rfx = asset.loc[22]
    s13rfy = asset.loc[23]
    s14rfx = asset.loc[24]
    s14rfy = asset.loc[25]
    s15rfx = asset.loc[26]
    s15rfy = asset.loc[27]
    s16rfx = asset.loc[28]
    s16rfy = asset.loc[29]
    s17rfx = asset.loc[30]
    s17rfy = asset.loc[31]
    s18rfx = asset.loc[32]
    s18rfy = asset.loc[33]
    s19rfx = asset.loc[34]
    s19rfy = asset.loc[35]
    s20rfx = asset.loc[36]
    s20rfy = asset.loc[37]
    s21rfx = asset.loc[38]
    s21rfy = asset.loc[39]
    s22rfx = asset.loc[40]
    s22rfy = asset.loc[41]
    s23rfx = asset.loc[42]
    s23rfy = asset.loc[43]

    #color section
    s2color = (asset.clr[0])
    s3color = (asset.clr[1])
    s4color = (asset.clr[2])
    s5color = (asset.clr[3])
    s6color = (asset.clr[4])
    s7color = (asset.clr[5])
    s8color = (asset.clr[6])
    s9color = (asset.clr[7])
    s10color = (asset.clr[8])
    s11color = (asset.clr[9])
    s12color = (asset.clr[10])
    s13color = (asset.clr[11])
    s14color = (asset.clr[12])
    s15color = (asset.clr[13])
    s16color = (asset.clr[14])
    s17color = (asset.clr[15])
    s18color = (asset.clr[16])
    s19color = (asset.clr[17])
    s20color = (asset.clr[18])
    s21color = (asset.clr[19])
    s22color = (asset.clr[20])
    s23color = (asset.clr[21])

opn = open("data.txt")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if nd == 2 or nd == 0:
                with open("data.txt", "w") as file:
                    json.dump((s2rfx, s2rfy, s3rfx, s3rfy, s4rfx, s4rfy, s5rfx, s5rfy, s6rfx, s6rfy, s7rfx, s7rfy, s8rfx, s8rfy,
                                s9rfx, s9rfy, s10rfx, s10rfy, s11rfx, s11rfy, s12rfx, s12rfy, s13rfx, s13rfy, s14rfx, s14rfy,
                                s15rfx, s15rfy, s16rfx, s16rfy, s17rfx, s17rfy, s18rfx, s18rfy, s19rfx, s19rfy, s20rfx, s20rfy,
                                s21rfx, s21rfy, s22rfx, s22rfy, s23rfx, s23rfy), file)
                with open("colors.txt", "w") as file2:
                    json.dump((s2color, s3color, s4color, s5color, s6color, s7color, s8color, s9color, s10color,
                               s11color, s12color, s13color, s14color, s15color, s16color, s17color, s18color, s19color,
                               s20color, s21color, s22color, s23color), file2)
            pygame.quit
            exit()

    willybonka = pygame.draw.rect(screen, (0, 0, 0), (0, 0, 1000, 1000))
    
    #movitron
    asset.keys()

    #selectitron
    button = pygame.Surface((50, 50))
    buttonn = button.get_rect(bottomright = (640, 480))
    button.fill((255, 0, 0))
    button.set_alpha(128)
    pygame.Surface.convert_alpha(asset.cmds)
    asset.cmds.set_alpha(128)

    #numbitron
    button2 = pygame.Surface((50, 50))
    buttonn2 = button.get_rect(bottomright = (590, 480))
    button2.fill((255, 255, 0))
    button2.set_alpha(128)
    pygame.Surface.convert_alpha(asset.nums)
    asset.nums.set_alpha(128)
    
    #centitron
    button3 = pygame.Surface((50, 50))
    buttonn3 = button3.get_rect(bottomright = (540, 480))
    button3.fill((0, 100, 255))
    button3.set_alpha(128)
    pygame.Surface.convert_alpha(asset.dics)
    asset.dics.set_alpha(128)

    #paintitron
    button4 = pygame.Surface((50, 50))
    buttonn4 = button4.get_rect(bottomright = (490, 480))
    button4.fill((255, 128, 0))
    button4.set_alpha(128)
    pygame.Surface.convert_alpha(asset.pain)
    asset.pain.set_alpha(128)

    #coorditron
    #bob = str(asset.posx, asset.posy)
    pos = asset.font.render("{}, {}".format(asset.posx, asset.posy), False, (255, 255, 0))


    #cmds
    mouse_pos = pygame.mouse.get_pos()
    if buttonn.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            cmd = input("control what tile: ")
            if cmd == "help":
                print("type in then a number to choose a tile to control ex. - s2")
            if cmd == "s2":
                asset.tracker = 2
            if cmd == "s3":
                asset.tracker = 3
            if cmd == "s4":
                asset.tracker = 4
            if cmd == "s5":
                asset.tracker = 5
            if cmd == "s6":
                asset.tracker = 6
            if cmd == "s7":
                asset.tracker = 7
            if cmd == "s8":
                asset.tracker = 8
            if cmd == "s9":
                asset.tracker = 9
            if cmd == "s10":
                asset.tracker = 10
            if cmd == "s11":
                asset.tracker = 11
            if cmd == "s12":
                asset.tracker = 12
            if cmd == "s13":
                asset.tracker = 13
            if cmd == "s14":
                asset.tracker = 14
            if cmd == "s15":
                asset.tracker = 15
            if cmd == "s16":
                asset.tracker = 16
            if cmd == "s17":
                asset.tracker = 17
            if cmd == "s18":
                asset.tracker = 18
            if cmd == "s19":
                asset.tracker = 19
            if cmd == "s20":
                asset.tracker = 20
            if cmd == "s21":
                asset.tracker = 21
            if cmd == "s22":
                asset.tracker = 22
            if cmd == "s23":
                asset.tracker = 23
    #numbers
    if buttonn2.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            numthing = 1
        else:
            numthing = 0 
    #saves
    if buttonn3.collidepoint(mouse_pos):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if nd == 2 or nd == 0:
                s2rfx = asset.s2r.x
                s2rfy = asset.s2r.y
                s3rfx = asset.s3r.x
                s3rfy = asset.s3r.y
                s4rfx = asset.s4r.x
                s4rfy = asset.s4r.y
                s5rfx = asset.s5r.x
                s5rfy = asset.s5r.y
                s6rfx = asset.s6r.x
                s6rfy = asset.s6r.y
                s7rfx = asset.s7r.x
                s7rfy = asset.s7r.y
                s8rfx = asset.s8r.x
                s8rfy = asset.s8r.y
                s9rfx = asset.s9r.x
                s9rfy = asset.s9r.y
                s10rfx = asset.s10r.x
                s10rfy = asset.s10r.y
                s11rfx = asset.s11r.x
                s11rfy = asset.s11r.y
                s12rfx = asset.s12r.x
                s12rfy = asset.s12r.y
                s13rfx = asset.s13r.x
                s13rfy = asset.s13r.y
                s14rfx = asset.s14r.x
                s14rfy = asset.s14r.y
                s15rfx = asset.s15r.x
                s15rfy = asset.s15r.y
                s16rfx = asset.s16r.x
                s16rfy = asset.s16r.y
                s17rfx = asset.s17r.x
                s17rfy = asset.s17r.y
                s18rfx = asset.s18r.x
                s18rfy = asset.s18r.y
                s19rfx = asset.s19r.x
                s19rfy = asset.s19r.y
                s20rfx = asset.s20r.x
                s20rfy = asset.s20r.y
                s21rfx = asset.s21r.x
                s21rfy = asset.s21r.y
                s22rfx = asset.s22r.x
                s22rfy = asset.s22r.y
                s23rfx = asset.s23r.x
                s23rfy = asset.s23r.y

    #how we figure out what is being used
    asset.trackitron()

    #how we place stuff and where it should be placed
    if willybonka.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (0, 0, 1):
            if asset.tracker == 2:
                (asset.s2r.x, asset.s2r.y) = mouse_pos
                (s2rfx, s2rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 3:
                (asset.s3r.x, asset.s3r.y) = mouse_pos
                (s3rfx, s3rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 4:
                (asset.s4r.x, asset.s4r.y) = mouse_pos
                (s4rfx, s4rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 5:
                (asset.s5r.x, asset.s5r.y) = mouse_pos
                (s5rfx, s5rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 6:
                (asset.s6r.x, asset.s6r.y) = mouse_pos
                (s6rfx, s6rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 7:
                (asset.s7r.x, asset.s7r.y) = mouse_pos
                (s7rfx, s7rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 8:
                (asset.s8r.x, asset.s8r.y) = mouse_pos
                (s8rfx, s8rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 9:
                (asset.s9r.x, asset.s9r.y) = mouse_pos
                (s9rfx, s9rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 10:
                (asset.s10r.x, asset.s10r.y) = mouse_pos
                (s10rfx, s10rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 11:
                (asset.s11r.x, asset.s11r.y) = mouse_pos
                (s11rfx, s11rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 12:
                (asset.s12r.x, asset.s12r.y) = mouse_pos
                (s12rfx, s12rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 13:
                (asset.s13r.x, asset.s13r.y) = mouse_pos
                (s13rfx, s13rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 14:
                (asset.s14r.x, asset.s14r.y) = mouse_pos
                (s14rfx, s14rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 15:
                (asset.s15r.x, asset.s15r.y) = mouse_pos
                (s15rfx, s15rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 16:
                (asset.s16r.x, asset.s16r.y) = mouse_pos
                (s16rfx, s16rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 17:
                (asset.s17r.x, asset.s17r.y) = mouse_pos
                (s17rfx, s17rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 18:
                (asset.s18r.x, asset.s18r.y) = mouse_pos
                (s18rfx, s18rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 19:
                (asset.s19r.x, asset.s19r.y) = mouse_pos
                (s19rfx, s19rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 20:
                (asset.s20r.x, asset.s20r.y) = mouse_pos
                (s20rfx, s20rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 21:
                (asset.s21r.x, asset.s21r.y) = mouse_pos
                (s21rfx, s21rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 22:
                (asset.s22r.x, asset.s22r.y) = mouse_pos
                (s22rfx, s22rfy) = mouse_pos
                asset.tracker = 0
            elif asset.tracker == 23:
                (asset.s23r.x, asset.s23r.y) = mouse_pos
                (s23rfx, s23rfy) = mouse_pos
                asset.tracker = 0

    #where all the colorful magic happens
    if buttonn4.collidepoint(mouse_pos):
       if pygame.mouse.get_pressed() == (1, 0, 0):
            colordata = [int(x) for x in input("type in an rgb value with spaces as seperators: ").split()]
            colorcode = tuple(colordata)
            if asset.tracker == 2:
               asset.s2.fill(colorcode)
               s2color = colorcode
            elif asset.tracker == 3:
               asset.s3.fill(colorcode)
               s3color = colorcode
            elif asset.tracker == 4:
               asset.s4.fill(colorcode)
               s4color = colorcode
            elif asset.tracker == 5:
               asset.s5.fill(colorcode)
               s5color = colorcode
            elif asset.tracker == 6:
               asset.s6.fill(colorcode)
               s6color = colorcode
            elif asset.tracker == 7:
               asset.s7.fill(colorcode)
               s7color = colorcode
            elif asset.tracker == 8:
               asset.s8.fill(colorcode)
               s8color = colorcode
            elif asset.tracker == 9:
               asset.s9.fill(colorcode)
               s9color = colorcode
            elif asset.tracker == 10:
               asset.s10.fill(colorcode)
               s10color = colorcode
            elif asset.tracker == 11:
               asset.s11.fill(colorcode)
               s11color = colorcode
            elif asset.tracker == 12:
               asset.s12.fill(colorcode)
               s12color = colorcode
            elif asset.tracker == 13:
               asset.s13.fill(colorcode)
               s13color = colorcode
            elif asset.tracker == 14:
               asset.s14.fill(colorcode)
               s14color = colorcode
            elif asset.tracker == 15:
               asset.s15.fill(colorcode)
               s15color = colorcode
            elif asset.tracker == 16:
               asset.s16.fill(colorcode)
               s16color = colorcode
            elif asset.tracker == 17:
               asset.s17.fill(colorcode)
               s17color = colorcode
            elif asset.tracker == 18:
               asset.s18.fill(colorcode)
               s18color = colorcode
            elif asset.tracker == 19:
               asset.s19.fill(colorcode)
               s19color = colorcode
            elif asset.tracker == 20:
               asset.s20.fill(colorcode)
               s20color = colorcode
            elif asset.tracker == 21:
               asset.s21.fill(colorcode)
               s21color = colorcode
            elif asset.tracker == 22:
               asset.s22.fill(colorcode)
               s22color = colorcode
            elif asset.tracker == 23:
               asset.s23.fill(colorcode)
               s23color = colorcode

    #all else drawing
    screen.blit(asset.s2, asset.s2r)
    screen.blit(asset.s3, asset.s3r)
    screen.blit(asset.s4, asset.s4r)
    screen.blit(asset.s5, asset.s5r)
    screen.blit(asset.s6, asset.s6r)
    screen.blit(asset.s7, asset.s7r)
    screen.blit(asset.s8, asset.s8r)
    screen.blit(asset.s9, asset.s9r)
    screen.blit(asset.s10, asset.s10r)
    screen.blit(asset.s11, asset.s11r)
    screen.blit(asset.s12, asset.s12r)
    screen.blit(asset.s13, asset.s13r)
    screen.blit(asset.s14, asset.s14r)
    screen.blit(asset.s15, asset.s15r)
    screen.blit(asset.s16, asset.s16r)
    screen.blit(asset.s17, asset.s17r)
    screen.blit(asset.s18, asset.s18r)
    screen.blit(asset.s19, asset.s19r)
    screen.blit(asset.s20, asset.s20r)
    screen.blit(asset.s21, asset.s21r)
    screen.blit(asset.s22, asset.s22r)
    screen.blit(asset.s23, asset.s23r)
    if numthing == 1:
        screen.blit(asset.s2t, asset.s2r)
        screen.blit(asset.s3t, asset.s3r)
        screen.blit(asset.s4t, asset.s4r)
        screen.blit(asset.s5t, asset.s5r)
        screen.blit(asset.s6t, asset.s6r)
        screen.blit(asset.s7t, asset.s7r)
        screen.blit(asset.s8t, asset.s8r)
        screen.blit(asset.s9t, asset.s9r)
        screen.blit(asset.s10t, asset.s10r)
        screen.blit(asset.s11t, asset.s11r)
        screen.blit(asset.s12t, asset.s12r)
        screen.blit(asset.s13t, asset.s13r)
        screen.blit(asset.s14t, asset.s14r)
        screen.blit(asset.s15t, asset.s15r)
        screen.blit(asset.s16t, asset.s16r)
        screen.blit(asset.s17t, asset.s17r)
        screen.blit(asset.s18t, asset.s18r)
        screen.blit(asset.s19t, asset.s19r)
        screen.blit(asset.s20t, asset.s20r)
        screen.blit(asset.s21t, asset.s21r)
        screen.blit(asset.s22t, asset.s22r)
        screen.blit(asset.s23t, asset.s23r)
    
    #middleitron
    if nd == 2 or nd == 0:
        asset.centre.set_alpha(128)
        screen.blit(asset.centre, asset.center)

    #player
    asset.s1.fill((0, 100, 255))
    screen.blit(asset.s1, asset.s1r)

    #screengui
    if nd == 2 or nd == 0:
        screen.blit(asset.cmds, buttonn)
        screen.blit(asset.nums, buttonn2)
        screen.blit(asset.dics, buttonn3)
        screen.blit(asset.pain, buttonn4)
        screen.blit(pos, (0, 0))

    pygame.display.flip()
    clock.tick(30)