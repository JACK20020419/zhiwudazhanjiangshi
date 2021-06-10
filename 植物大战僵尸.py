import pygame
from pygame.locals import *
from sys import exit
import time
import Main_window
import Image
image=Image.Image()
pygame.mixer.init()
pygame.mixer.music.load('jspvz/main_aubio/begin_window.mp3')
pygame.mixer.music.set_volume(0.7)
buttonclick=pygame.mixer.Sound("jspvz/main_aubio/buttonclick.wav")
while True:
    window =Main_Window.Window()
    window.CreateWindow()
    if pygame.mixer.music.get_busy() ==False:
        pygame.mixer.music.play()
    for event in pygame.event.get():
        if event.type==QUIT:
            exit()
        if event.type==KEYDOWN:
            if event.key==k_f:
                window.PlayGame()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x1,y1=event.pos
            if 470<=x1<=800 and 96<=y1<=242:
                buttonclick.play()
                begin1 = pygame.image.load(image.PlayGame2).convert_alpha()
                window.pywindow.blit(beginl, (470,96))
                pygame.display.update()
                w, h=pygame.image.load(image.PlayGame).convert_alpha().ge
                time.sleep(0,5)
                if window.is_rect(event.pos,(470,100,w,))
                    pygame.mixer.music.stop()
                    window.PlayGame()
            if 800 <= x1 <=900 and 500 <= y1 <=550:
                if window. is_rect(event.pos,(800,50))
                exit()
                
