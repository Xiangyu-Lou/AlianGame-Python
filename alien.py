import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ control the alien """
    def __init__(self, ai_game):
        """ init the alien settings and position """
        super().__init__()
        self.screen = ai_game.screen
        
        # load the alien image and setting the rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        # move the alien position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # save the positon of the alien
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        self.settings = ai_game.settings
        
    def update(self):
        """ move the alien fleet """
        if self.check_edages() == False:
            self.settings.fleet_direction = -1
        self.x += (self.settings.alien_speed_x * self.settings.fleet_direction)
        self.rect.x = self.x
    
    def check_edages(self):
        """ detect wheter the alien touch edge of the screen """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        else :
            return False