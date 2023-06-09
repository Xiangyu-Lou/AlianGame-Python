import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_status import GameStatus


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
        # bullets
        self.bullets = pygame.sprite.Group()
        # aliens
        self.aliens = pygame.sprite.Group()
        self._creat_fleet()
        
        # creat a clock
        self.clock = pygame.time.Clock()
        self.fps = self.settings.fps
        
    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self.clock.tick(self.fps)
            self._check_events()
            self.ship.update()
            self._update_screen()
            self._update_bulletes()
            self._update_aliens()
            
    def _update_screen(self):
        """ screen update """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites(): 
            bullet.draw_bullet()
        pygame.display.flip()
            
    def _update_aliens(self):
        """ update the alien position """
        self.aliens.update()
        
    def _creat_fleet(self):
        # calaulate the number of alien in a row
        aliens = Alien(self)
        number_aliens_x = int((self.settings.screen_width - (2 * aliens.rect.width))/aliens.rect.width)
        # calaulate the number of alien in a column
        number_aliens_y = 2
        
        # creat the alien fleet
        for alien_number_y in range(number_aliens_y):
            for alien_number_x in range(number_aliens_x):
                self._creat_alien(alien_number_y,alien_number_x)
                
    def _creat_alien(self,alien_number_y,alien_number_x):
        """ creat an alien """
        alien = Alien(self)
        alien_width = alien.rect.width
        alien_height = alien.rect.height
        alien.y = alien_height + 2 * alien_height * alien_number_y
        alien.x = alien_width + 2 * alien_width * alien_number_x
        alien.rect.y = alien.y
        alien.rect.x = alien.x
        self.aliens.add(alien)
            
    def generate_alien(self):
        """ generate the alien """
        alien = Alien(self)
        self.aliens.add(alien)
            
    def _update_bulletes(self):
        """ update the bullets """
        self.bullets.update()        
        # delete the bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
                
        # detect whether the bullet hit the alien
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
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
             
    def _check_keydown_events(self, event):
        """ keydown events """
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
            
    def _check_keyup_events(self, event):
        """ keyup events """
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
                
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()