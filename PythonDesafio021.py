#Faça um programa em python que abra e reproduza o audio de um arquivo mp3

import pygame

pygame.init()
pygame.mixer.music.load("ex021.mp3") #o audio tera que estar na mesma pasta desse arquivo python
pygame.mixer.music.play()
input()
pygame.event.wait()
