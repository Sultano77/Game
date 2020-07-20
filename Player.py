import pygame
from Projectile import Projectile

class Player(pygame.sprite.Sprite):
    #sprite element du jeux pour se deplacer par ex
    def __init__(self,game):
        super().__init__()
        self.game =game
        self.health = 100
        self.health_max = 100
        self.attack = 10
        self.velocity = 5
        self.score = 0
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/Pikatchu.png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 550

    def damage (self,amount):
        #infliger degats:
        self.health -= amount
        if self.health<=0 :
            #fin de partie
            self.game.game_over()


    def update_health_bar(self, surface):

        #dessiner barre de vie + la barre max
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.health_max, 5])
        pygame.draw.rect(surface,(111,210,46),[self.rect.x+50, self.rect.y+20, self.health, 5])


    def launch_projectile(self):
        #creer une instance de projectile
        self.all_projectiles.add(Projectile(self))


    def move_right(self):
        #si le joueur n'est pas en collision avec le monstre
        if not self.game.check_collision(self,self.game.all_monsters):
            self.rect.x += self.velocity


    def move_left(self):
        self.rect.x -= self.velocity