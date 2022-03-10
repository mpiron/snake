# il faudra penser à appeler ce fichier main.py  par la suite.
import pygame
from game import Game
pygame.init()

# Nous générons la fenêtre de notre jeu
pygame.display.set_caption("Jeu de Graven")


# Initialisation des variables
# récupération de l'arrière plan

# Screen est une surface
screen = pygame.display.set_mode((1080, 720))
#  dans mon environnement, les liens se font à partir de E:\_Virtual_environment\python>
background = pygame.image.load('travail_Graven/assets/bg.jpg')
# charger notre jeu
game = Game()
# charger notre joueur (création d'une variable player)
# player=Player()


running = True
# boucle qui s'exécute tant que running est sur vrai
while running:
    # injection de l'image sur la surface avec la fonction blit (image + position)
    screen.blit(background, (0, -200))
    #recherche dans le dictionnaire game.pressed pour savoir si le joueur désire aller 
    #à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT):
        game.player.move_right()
    if game.pressed.get(pygame.K_LEFT):
        game.player.move_left()
    # On crée une instance de la classe player pour afficher notre joueur
    # Le second argument correspond à la position du joueur par rapport à la fenêtre
    screen.blit(game.player.image, game.player.rect)

    # mettre à jour l'écran avec la fonction flip du module pygame
    pygame.display.flip()
    # condition de sortie si le joueur ferme cette fenêtre

    # pour tous les événenment que je vais récupérer
    # dans la liste d'évenement de pygame
    for event in pygame.event.get():
        # Je vérifie que l'événement est la fermnetur de la fenêtre
        if event.type == pygame.QUIT:
            # on met la variable running sur faux pour sortir de la boucle
            # et on ferme le jeu
            running = False
            pygame.quit()
            # on ajoute un petit retour dans la console
            print("fermeture du jeu")
        # détecter si le joueur lâche une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key]=True
        elif event.type==pygame.KEYUP:
            game.pressed[event.key]=False
            # quelle touche a été utilisée
            # if event.key == pygame.K_RIGHT:
                # game.player.move_right()
            # elif event.key == pygame.K_LEFT:
                # game.player.move_left()
