import pygame, sys
from PIL import Image
from pygame import mouse

from pygame.constants import K_ESCAPE, K_SPACE, KEYDOWN, MOUSEBUTTONDOWN, MOUSEBUTTONUP, QUIT

def main():

    green = (0, 255, 0)
    blue = (0, 0, 128)

    clock = pygame.time.Clock()
    pygame.init()
    WINDOW_SIZE = (600,800)
    pygame.display.set_caption('Projectile Launcher')

    font = pygame.font.Font('freesansbold.ttf', 20)
    score = 0
    text = font.render('Score: ' + str(score), True, green, blue)

    display = pygame.display.set_mode(WINDOW_SIZE)
    player_image = pygame.image.load('testing.png')
    enemy_image = pygame.image.load('blocks.png')
    enemy_image_2 = pygame.image.load('blocks.png')

    starting_location = [280, 700]
    ball_location = starting_location

    enemy1_start = [100,180]
    enemy2_start = [460,120]
    enemy_location = [100, 180]
    enemy_location_2 = [460, 120]
    ball_dx = 0
    ball_dy = 0
    e1_life = True
    e2_life = True
    rect_color = (255,0,0)
    enemy1_dx = 30
    enemy2_dx = 30


    begin = 0
    movement = False
    Power = 0

    power_font = pygame.font.Font('freesansbold.ttf', 15)

    while True:
        
        #End Screen
        if score == 2:
            begin = 2
            display.fill((146,244,255))
            font = pygame.font.Font('freesansbold.ttf', 40)
            text = font.render('CONGRATULATIONS', True, green, blue)
            display.blit(text, (100,400))
            text = font.render('Space to continue', True, green, blue)
            display.blit(text, (100,450))
            text = font.render('Escape to exit', True, green, blue)
            display.blit(text, (100, 500))
            pygame.display.update()
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        begin = 1
                        Power = 0
                        score = 0
                        e1_life = True
                        e2_life = True
                        enemy_location = enemy1_start
                        enemy_location_2 = enemy2_start
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
        
        #Game Loop
        if begin == 1:

            display.fill((146,244,255))
            pygame.draw.rect(display, rect_color, pygame.Rect(0,1,600, 10))
            display.blit(player_image, ball_location)
            
            power = power_font.render('Power ' + str(Power) + '%', True, (255,0,0), blue)
            display.blit(power, (10, 750))

            text = font.render('Score: ' + str(score), True, green, blue)
            display.blit(text, (10,20))

            enemy_location[0] += enemy1_dx * 0.10
            enemy_location_2[0] -= enemy2_dx * 0.10

            if enemy_location[0] > WINDOW_SIZE[0] - 50 or enemy_location[0] < 0:
                enemy1_dx *= -1
            if enemy_location_2[0] > WINDOW_SIZE[0] - 50 or enemy_location_2[0] < 0:
                enemy2_dx *= -1

            if e1_life:
                display.blit(enemy_image, enemy_location)
            if e2_life:
                display.blit(enemy_image_2, enemy_location_2)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                if event.type == MOUSEBUTTONUP:
                    next_x, next_y = pygame.mouse.get_pos()
                    ball_dx = x - next_x
                    ball_dy = y - next_y
                    Power = ball_dx + ball_dy
                    movement = True
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        print('dy: ',ball_dy)
                        print('dx: ',ball_dx)
                        print('ball location: ', ball_location[0], ball_location[1])

            if movement == True:
                ball_location[0] += ball_dx * 0.10
                ball_location[1] += ball_dy * 0.10

                if (ball_location[0] < enemy_location[0] + 40 and ball_location[0] > enemy_location[0]) or (ball_location[0] + 40 > enemy_location[0] + 10 and ball_location[0] + 40 < enemy_location[0] + 40):
                    if (ball_location[1] < enemy_location[1] + 40 and ball_location[1] > enemy_location[1]) or (ball_location[1] + 40 > enemy_location[1]+10 and ball_location[1] + 40 < enemy_location[1] + 40):
                        e1_life = False
                        enemy_location = [0,800]
                        ball_location = [280,700]
                        ball_dx = 0
                        ball_dy = 0
                        score += 1
                
                if (ball_location[0] < enemy_location_2[0] + 40 and ball_location[0] > enemy_location_2[0]) or (ball_location[0] + 40 > enemy_location_2[0] + 10 and ball_location[0] + 40 < enemy_location_2[0] + 40):
                    if (ball_location[1] < enemy_location_2[1] + 40 and ball_location[1] > enemy_location_2[1]) or (ball_location[1] + 40 > enemy_location_2[1]+10 and ball_location[1] + 40 < enemy_location_2[1] + 40):
                        e2_life = False
                        ball_location = [280,700]
                        enemy_location_2 = [0,800]
                        ball_dx = 0
                        ball_dy = 0
                        score += 1

                if ball_location[0] > (WINDOW_SIZE[0] - 40) or ball_location[0] < 0:
                    ball_dx *= -1

                if ball_location[1] > (WINDOW_SIZE[1] - 40):
                    ball_dy *= -1

                if ball_location[1] < 0:
                    ball_location = [280,700]
                    ball_dx = 0
                    ball_dy = 0
                    movement = False

            pygame.display.update()
            clock.tick(60)

        #begin screen
        elif begin == 0:
            display.fill((146,244,255))
            font = pygame.font.Font('freesansbold.ttf', 40)
            text_1 = font.render('WELCOME', True, blue, green)
            text_2 = font.render('TO', True, blue, green)
            text_3 = font.render('MY GAME', True, blue, green)
            display.blit(text_1, (100,100))
            display.blit(text_2, (100,140))
            display.blit(text_3, (100,180))

            font = pygame.font.Font('freesansbold.ttf', 30)
            play = font.render('Press Space To Start', True, green, blue)
            display.blit(play, (160, 450))

            pygame.display.update()
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        begin = True

        
main()


