import pygame
from Game import *
from Player import *
import math


pygame.init()

# generer la fenetre du jeux
pygame.display.set_caption("Jeux Geo")
screen = pygame.display.set_mode((1080, 720))


#image arriere plane
background = pygame.image.load('assets/bg.jpg')

#charger notre banniere
banner = pygame.image.load('assets/Pokemon.png')
banner = pygame.transform.scale(banner,(450,250))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() /3.5)
banner_rect.y = math.ceil(screen.get_height() /6)

#charger le bouton
button = pygame.image.load('assets/button.png')
button = pygame.transform.scale(button,(400,150))
button_rect = button.get_rect()
button_rect.x = math.ceil(screen.get_width() /3.33)
button_rect.y = math.ceil(screen.get_height() /2)
#charger un joueur
game = Game()

running = True

while running:

    #appliquer arriere plan
    screen.blit(background, (0,-200))

    #verifier si le jeu a commencé:
    if game.isPlaying:
        game.update(screen)
    # verifier si notre jeu n'a pas commencé:
    else:
        # appliquer arriere plan
        screen.blit(button, button_rect)
        screen.blit(banner, banner_rect)

    #mettre à jour l'ecran
    pygame.display.flip()

    for event in pygame.event.get():
        # si la fenetre est fermée:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("fermeture du jeux")
        #si un joueur appuie sur une touche du clavier:
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche " " est enclenché:
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        #si le joueur relache la touche
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                game.start()

