import pygame

#classe qui herite de la classe sprite
# qui gere le projectile du joueur

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player=player
        self.image = pygame.image.load('assets/projectile.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect.x = player.rect.x +120
        self.rect.y = player.rect.y + 80
        self.rect.center = self.rect.center
        self.origin_image =self.image
        self.angle=0

    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        #print (self.rect, self.image.get_rect(center=self.rect.center))

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        # si le projectile rentre en collision avec monstre:
        for monster in  self.player.game.check_collision(self, self.player.game.all_monsters):
            #supprimer le projectile
            self.remove()
            #infliger degats
            monster.damage(self.player.attack)

        #verifier si le projectile n'est plus dans l'ecran
        if self.rect.x>1080:
            self.remove()
