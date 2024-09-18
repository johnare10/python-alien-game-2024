import sys
from settings import Settings
from ship import Ship

import pygame

class AlienInvasion:
    """Class that will handle the game assets and behaviors"""
    def __init__(self):
        """Initialize the game and create the game resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
    

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        
        # Create the ship
        self.ship = Ship(self)


    def run_game(self):
        """Start main loop for game"""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Responds to keypress etc"""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit
    
    def _update_screen(self):

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
         

if __name__ == '__main__':
    # Make a  game instance, and run the game.

    ai = AlienInvasion()
    ai.run_game()