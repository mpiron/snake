
import pygame

# Création d'une première classe qui va représenter notre joueur
# Il faut également que cette classe corresponde à un sprite sur notre jeu
# un sprite étant un élément graphique qui peut se déplacer.
# Pour ce faire il faut lui faire hériter () de la superclasse pygame.sprite.Sprite
# Ces sprite peuvent se faire assigner une image et une position (rect)
class Player(pygame.sprite.Sprite):
    # On va définir la méthode Init
    # Méthode init = constructeur de la classe
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        self.image = pygame.image.load('travail_Graven/assets/player.png')
        # récupération des coordonnées de l'image
        self.rect = self.image.get_rect()
        self.rect.x=300
        self.rect.y= 500

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -=self.velocity