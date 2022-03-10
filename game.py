import pygame
from player import Player

# Création d'un classe (2e création)
# représentant notre jeu
class Game:
    def __init__(self):
        #générer notre joueur
        self.player = Player()
        self.pressed = { }
