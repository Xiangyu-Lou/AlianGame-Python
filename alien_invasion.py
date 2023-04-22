import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """管理游戏资源和行为的类 """
    
    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()
        self.settings = Settings()
        
        # window play
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        # full screen play
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        
        pygame.display.set_caption("星球大战")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
        # creat a clock and set the fps to 240
        self.clock = pygame.time.Clock()
        self.fps = 240
        
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self.clock.tick(self.fps)
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            
    def _check_events(self):
        """ 响应按键和鼠标事件 """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # ship moving
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                self._check_quit(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    # keydown events          
    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_SPACE:
            self.bullets.fire_signal = True
            self._fire_bullet()
            
    # keyup events
    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
            
    def _check_quit(self,event):
        """ quit the game """
        if event.key == pygame.K_ESCAPE:
            sys.exit()
            
    def _fire_bullet(self):
        """ creat a bullet and add it to the bullets group """
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
            
    def _update_screen(self):
        """ screen update """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()
                
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()