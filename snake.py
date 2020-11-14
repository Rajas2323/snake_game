import pygame
import random
pygame.init()


def game_over():

    blue = (0, 0, 255)
    X = 800
    Y = 700
    RUN = False

    while not RUN:
        window1 = pygame.display.set_mode((X, Y))
        pygame.display.set_caption("Game Over!")

        font = pygame.font.Font("freesansbold.ttf", 40)
        text = font.render("Game Over! Press Enter to play Again", True, blue)
        text_rect = text.get_rect()
        text_rect.center = (X // 2, Y//2)

        window1.blit(text, text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    RUN = True
                    gameloop()

        pygame.display.update()




def gameloop():
    def plot_snake(gamewindow, color, snk_list, size):

        for x, y in snk_list:
            pygame.draw.rect(window, red, [x, y, snake_width, snake_height])

    # Colors
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    black = (0, 0, 0)

    # In-Game Variables
    clock = pygame.time.Clock()
    screen_width = 800
    screen_height = 700
    snake_x = screen_width / 2
    snake_y = screen_height / 2
    snake_width = 20
    snake_height = 20
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(20, screen_height - 20)
    fps = 240
    snk_list = []
    snk_length = 1
    # In-Game Variables

    # Main Window
    window = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Jai Shri Krishna")

    exit_game = False

    while not exit_game:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    velocity_x = 1
                    velocity_y = 0

                if event.key == pygame.K_LEFT:
                    velocity_x = -1
                    velocity_y = 0

                if event.key == pygame.K_UP:
                    velocity_y = -1
                    velocity_x = 0

                if event.key == pygame.K_DOWN:
                    velocity_y = 1
                    velocity_x = 0


        if abs(snake_x - food_x) <= 16 and abs(snake_y - food_y) <= 16:
            food_x = random.randint(20, screen_width - 20)
            food_y = random.randint(20, screen_height - 20)
            snk_length += 20


        snake_x = snake_x + velocity_x
        snake_y = snake_y + velocity_y


        head = []
        head.append(snake_x)
        head.append(snake_y)
        snk_list.append(head)



        if len(snk_list) > snk_length:
            del snk_list[0]


        if snake_x < 0 or snake_x > screen_width or snake_y < 0 or snake_y > screen_height:
            print("Game Over")
            pygame.display.quit()
            game_over()

        if head in snk_list[:-1]:
            exit_game = True
            game_over()

        clock.tick(fps)
        window.fill(black)
        #pygame.draw.rect(window, red, [snake_x, snake_y, snake_width, snake_height])
        plot_snake(window, red, snk_list, snake_width)


        pygame.draw.rect(window, yellow, (food_x, food_y, snake_width, snake_height))
        pygame.display.update()

gameloop()
