from random import randint
#base
a = ["pierre", "papier", "ciseaux" ]
#set play for computer
ordi = a[randint(0,2)]

import pygame, sys


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

player = ""
clock = pygame.time.Clock()

fini = 0
while fini == 0:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("hello", event.pos[0], event.pos[1])

            mouseposition = event.pos
            if mouseposition[0] >= 175 and mouseposition[0] <= 375 and mouseposition[1] >= 500 and mouseposition[1] <= 700:
                player = "pierre"
                print("pierre")

            if mouseposition[0] >= 400 and mouseposition[0] <= 600 and mouseposition[1] >= 500 and mouseposition[1] <= 700:
                player = "ciseaux"
                print("ciseaux")

            if mouseposition[0] >= 625 and mouseposition[0] <= 825 and mouseposition[1] >= 500 and mouseposition[1] <= 700:
                player = "papier"
                print("papier")

            if player != "":
                print("ordi", ordi)

                if player == ordi:
                    print("tie")

                elif player  == "pierre":
                    if ordi == "papier":
                        print("you lost")
                    else:
                        print ("you won")

                elif player == "papier":
                    if ordi == "ciseaux":
                        print("you lost")
                    else:
                        print("you won")

                elif player == "ciseaux":
                    if ordi == "pierre":
                        print("you lost")
                    else:
                        print("you won")




    # TICK

    # DESSIN
    ecran.fill(BLANC)

    ecran.blit(image_papier_petite, [625, 500])
    ecran.blit(image_ciseaux_petite, [400, 500])
    ecran.blit(image_pierre_petite, [175, 500])

    pygame.display.flip()
    #sys.stdout.flush()

    clock.tick(60)

pygame.quit()
