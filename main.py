import pygame
from sys import exit
from random import randint
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - star_time
    score_surf = fontA.render(f'Score: {current_time}',False,(64,64,64))
    score_rec = score_surf.get_rect(center = (400,50))
    secreen.blit(score_surf,score_rec)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstcle_rect in obstacle_list:
            obstcle_rect.x -= 5
            if obstcle_rect.bottom == 300:
                secreen.blit(snail_surf,obstcle_rect)
            else:
                secreen.blit(fly_surf, obstcle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: return []

def collitions(player,obstacles):
    if obstacles:
        for obstacle_rec in obstacles:
            if player.colliderect(obstacle_rec): return False
    return True
def player_animation():
    global player_surf, player_index
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk):player_index = 0
        player_surf = player_walk[int(player_index)]

pygame.init()
wdith = 800
hight = 400
sWdith = 10
sHight = 10
game_active = False
star_time = 0
score = 0
player_gravity = 0
secreen = pygame.display.set_mode((wdith,hight))
fontA = pygame.font.Font('font/Pixeltype.ttf',50)
pygame.display.set_caption("Corredor")
clock = pygame.time.Clock()
skyImg = pygame.image.load('graphics/Sky.png').convert_alpha()
groundImg = pygame.image.load('graphics/ground.png').convert_alpha()
#scoreText = fontA.render('Mi Juego', False , (64,64,64))
#scoreTextrec = scoreText.get_rect(center = (400,50))
player_walk1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk1,player_walk2]
player_index = 0
player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))

#obstacles
snail_frame_1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_frame_2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
snail_frames = [snail_frame_1,snail_frame_2]
snail_frame_index = 0
snail_surf = snail_frames[snail_frame_index]

fly_frame1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
fly_frame2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly_frame1,fly_frame2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

obstacle_rec_list = []

#instro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_text = fontA.render('Pixel Runner',False,(111,196,169))
game_text_rec = game_text.get_rect(center = (400,80))

game_message = fontA.render('Press Space to Start!!',False,(111,196,169))
game_message_rec = game_message.get_rect(center = (400,320))
#timer
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

snail_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #if event.type == pygame.MOUSEMOTION:
        #    if player_rect.collidepoint(event.pos):
        #        print('funciona')
        if game_active:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos) and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and game_active == False:
                    game_active = True
                    star_time = int(pygame.time.get_ticks() / 1000)
        if game_active:
            if event.type == obstacle_timer:
                if randint(0,2):
                    obstacle_rec_list.append(snail_surf.get_rect(midbottom=(randint(900,1100),300)))
                else:
                    obstacle_rec_list.append(fly_surf.get_rect(midbottom=(randint(900, 1100), 210)))
            if event.type == snail_animation_timer:
                if snail_frame_index == 0: snail_frame_index = 1
                else: snail_frame_index = 0
                snail_surf = snail_frames[snail_frame_index]

            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]

    #dibuamos los elementos
    #updateamos todo
    if game_active:
        secreen.blit(skyImg,(0,0))
        secreen.blit(groundImg, (0, 300))
        #pygame.draw.rect(secreen,'#c0e8ec',scoreTextrec)
        #pygame.draw.rect(secreen, '#c0e8ec', scoreTextrec, 10)
        #secreen.blit(scoreText, scoreTextrec)
        score = display_score()
        #secreen.blit(caracolSurfaceIzquierda1, caracolSurfaceIzquierda1Rect)
        #caracolSurfaceIzquierda1Rect.right -= 4
        #if caracolSurfaceIzquierda1Rect.right < -100: caracolSurfaceIzquierda1Rect.right = 800

        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300 : player_rect.bottom = 300
        player_animation()
        secreen.blit(player_surf, player_rect)
        #obstacle movement
        obstacle_rec_list = obstacle_movement(obstacle_rec_list)
        #collision
        game_active = collitions(player_rect,obstacle_rec_list)
    else:
        secreen.fill((94,129,162))
        secreen.blit(player_stand,player_stand_rect)
        score_message = fontA.render(f'Your Score: {score}',False,(111,196,169))
        score_message_rec = score_message.get_rect(center = (400,330))
        obstacle_rec_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0

        secreen.blit(game_text,game_text_rec)
        if score == 0:
            secreen.blit(game_message,game_message_rec)
        else:
            secreen.blit(score_message,score_message_rec)
    #keys = pygame.key.get_pressed()
    #if keys[pygame.K_SPACE]:
    #    print('jump')
    #mouse_pos = pygame.mouse.get_pos()
    #se fija si el mouse esta sobre el rectangulo
    #if player_rect.collidepoint(mouse_pos):
        #muestra los botones q se tocan del mouse
        #print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)