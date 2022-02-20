import pygame
from sys import exit
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) - star_time
    score_surf = fontA.render(f'Score: {current_time}',False,(64,64,64))
    score_rec = score_surf.get_rect(center = (400,50))
    secreen.blit(score_surf,score_rec)
    return current_time

pygame.init()
wdith = 800
hight = 400
sWdith = 10
sHight = 10
game_active = False
star_time = 0
score = 0
secreen = pygame.display.set_mode((wdith,hight))
fontA = pygame.font.Font('font/Pixeltype.ttf',50)
pygame.display.set_caption("Corredor")
clock = pygame.time.Clock()
skyImg = pygame.image.load('graphics/Sky.png').convert_alpha()
groundImg = pygame.image.load('graphics/ground.png').convert_alpha()
#scoreText = fontA.render('Mi Juego', False , (64,64,64))
#scoreTextrec = scoreText.get_rect(center = (400,50))
player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
caracolSurfaceIzquierda1 = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
caracolSurfaceIzquierda1Rect = caracolSurfaceIzquierda1.get_rect(midbottom = (600,300))
caracolSurfaceIzquierda2 = pygame.image.load('graphics/snail/snail2.png').convert_alpha()
player_gravity = 0

#instro screen
player_stand = pygame.image.load('graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.scale2x(player_stand)
player_stand_rect = player_stand.get_rect(center = (400,200))

game_text = fontA.render('Pixel Runner',False,(111,196,169))
game_text_rec = game_text.get_rect(center = (400,80))

game_message = fontA.render('Press Space to Start!!',False,(111,196,169))
game_message_rec = game_message.get_rect(center = (400,320))
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
                    caracolSurfaceIzquierda1Rect.right = 600
                    game_active = True
                    star_time = int(pygame.time.get_ticks() / 1000)
    #dibuamos los elementos
    #updateamos todo
    if game_active:
        secreen.blit(skyImg,(0,0))
        secreen.blit(groundImg, (0, 300))
        #pygame.draw.rect(secreen,'#c0e8ec',scoreTextrec)
        #pygame.draw.rect(secreen, '#c0e8ec', scoreTextrec, 10)
        #secreen.blit(scoreText, scoreTextrec)
        score = display_score()
        secreen.blit(caracolSurfaceIzquierda1, caracolSurfaceIzquierda1Rect)
        caracolSurfaceIzquierda1Rect.right -= 4
        if caracolSurfaceIzquierda1Rect.right < -100: caracolSurfaceIzquierda1Rect.right = 800

        player_gravity += 1
        secreen.blit(player_surf,player_rect)
        player_rect.y += player_gravity
        if player_rect.bottom >= 300 : player_rect.bottom = 300
        if caracolSurfaceIzquierda1Rect.colliderect(player_rect):
            game_active = False
    else:
        secreen.fill((94,129,162))
        secreen.blit(player_stand,player_stand_rect)
        score_message = fontA.render(f'Your Score: {score}',False,(111,196,169))
        score_message_rec = score_message.get_rect(center = (400,330))
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