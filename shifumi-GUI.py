from random import randint
#base
a = ["pierre", "papier", "ciseaux" ]
#set play for computer
ordi = a[randint(0,2)]

import pygame

pygame.init()

taille = [1000, 800]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

# DÉBUT
image_pierre = pygame.image.load('pierre.jpg').convert_alpha()
image_ciseaux = pygame.image.load('ciseaux.jpg').convert_alpha()
image_papier = pygame.image.load('papier.png').convert_alpha()


image_pierre_petite = pygame.transform.smoothscale(image_pierre, [200,200])
image_ciseaux_petite = pygame.transform.smoothscale(image_ciseaux, [200,200])
image_papier_petite = pygame.transform.smoothscale(image_papier, [200,200])


print("Taille pierre :", image_pierre.get_width(), image_pierre.get_height())
print("Taille ciceau:", image_ciseaux.get_width(), image_ciseaux.get_height())
print("Taille papier :", image_papier.get_width(), image_papier.get_height())

clock = pygame.time.Clock()

fini = 0
while fini == 0:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1

    # TICK

    # DESSIN
    ecran.fill(BLANC)

    ecran.blit(image_papier_petite, [600, 200])
    ecran.blit(image_ciseaux_petite, [400, 200])
    ecran.blit(image_pierre_petite, [200, 200])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
