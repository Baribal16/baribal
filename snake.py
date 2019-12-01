# snake :
import pygame
import random

pygame.init()


# for wing consol
def print(*a, **b):
    import builtins, sys
    builtins.print(*a, **b)
    sys.stdout.flush()


# setup
taille = [700, 500]
screen = pygame.display.set_mode(taille)
clock = pygame.time.Clock()
red = [255, 0, 0]
white = [255, 255, 255]
blue = [0, 0, 204]


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
food.x = random.randrange(650)
food.y = random.randrange(450)

apple_list = []
apple_list.append(food)

for i in range(2):
    food2 = Food()
    food2.x = random.randrange(650)
    food2.y = random.randrange(450)
    apple_list.append(food2)

list_snake = []
list_snake.append(snake)

for f in range(1):  # f = 0 1, 2, 3, 4
    snake2 = Snake()
    snake2.ma_position = 25
    snake2.ma_position2 = f * 25 # = 0, 25, 50, 75, 100
    list_snake.append(snake2)
    snake2.direction = 0

print("len", len(list_snake))
print("comm", snake.ma_position, snake.ma_position2, list_snake[1].ma_position, list_snake[1].ma_position)

font = pygame.font.SysFont('Calibri', 25)

s = 1
compteur = 0

# set up lost game
fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1

        # change direction if key is presst

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
    # make the snake move

    compteur += 1
    if compteur == 10:
        compteur = 0

        #print("avant", snake.ma_position, snake.ma_position2, list_snake[1].ma_position, list_snake[1].ma_position)
        if snake.direction != 0:
            i = len(list_snake) - 1
            while i > 0:
                list_snake[i].ma_position = list_snake[i-1].ma_position
                list_snake[i].ma_position2 = list_snake[i-1].ma_position2
                i = i - 1

        #print("d", snake.direction)
        #print("apres", snake.ma_position, snake.ma_position2, list_snake[1].ma_position, list_snake[1].ma_position)
        if snake.direction == 1:
            snake.ma_position = snake.ma_position + 25
        elif snake.direction == 2:
            snake.ma_position = snake.ma_position - 25
        elif snake.direction == 3:
            snake.ma_position2 = snake.ma_position2 + 25
        elif snake.direction == 4:
            snake.ma_position2 = snake.ma_position2 - 25
        #print(snake.ma_position, snake.ma_position2, list_snake[1].ma_position, list_snake[1].ma_position)

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

    for serpent in list_snake[1:]:
        if snake.ma_position == serpent.ma_position and snake.ma_position2 == serpent.ma_position2:
            fini = 1
            print("you losty")
            print("your score is", score)


        # colisions
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
            #print("touch")
            snake3 = Snake()
            snake3.ma_position = list_snake[len(list_snake) - 1].ma_position
            snake3.ma_position2 = list_snake[len(list_snake) - 1].ma_position2

            f.x = random.randrange(670)
            f.y = random.randrange(470)
            score = score + 1
            list_snake.append(snake3)

    # draw !

    # score set up
    image_score = font.render("Score: " + str(score), True, blue)

    screen.fill(white)

    # snake draw
    for serpent in list_snake:
        pygame.draw.rect(screen, red, [serpent.ma_position,
                                       serpent.ma_position2, 25, 25])
    # food draw
    for f in apple_list:
        pygame.draw.rect(screen, blue, [f.x, f.y, 25, 25])

    # score draw
    screen.blit(image_score, [20, 20])
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
