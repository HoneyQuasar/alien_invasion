import pygame

class Ship():
    """Class for control ship"""
    def __init__(self, ai_game):
        """initialization ship and sets its initial position"""
        self.screen = ai_game
        self.screen_rect = ai_game.get_rect()
        #Load image ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        #Each new ship appears at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship in current position"""
        self.screen.blit(self.image, self.rect)