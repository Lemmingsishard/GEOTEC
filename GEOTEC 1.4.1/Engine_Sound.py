"""This is where sound functionality in the engine comes from."""
import pygame

#when writing this, I noticed I section my code like x86 asm with data then code, but then I realised, that is prtty much the only way to write code :|

pygame.init()
pygame.mixer.init()
loaded = False
playing = False
loaded2 = False
playing2 = False

class GeoPlayer:
    def __init__(self, titular, Enabled, song = None):
        if song != None:
            if Enabled == True:
                global loaded
                global playing
                if titular == False:
                    if loaded == False:
                        pygame.mixer.music.load(song)
                        loaded = True
                    if playing == False:
                        pygame.mixer.music.play(-1)
                        playing = True
                else:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    loaded = False
                    playing = False
            else:
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                loaded = False
                playing = False

class TitlePlayer:
    def __init__(self, titular, Enabled, song = None):
        if song != None:
            if Enabled == True:
                global loaded2
                global playing2
                global loaded
                global playing
                if titular == True:
                    if loaded or playing == True:
                        pygame.mixer.music.stop()
                        pygame.mixer.music.unload()
                        loaded = False
                        playing = False
                        pygame.mixer.music.load(song)
                        loaded2 = True
                        pygame.mixer.music.play(-1)
                        playing2 = True
                    if loaded2 == False:
                        pygame.mixer.music.load(song)
                        loaded2 = True
                    if playing2 == False:
                        pygame.mixer.music.play(-1)
                        playing2 = True
                else:
                    pygame.mixer.music.stop()
                    pygame.mixer.music.unload()
                    loaded2 = False
                    playing2 = False
            else:
                pygame.mixer.music.stop()
                pygame.mixer.music.unload()
                loaded2 = False
                playing2 = False
