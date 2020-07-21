import pygame
import random
import time
import Window
from Player import Player
from Monster import Monster
from Meteorite import Meteorite


class Game:

    def __init__(self):
        #definir si notre jeu a commencé
        self.isPlaying = False
        #generer un joueur
        self.all_players =pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #group de monstres
        self.all_monsters = pygame.sprite.Group()
        #initialisation du dico de touches qui seront pressées
        self.pressed = {}
        self.all_meteorites = pygame.sprite.Group()

    def start (self):
        self.isPlaying = True
        # ajouter un timer pour declencher l'avalanche
        for i in range(random.randint(10, 40)):
            self.avalanche_meteorites()
        # ajout entre 1 et 9 monstres
        for i in range(random.randint(1, 5)):
            self.spawn_monster()
        print(2 , time.clock())

    def game_over(self):

        self.all_monsters= pygame.sprite.Group()
        self.all_meteorites =pygame.sprite.Group()
        self.player.health=self.player.health_max
        # intialiser le nom du joueur dans une base de données:

        Window.MEP_Interface_Classement(self.player.score)
        print(self.player.score)
        self.isPlaying = False

    def avalanche_meteorites(self):
        meteorite = Meteorite(self)
        self.all_meteorites.add(meteorite)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)

    def check_collision(self,sprite,group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)

    def update(self,screen):
        # appliquer le joueur
        screen.blit(self.player.image, self.player.rect)

        # appliquer la barre du joueur:
        self.player.update_health_bar(screen)

        #declenchement des meteorites:
        for meteorite in self.all_meteorites:
            meteorite.move_damage()

        self.all_meteorites.draw(screen)

        # deplacement des projectiles
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recuperer les monstres du jeu:
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
        # appliquer les images des monstres
        self.all_monsters.draw(screen)
        # appliquer les images du projectile
        self.player.all_projectiles.draw(screen)

        # verifier les commandes utilisées
        if self.pressed.get(
                pygame.K_RIGHT) and self.player.rect.x <= screen.get_width() - self.player.image.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()