#snake:
import pygame
import random

pygame.init()

#setup
taille = [700, 500]
ecran = pygame.display.set_mode(taille)
clock = pygame.time.Clock()
rouge = [255,0,0]
blanc = [255,255,255]
bleu = [0,0,204]


# fruit : position
x = random.randrange(700)
y = random.randrange(500)


ma_position = 10
ma_position2 = 20
direction = 0

fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1


        if ma_position > 600:
            fini = 1
        if ma_position2 > 500:
            fini = 1
       

        #good work but need more work
        if (ma_position == x or ma_position == x + 7 or ma_position == x - 7 and ma_position2 == y or ma_position2 == y + 7 or ma_position2 == y - 7):
            x = random.randrange(700)
            y = random.randrange(500)

        if event.type == pygame.KEYDOWN:
            if event.key == 276:
                direction = 2
            elif event.key == 275:
                direction = 1
            elif event.key == 273:
                direction = 4
            elif event.key == 274:
                direction = 3



    # tick
    if direction == 1:
        ma_position = ma_position + 3
    elif direction== 2:
        ma_position = ma_position - 3
    elif direction == 3:
        ma_position2 = ma_position2 + 3
    elif direction == 4:
        ma_position2 = ma_position2 - 3
    # dessin
    ecran.fill(blanc)
    pygame.draw.rect(ecran, rouge, [ma_position, ma_position2 , 25, 25])
    pygame.draw.rect(ecran, bleu, [x, y, 25, 25])
    pygame.display.flip()

    clock.tick(60)



pygame.quit()
