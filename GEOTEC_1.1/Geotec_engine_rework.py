import pygame
import json
import sys
pygame.init()

#important, this engine supports 80 tiles only more tiles will be added with time

var = 0
nd = 0
utn = 1
tick = 1

screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("G3DTEK")

font = pygame.font.Font("Grand9K Pixel.ttf", 50)

data = {
    "dx" : 590,
    "dy" : 480,
    "rx" : 640,
    "ry" : 480,
    "ux" : 590,
    "uy" : 430,
    "lx" : 540,
    "ly" : 480,
    "x1" : 0,
    "y1" : 0,
    "x2" : 0,
    "y2" : 0,
    "x3" : 0,
    "y3" : 0,
    "x4" : 0,
    "y4" : 0,
    "x5" : 0,
    "y5" : 0,
    "x6" : 0,
    "y6" : 0,
    "x7" : 0,
    "y7" : 0,
    "x8" : 0,
    "y8" : 0,
    "x9" : 0,
    "y9" : 0,
    "x10" : 0,
    "y10" : 0,
    "x11" : 0,
    "y11" : 0,
    "x12" : 0,
    "y12" : 0,
    "x13" : 0,
    "y13" : 0,
    "x14" : 0,
    "y14" : 0,
    "x15" : 0,
    "y15" : 0,
    "x16" : 0,
    "y16" : 0,
    "x17" : 0,
    "y17" : 0,
    "x18" : 0,
    "y18" : 0,
    "x19" : 0,
    "y19" : 0,
    "x20" : 0,
    "y20" : 0,
    "x21" : 0,
    "y21" : 0,
    "x22" : 0,
    "y22" : 0,
    "x23" : 0,
    "y23" : 0,
    "x24" : 0,
    "y24" : 0,
    "x25" : 0,
    "y25" : 0,
    "x26" : 0,
    "y26" : 0,
    "x27" : 0,
    "y27" : 0,
    "x28" : 0,
    "y28" : 0,
    "x29" : 0,
    "y29" : 0,
    "x30" : 0,
    "y30" : 0,
    "x31" : 0,
    "y31" : 0,
    "x32" : 0,
    "y32" : 0,
    "x33" : 0,
    "y33" : 0,
    "x34" : 0,
    "y34" : 0,
    "x35" : 0,
    "y35" : 0,
    "x36" : 0,
    "y36" : 0,
    "x37" : 0,
    "y37" : 0,
    "x38" : 0,
    "y38" : 0,
    "x39" : 0,
    "y39" : 0,
    "x40" : 0,
    "y40" : 0,
    "x41" : 0,
    "y41" : 0,
    "x42" : 0,
    "y42" : 0,
    "x43" : 0,
    "y43" : 0,
    "x44" : 0,
    "y44" : 0,
    "x45" : 0,
    "y45" : 0,
    "x46" : 0,
    "y46" : 0,
    "x47" : 0,
    "y47" : 0,
    "x48" : 0,
    "y48" : 0,
    "x49" : 0,
    "y49" : 0,
    "x50" : 0,
    "y50" : 0,
    "x51" : 0,
    "y51" : 0,
    "x52" : 0,
    "y52" : 0,
    "x53" : 0,
    "y53" : 0,
    "x54" : 0,
    "y54" : 0,
    "x55" : 0,
    "y55" : 0,
    "x56" : 0,
    "y56" : 0,
    "x57" : 0,
    "y57" : 0,
    "x58" : 0,
    "y58" : 0,
    "x59" : 0,
    "y59" : 0,
    "x60" : 0,
    "y60" : 0,
    "x61" : 0,
    "y61" : 0,
    "x62" : 0,
    "y62" : 0,
    "x63" : 0,
    "y63" : 0,
    "x64" : 0,
    "y64" : 0,
    "x65" : 0,
    "y65" : 0,
    "x66" : 0,
    "y66" : 0,
    "x67" : 0,
    "y67" : 0,
    "x68" : 0,
    "y68" : 0,
    "x69" : 0,
    "y69" : 0,
    "x70" : 0,
    "y70" : 0,
    "x71" : 0,
    "y71" : 0,
    "x72" : 0,
    "y72" : 0,
    "x73" : 0,
    "y73" : 0,
    "x74" : 0,
    "y74" : 0,
    "x75" : 0,
    "y75" : 0,
    "x76" : 0,
    "y76" : 0,
    "x77" : 0,
    "y77" : 0,
    "x78" : 0,
    "y78" : 0,
    "x79" : 0,
    "y79" : 0,
    "x80" : 0,
    "y80" : 0,
}

if nd == 0:
    with open("engine_details.txt") as DATA:
        data = json.load(DATA)
        
tile1 = pygame.Surface((50, 50))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if var == 0:
                with open("engine_details.txt", "w") as DATA:
                    json.dump(data, DATA)
            pygame.quit()
            sys.exit(0)
                    

    txtx = f"{data['dx']}"
    txty = f"{data['dy']}"
    Rightx = f"{data['rx']}"
    Righty = f"{data['ry']}"
    Upx = f"{data['ux']}"
    Upy = f"{data['uy']}"
    Leftx = f"{data['lx']}"
    Lefty = f"{data['ly']}"
    t1posx = f"{data['x1']}"
    t1posy = f"{data['y1']}"

    screen.fill((0, 0, 0))
    
    tile1r = tile1.get_rect(topleft = (int(t1posx), int(t1posy)))
    screen.blit(tile1, tile1r)
    tile1.fill((255, 255, 255))
    if var == 0:
        txt = font.render("D", False, (255, 255, 0))
        txt_rect = txt.get_rect(bottomright = (int(txtx), int(txty)))
        screen.blit(txt, txt_rect)
        R = font.render("R", False, (255, 255, 0))
        R_rect = txt.get_rect(bottomright = (int(Rightx), int(Righty)))
        screen.blit(R, R_rect)
        L = font.render("L", False, (255, 255, 0))
        L_rect = txt.get_rect(bottomright = (int(Leftx), int(Lefty)))
        screen.blit(L, L_rect)
        U = font.render("U", False, (255, 255, 0))
        U_rect = txt.get_rect(bottomright = (int(Upx), int(Upy)))
        screen.blit(U, U_rect)

    mouse_pos = pygame.mouse.get_pos()
    if tile1r.collidepoint((mouse_pos)):
        if pygame.mouse.get_pressed() == (1, 0, 0):
            utn = 1
            
    if utn == 1:
        if txt_rect.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["y1"] += 10
        elif U_rect.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["y1"] -= 10
        elif L_rect.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["x1"] -= 10
        elif R_rect.collidepoint((mouse_pos)):
            if pygame.mouse.get_pressed() == (1, 0, 0):
                data["x1"] += 10

    clock = pygame.time.Clock()
    pygame.display.flip()
    clock.tick(30)