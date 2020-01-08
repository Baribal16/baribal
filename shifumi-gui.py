from random import randint

# base
a = ["pierre", "papier", "ciseaux"]
# set play for computer
ordi = a[randint(0, 2)]

import pygame, sys

pygame.init()

taille = [1000, 800]
ecran = pygame.display.set_mode(taille)

NOIR = [0, 0, 0]
BLANC = [255, 255, 255]
ROUGE = [255, 0, 0]
VERT = [0, 255, 0]
BLEU = [0, 0, 255]

font = pygame.font.SysFont('Calibri', 90)
font2 = pygame.font.SysFont('Calibri', 20)
# DÉBUT
image_pierre = pygame.image.load('pierre.jpg').convert_alpha()
image_ciseaux = pygame.image.load('ciseaux.jpg').convert_alpha()
image_papier = pygame.image.load('papier.png').convert_alpha()

image_pierre_petite = pygame.transform.smoothscale(image_pierre, [200, 200])
image_ciseaux_petite = pygame.transform.smoothscale(image_ciseaux, [200, 200])
image_papier_petite = pygame.transform.smoothscale(image_papier, [200, 200])

score = 0
score_ordi = 0
player = ""
clock = pygame.time.Clock()

resultat = ""
fini = 0
while fini == 0:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("hello", event.pos[0], event.pos[1])

            if player == "":

                mouseposition = event.pos
                if 175 <= mouseposition[0] <= 375 and 500 <= mouseposition[1] <= 700:
                    player = "pierre"
                    print("pierre")

                if 400 <= mouseposition[0] <= 600 and 500 <= mouseposition[1] <= 700:
                    player = "ciseaux"
                    print("ciseaux")

                if 625 <= mouseposition[0] <= 825 and 500 <= mouseposition[1] <= 700:
                    player = "papier"
                    print("papier")

                if player != "":
                    print("ordi", ordi)

                    if player == ordi:
                        print("tie")
                        resultat = "tie"
                        # ordi = a[randint(0, 2)]

                    elif player == "pierre":
                        if ordi == "papier":
                            print("you lost")
                            resultat = "lost"
                            # ordi = a[randint(0, 2)]

                        else:
                            print("you won")
                            resultat = "won"
                            #ordi = a[randint(0, 2)]

                    elif player == "papier":
                        if ordi == "ciseaux":
                            print("you lost")
                            resultat = "lost"
                            #ordi = a[randint(0, 2)]

                        else:
                            print("you won")
                            resultat = "won"
                            #ordi = a[randint(0, 2)]

                    elif player == "ciseaux":
                        if ordi == "pierre":
                            print("you lost")
                            resultat = "lost"
                            #ordi = a[randint(0, 2)]

                        else:
                            print("you won")
                            resultat = "won"
                    if resultat == "won":
                        score = score + 1
                    elif resultat == "lost":
                        score_ordi = score_ordi + 1
                    elif resultat == "tie":
                        ...


            else:
                player = ""
                ordi = a[randint(0, 2)]


    # TICK

    # DESSIN
    ecran.fill(BLANC)

    ecran.blit(image_papier_petite, [625, 500])
    ecran.blit(image_ciseaux_petite, [400, 500])
    ecran.blit(image_pierre_petite, [175, 500])

    image_score2 = font2.render("your score " + str(score), True, NOIR)
    image_score3 = font2.render("computer score " + str(score_ordi), True, NOIR)
    ecran.blit(image_score2, [20, 20])
    ecran.blit(image_score3, [850, 20])
    if player == "":
        ...
    else:

        if ordi == "papier":
            ecran.blit(image_papier_petite, [400, 100])
        elif ordi == "ciseaux":
            ecran.blit(image_ciseaux_petite, [400, 100])
        elif ordi == "pierre":
            ecran.blit(image_pierre_petite, [400, 100])

        image_score = font.render("you " + str(resultat), True, NOIR)
        ecran.blit(image_score, [500-image_score.get_width()/2, 350])


    pygame.display.flip()
    # sys.stdout.flush()

    clock.tick(60)

pygame.quit()
