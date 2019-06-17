#snake :
import pygame
import random

pygame.init()

#for wing consol
def print(*a, **b):
    import builtins, sys
    builtins.print(*a, **b)
    sys.stdout.flush()

#setup
taille = [700, 500]
screen = pygame.display.set_mode(taille)
clock = pygame.time.Clock()
red = [255,0,0]
white = [255,255,255]
blue = [0,0,204]




class Snake:
    pass

class Food:
    pass

snake = Snake()  # Snake snake = new Snake();
snake.ma_position = 0
snake.ma_position2 = 0
snake.direction = 0
score = 0
food = Food()
food.x = random.randrange(700)
food.y = random.randrange(500)


apple_list = []
apple_list.append(food)

for i in range(2):
    food2 = Food()
    food2.x = random.randrange(675)
    food2.y = random.randrange(475)
    apple_list.append(food2)

list_snake = []
list_snake.append(snake)


for f in range(1):   #f = 0 1, 2, 3, 4
    snake2 = Snake()
    snake2.ma_position = f * 25   # = 0, 25, 50, 75, 100
    snake2.ma_position2 = 25
    list_snake.append(snake2)
    snake2.direction = 0
    print(len(list_snake))
    


font = pygame.font.SysFont('Calibri', 25)

s = 1

 #set up lost game
fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1


       #change direction if key is presst

        for serpent in list_snake:
            if event.type == pygame.KEYDOWN:
                if event.key == 276:
                    serpent.direction = 2
                elif event.key == 275:
                    serpent.direction = 1
                elif event.key == 273:
                    serpent.direction = 4
                elif event.key == 274:
                    serpent.direction = 3  
                

 # tick
    # make the snake move
    for serpent in list_snake:
        if serpent.direction == 1:
            serpent.ma_position = snake.ma_position + 3
        elif serpent.direction== 2:
            serpent.ma_position = snake.ma_position - 3
        elif serpent.direction == 3:
            serpent.ma_position2 = snake.ma_position2 + 3
        elif serpent.direction == 4:
            serpent.ma_position2 = snake.ma_position2 - 3    


# game lost
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

   
    #colisions
    for f in apple_list:
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
                

 # draw !
    

    #score set up
    image_score = font.render("Score: " + str(score), True, blue)
    

    screen.fill(white)
    
    #snake draw
    for serpent in list_snake:
        pygame.draw.rect(screen, red, [serpent.ma_position,
                                        serpent.ma_position2, 25, 25])
    #food draw
    for f in apple_list:
        pygame.draw.rect(screen, blue, [f.x, f.y, 25, 25])
   
    #score draw
    screen.blit(image_score, [20,20])
    pygame.display.flip()

    clock.tick(60)


pygame.quit()
