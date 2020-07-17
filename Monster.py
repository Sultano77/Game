import pygame
import random

#notion de monstre sur le jeux
class Monster(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100
        self.health_max = 100
        self.attack = 5
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = 1000 +random.randint(0,300)
        self.rect.y = 540

    def damage (self,amount):
        #infliger degats:
        self.health -= amount
        if self.health<=0 :
            #supprimer le monstre + ajoute un score
            #reapparaitre comme au debut
            self.game.player.score += 5
            self.rect.x=1000 +random.randint(0,300)
            self.health=self.health_max
            self.velocity = random.randint(1, 3)



    def update_health_bar(self, surface):

        #dessiner barre de vie + la barre max
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 10, self.health_max, 5])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x+10, self.rect.y-10, self.health, 5])


    def forward(self):
        # si le monstre n'est pas en collision avec le joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            #infliger degats:
            self.game.player.damage(self.attack)