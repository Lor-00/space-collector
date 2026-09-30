import pygame
import random


pygame.init()

game_window = pygame.display.set_mode((700, 600))
pygame.display.set_caption("Space Colletor")

spaceship_image = pygame.image.load("spaceship.png").convert_alpha()
spaceship_image = pygame.transform.scale(spaceship_image,(80,80))

spaceship_x = 400
spaceship_y = 350
spaceship_speed = 10

star_x = random.randint(20, 680)
star_y = random.randint(20, 580)
star_size = 20

blackhole_x = 650
blackhole_y = random.randint(0, 550)
blackhole_speed = 5
blackhole_size = 50



clock = pygame.time.Clock()
running = True

game_over = False
score = 0
high_score = 0
score_font = pygame.font.Font(None, 8)
stardust = pygame.font.Font("ZerpixlVolt-Italic.ttf", 30)

def reset_game():
    global game_over 
    global spaceship_speed, blackhole_speed
    global score 
    global spaceship_x, spaceship_y
    global star_x, star_y
    global blackhole_x, blackhole_y
    spaceship_x = 400
    spaceship_y = 350
    star_x = random.randint(20, 680)
    star_y = random.randint(20, 580)
    blackhole_x = 650
    blackhole_y = random.randint(0, 550)
    score = 0
    high_score = 0
    game_over = False
    spaceship_speed = 10
    blackhole_speed = 5

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                reset_game()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        spaceship_x -= spaceship_speed

    if keys[pygame.K_RIGHT]:
        spaceship_x += spaceship_speed

    if keys[pygame.K_UP]:
        spaceship_y -= spaceship_speed

    if keys[pygame.K_DOWN]:
        spaceship_y += spaceship_speed


#keep spaceship in game window
#left
    if spaceship_x < 0:
        spaceship_x = 0
#right
    if spaceship_x > 700 - 80:
        spaceship_x = 700-80
#top
    if spaceship_y < 0:
        spaceship_y = 0
#down
    if spaceship_y > 600 - 80:
        spaceship_y = 600-80
    
    spaceship_ship = pygame.Rect(spaceship_x, spaceship_y, 80, 80)
    star = pygame.Rect(
        star_x - star_size,
        star_y - star_size,
        star_size *2,
        star_size *2
    )
    score_screen = stardust.render(
      "score" + str(score),
      True, "dark blue"
    )
    high_score_screen = stardust.render("THIS IS YOUR HIGH SCORE" + str (high_score), True, "cyan")
    if not game_over and spaceship_ship.colliderect(star):
        score += 1
        star_x = random.randint(20, 680)
        star_y = random.randint(20, 580)
    blackhole = pygame.Rect(
        blackhole_x,
        blackhole_y,
        blackhole_size,
        blackhole_size
    )
    blackhole_x -= blackhole_speed
    if blackhole_x < blackhole_size:
        blackhole_x = 650
        blackhole_y = random.randint(0, 550)

    if spaceship_ship.colliderect(blackhole):
        # score += 1
        #print("score", score)
        game_over = True
        spaceship_speed = 0
        blackhole_speed = 0
        if score > high_score:
          high_score = score 

    






    if spaceship_ship.colliderect(star):
       # score += 1
       #print("score", score)
        star_x = random.randint(20, 400)
        star_y = random.randint(20, 350)

    game_window.fill((75, 0, 130))
    game_window.blit(spaceship_image,(spaceship_x,spaceship_y))
    game_window.blit(score_screen, (20, 20))
    game_window.blit(high_score_screen, (20, 60) )
    pygame.draw.circle(game_window, "yellow", (star_x, star_y), star_size)
    pygame.draw.rect(game_window, (4,10,12), blackhole)
    if game_over:
        game_over_screen = stardust.render(
         "You have been absorbed",
         True, "white"
        )
        game_window.blit(
         game_over_screen,
         (190, 260)
     )
    pygame.display.flip()
    clock.tick(60)
pygame.quit()