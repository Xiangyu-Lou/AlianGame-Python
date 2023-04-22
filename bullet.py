import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ manage the bullets fired from the ship """
    
    def __init__(self, ai_game):
        """ creat a bullet at the position of the ship """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.fire_signal = False
        
        # creat a bullet at (0, 0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        # bullet position is a float value
        self.y = float(self.rect.y)
    
    def update(self):
        """ move the bullet up the screen """
        # update the float value of the bullet
        self.y -= self.settings.bullet_speed
        # update the rect position
        self.rect.y = self.y
    
    def draw_bullet(self):
        # draw bullet on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)