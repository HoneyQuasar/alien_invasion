import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion():
    """A class for managing resources and game behavior"""
    def __init__(self):
        """Inizialization game and create games resources"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self.screen)

    def run_game(self):
        """Launch main cycle game"""
        while True:
            # keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Display the last drawn screen
            pygame.display.flip()

if __name__ == '__main__':
    # Create exemple and launch game
    ai = AlienInvasion()
    ai.run_game()