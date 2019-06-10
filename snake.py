#snake:
import pygame
import random

pygame.init()

def print(*a, **b):
    import builtins, sys
    builtins.print(*a, **b)
    sys.stdout.flush()

#setup
taille = [700, 500]
ecran = pygame.display.set_mode(taille)
clock = pygame.time.Clock()
rouge = [255,0,0]
blanc = [255,255,255]
bleu = [0,0,204]


# fruit : position


class Snake:
 import pygame
import random

pygame.init()

def print(*a, **b):
    import builtins, sys
    builtins.print(*a, **b)
    sys.stdout.flush()

#setup
taille = [700, 500]
ecran = pygame.display.set_mode(taille)
clock = pygame.time.Clock()
rouge = [255,0,0]
blanc = [255,255,255]
bleu = [0,0,204]


# fruit : position


class Snake:
    pass

class Food:
    pass

snake = Snake()  # Snake snake = new Snake();
snake.ma_position = 10
snake.ma_position2 = 20
snake.direction = 0
score = 0
food = Food()
food.x = random.randrange(700)
food.y = random.randrange(500)


liste_de_pommes_wesh = []
liste_de_pommes_wesh.append(food)

for i in range(2):
    food2 = Food()
    food2.x = random.randrange(700)
    food2.y = random.randrange(500)
    liste_de_pommes_wesh.append(food2)


font = pygame.font.SysFont('Calibri', 25)

s = 1

fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        if event.type == pygame.KEYDOWN:
            if event.key == 276:
                snake.direction = 2
            elif event.key == 275:
                snake.direction = 1
            elif event.key == 273:
                snake.direction = 4
            elif event.key == 274:
                snake.direction = 3  


    # tick
    if snake.direction == 1:
        snake.ma_position = snake.ma_position + 3
    elif snake.direction== 2:
        snake.ma_position = snake.ma_position - 3
    elif snake.direction == 3:
        snake.ma_position2 = snake.ma_position2 + 3
    elif snake.direction == 4:
        snake.ma_position2 = snake.ma_position2 - 3    


    if snake.ma_position > 700:
        fini = 1
        print("you lost")
        print("your score is", score)
    if snake.ma_position < 0:
        fini = 1
        print("you lost")
        print("your score is", score)        
    if snake.ma_position2 > 500:
        fini = 1
        print("you lost")
        print("your score is", score)
    if snake.ma_position2 < 0:
        fini = 1
        print("you lost")
        print("your score is", score)  

    #colisionq
    for f in liste_de_pommes_wesh:
        if snake.ma_position + 25 < f.x:
            touch = False
        elif snake.ma_position > f.x + 25:
            touch = False        
        elif snake.ma_position2 + 25 < f.y:
            touch = False
        elif snake.ma_position2 > f.y + 25:
            touch = False
        else:
            touch = True
        
        if touch == True:
            f.x = random.randrange(700)
            f.y = random.randrange(500)
            score = score + 1
            


    
    # dessin !
    image_score = font.render("Score: " + str(score), True, bleu)
    
    ecran.fill(blanc)
    pygame.draw.rect(ecran, rouge, [snake.ma_position, snake.ma_position2 , 25, 25])
    for f in liste_de_pommes_wesh:
        pygame.draw.rect(ecran, bleu, [f.x, f.y, 25, 25])
    ecran.blit(image_score, [20,20])
    pygame.display.flip()

    clock.tick(60)



pygame.quit()
