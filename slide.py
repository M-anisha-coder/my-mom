#this module help us to create this slide show
import pygame
#from time module import sleep for this program
from time import sleep
#initialize pygame module
pygame.init()
#this syntax is use for display output in fill screen of window
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
# here we initialize the mixer function of pygame module
pygame.mixer.init()
#here we are load our music and play the music
pygame.mixer.music.load('mother.mp3')
pygame.mixer.music.play()
# then here we load our first img and it will appear in full window screen
image1 = pygame.image.load('images/img1.jpg')
window.blit(image1, (0, 0))
# this syntax tell us to update the next image after 5 sec
pygame.display.update()
sleep(5)
#now we are loading our second image and it will appear in full window screen
image3 = pygame.image.load('images/nobi1.jpg')
window.blit(image3, (0, 0))
# this syntax tell us to update the next image after 20 sec
pygame.display.update()
sleep(20)
#now we are loading our third image image and it will appear in full window screen
image4 = pygame.image.load('images/shin1.png')
window.blit(image4, (0, 0))
# this syntax tell us to update the next image after 20 sec
pygame.display.update()
sleep(20)
#now we are loading our fourth image and it will appear in full window screen
image5 = pygame.image.load('images/shin2.jpg')
window.blit(image5, (0, 0))
# this syntax tell us to update the next image after 20 sec
pygame.display.update()
sleep(20)
#now we are loading our fifth image and it will appear in full window screen
image5 = pygame.image.load('images/ash1.jpg')
window.blit(image5, (0, 0))
# this syntax tell us to update the next image after 20 sec
pygame.display.update()
sleep(20)


# similarly we can add also use multiple images and add song we love 
#this is very simple and easy project for python newbie
#GOOD LUCK GUYS WITH THIS LOVELY GIFT


