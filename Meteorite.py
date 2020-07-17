import pygame
import random

class Meteorite(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.velocity = random.randint(1, 3)
        self.attack = 5
        self.image = pygame.image.load('assets/comet.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1, 1080)
        self.rect.y = 0

    def move_damage(self):
        # si le monstre n'est pas en collision avec le joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.y += self.velocity
        else:
            # infliger degats au player:
            self.game.player.damage(self.attack)
            self.remove()
        if self.rect.y ==720:
            #reapparition:
            self.rect.y = 0
            self.rect.x = random.randint(1, 1080)
            self.velocity = random.randint(1, 3)

    def remove(self):
        self.game.all_meteorites.remove(self)