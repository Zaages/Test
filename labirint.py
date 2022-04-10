from pygame import * 



init()
black = (0, 0, 0)
white = (255, 255, 255)
color = (150, 150, 150)
run = True
shrift = font.Font(None, 36)
points = 0
image_win = transform.scale(image.load('thumb.jpg'), (700, 500))
image_lose = transform.scale(image.load('game-over.png'), (700, 500))
display.set_caption('Game')
window = display.set_mode((700, 500))


class GameSprite(sprite.Sprite):
    def __init__(self, pic, w, h, x, y):
        super().__init__()
        self.image = transform.scale(image.load(pic), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def blit_images(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class player(GameSprite):
    def __init__(self, pic, w, h, x, y):
        self.speed_x = 0
        self.speed_y = 0
        super().__init__(pic, w, h, x, y)
    def dvijenie(self, barriers):
        self.rect.x += self.speed_x
        stolknovenie = sprite.spritecollide(self, barriers, False)
        if self.speed_x > 0:
            for kto_to in stolknovenie:
                self.rect.right = min(self.rect.right, kto_to.rect.left)

        elif self.speed_x < 0:
            for kto_to in stolknovenie:
                self.rect.left = max(self.rect.left, kto_to.rect.right)


        self.rect.y += self.speed_y
        stolknovenie = sprite.spritecollide(self, barriers, False)
        if self.speed_y > 0:
            for kto_to in stolknovenie:
                self.rect.bottom = min(self.rect.bottom, kto_to.rect.top)

        elif self.speed_y < 0:
            for kto_to in stolknovenie:
                self.rect.top = max(self.rect.top, kto_to.rect.bottom)
    def fire(self, direction_x, direction_y, speed_x, speed_y):
        bullet = Bullet('Ball.png', 25, 25, direction_x, direction_y, speed_x, speed_y)
        bullets.add(bullet)




class Enemy(GameSprite):
    def __init__(self, pic, w, h, x, y):
        self.speed_x = 0
        self.speed_y = 0
        super().__init__(pic, w, h, x, y)
    def update(self):
        self.rect.x += self.speed_x
        if self.rect.x <= 400:
            self.speed_x = 2
        if self.rect.x >= 635:
            self.speed_x = -2

class Bullet(GameSprite):
    def __init__(self, pic, w, h, x, y, speed_x, speed_y):
        self.speed_x = speed_x
        self.speed_y = speed_y
        super().__init__(pic, w, h, x, y)
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.x >= 700:
            self.kill()



spisok_ekzemlplarov = [player('player_R.png', 50, 50, 50, 400),
                    player('player_L.png', 50, 50, 50, 400),
                    player('player_D.png', 50, 50, 50, 400),
                    player('player_U.png', 50, 50, 50, 400),
                    player('player_D_L.png', 50, 50, 50, 400),
                    player('player_D_R.png', 50, 50, 50, 400),
                    player('player_U_L.png', 50, 50, 50, 400),
                    player('player_U_R.png', 50, 50, 50, 400),
                    GameSprite('platform2.png', 160, 50, 200, 340),
                    GameSprite('platform2_v.png', 50, 190, 350, 200),
                    GameSprite('Money.png', 50, 50, 140, 135),
                    GameSprite('platform2_v.png', 50, 500, 0, 0),
                    GameSprite('platform2.png', 200, 50, 50, 200),
                    GameSprite('platform2_v.png', 50, 170, 200, 75),
                    GameSprite('platform2.png', 110, 50, 140, 75),
                    GameSprite('platform2_v.png', 50, 300, 200, 340),
                    GameSprite('platform2.png', 200, 50, 350, 200),
                    Enemy('cyborg.png', 65, 65, 400, 300),
                    GameSprite('finish.png', 65, 65, 250, 425),
                    ]

barriers = sprite.Group()
barriers.add(spisok_ekzemlplarov[8])
barriers.add(spisok_ekzemlplarov[9])
barriers.add(spisok_ekzemlplarov[11])
barriers.add(spisok_ekzemlplarov[12])
barriers.add(spisok_ekzemlplarov[13])
barriers.add(spisok_ekzemlplarov[14])
barriers.add(spisok_ekzemlplarov[15])
barriers.add(spisok_ekzemlplarov[16])

monsters = sprite.Group()
monsters.add(spisok_ekzemlplarov[17])

bullets = sprite.Group()
speed_x = 0
speed_y = 0
direction_x = 0
direction_y = 0
basic = spisok_ekzemlplarov[0]
while run:
    for events in event.get():
        if events.type == QUIT:
            exit()
        if events.type == KEYDOWN:
            if events.key == K_SPACE:
                spisok_ekzemlplarov[0].fire(direction_x, direction_y, speed_x, speed_y)

            if events.key == K_UP:
                spisok_ekzemlplarov[0].speed_y = -1
                spisok_ekzemlplarov[1].speed_y = -1
                spisok_ekzemlplarov[2].speed_y = -1
                spisok_ekzemlplarov[3].speed_y = -1
                spisok_ekzemlplarov[4].speed_y = -1
                spisok_ekzemlplarov[5].speed_y = -1
                spisok_ekzemlplarov[6].speed_y = -1
                spisok_ekzemlplarov[7].speed_y = -1
                


            if events.key == K_DOWN:
                spisok_ekzemlplarov[0].speed_y = 1
                spisok_ekzemlplarov[1].speed_y = 1
                spisok_ekzemlplarov[2].speed_y = 1
                spisok_ekzemlplarov[3].speed_y = 1
                spisok_ekzemlplarov[4].speed_y = 1
                spisok_ekzemlplarov[5].speed_y = 1
                spisok_ekzemlplarov[6].speed_y = 1
                spisok_ekzemlplarov[7].speed_y = 1



            if events.key == K_LEFT:
                spisok_ekzemlplarov[0].speed_x = -1
                spisok_ekzemlplarov[1].speed_x = -1
                spisok_ekzemlplarov[2].speed_x = -1
                spisok_ekzemlplarov[3].speed_x = -1
                spisok_ekzemlplarov[4].speed_x = -1
                spisok_ekzemlplarov[5].speed_x = -1
                spisok_ekzemlplarov[6].speed_x = -1
                spisok_ekzemlplarov[7].speed_x = -1

            if events.key ==  K_RIGHT:
                spisok_ekzemlplarov[0].speed_x = 1
                spisok_ekzemlplarov[1].speed_x = 1
                spisok_ekzemlplarov[2].speed_x = 1
                spisok_ekzemlplarov[3].speed_x = 1
                spisok_ekzemlplarov[4].speed_x = 1
                spisok_ekzemlplarov[5].speed_x = 1
                spisok_ekzemlplarov[6].speed_x = 1
                spisok_ekzemlplarov[7].speed_x = 1
            




        if events.type == KEYUP:
            if events.key == K_UP:
                spisok_ekzemlplarov[0].speed_y = 0
                spisok_ekzemlplarov[1].speed_y = 0
                spisok_ekzemlplarov[2].speed_y = 0
                spisok_ekzemlplarov[3].speed_y = 0
                spisok_ekzemlplarov[4].speed_y = 0
                spisok_ekzemlplarov[5].speed_y = 0
                spisok_ekzemlplarov[6].speed_y = 0
                spisok_ekzemlplarov[7].speed_y = 0


            if events.key == K_DOWN:
                spisok_ekzemlplarov[0].speed_y = 0
                spisok_ekzemlplarov[1].speed_y = 0
                spisok_ekzemlplarov[2].speed_y = 0
                spisok_ekzemlplarov[3].speed_y = 0
                spisok_ekzemlplarov[4].speed_y = 0
                spisok_ekzemlplarov[5].speed_y = 0
                spisok_ekzemlplarov[6].speed_y = 0
                spisok_ekzemlplarov[7].speed_y = 0

            if events.key == K_LEFT:
                spisok_ekzemlplarov[0].speed_x = 0
                spisok_ekzemlplarov[1].speed_x = 0
                spisok_ekzemlplarov[2].speed_x = 0
                spisok_ekzemlplarov[3].speed_x = 0
                spisok_ekzemlplarov[4].speed_x = 0
                spisok_ekzemlplarov[5].speed_x = 0
                spisok_ekzemlplarov[6].speed_x = 0
                spisok_ekzemlplarov[7].speed_x = 0


            if events.key ==  K_RIGHT:
                spisok_ekzemlplarov[0].speed_x = 0
                spisok_ekzemlplarov[1].speed_x = 0
                spisok_ekzemlplarov[2].speed_x = 0
                spisok_ekzemlplarov[3].speed_x = 0
                spisok_ekzemlplarov[4].speed_x = 0
                spisok_ekzemlplarov[5].speed_x = 0
                spisok_ekzemlplarov[6].speed_x = 0
                spisok_ekzemlplarov[7].speed_x = 0

                
    if spisok_ekzemlplarov[0].speed_y < 0 and spisok_ekzemlplarov[0].speed_x == 0:
        basic = spisok_ekzemlplarov[3]
        direction_x = spisok_ekzemlplarov[0].rect.x + 25
        direction_y = spisok_ekzemlplarov[0].rect.y
        speed_x = 0
        speed_y = -8
    if spisok_ekzemlplarov[0].speed_y > 0 and spisok_ekzemlplarov[0].speed_x == 0:
        basic = spisok_ekzemlplarov[2]
        direction_x = spisok_ekzemlplarov[0].rect.x + 25
        direction_y = spisok_ekzemlplarov[0].rect.y + 50
        speed_x = 0
        speed_y = 8
    if spisok_ekzemlplarov[0].speed_x > 0 and spisok_ekzemlplarov[0].speed_y == 0:
        basic = spisok_ekzemlplarov[0]
        direction_x = spisok_ekzemlplarov[0].rect.x + 50
        direction_y = spisok_ekzemlplarov[0].rect.y + 25
        speed_x = 8
        speed_y = 0
    if spisok_ekzemlplarov[0].speed_x < 0 and spisok_ekzemlplarov[0].speed_y == 0:
        basic = spisok_ekzemlplarov[1]
        direction_x = spisok_ekzemlplarov[0].rect.x
        direction_y = spisok_ekzemlplarov[0].rect.y + 25
        speed_x = -8
        speed_y = 0



    if spisok_ekzemlplarov[0].speed_x > 0 and spisok_ekzemlplarov[0].speed_y > 0:
        basic = spisok_ekzemlplarov[5]
        direction_x = spisok_ekzemlplarov[0].rect.x + 50
        direction_y = spisok_ekzemlplarov[0].rect.y + 50
        speed_x = 8
        speed_y = 8
    if spisok_ekzemlplarov[0].speed_x < 0 and spisok_ekzemlplarov[0].speed_y > 0:
        basic = spisok_ekzemlplarov[4]
        direction_x = spisok_ekzemlplarov[0].rect.x
        direction_y = spisok_ekzemlplarov[0].rect.y + 50
        speed_x = -8
        speed_y = 8
    if spisok_ekzemlplarov[0].speed_x > 0 and spisok_ekzemlplarov[0].speed_y < 0:
        basic = spisok_ekzemlplarov[7]
        direction_x = spisok_ekzemlplarov[0].rect.x + 50
        direction_y = spisok_ekzemlplarov[0].rect.y
        speed_x = 8
        speed_y = -8
    if spisok_ekzemlplarov[0].speed_x < 0 and spisok_ekzemlplarov[0].speed_y < 0:
        basic = spisok_ekzemlplarov[6]
        direction_x = spisok_ekzemlplarov[0].rect.x
        direction_y = spisok_ekzemlplarov[0].rect.y
        speed_x = -8
        speed_y = -8



                

    
    window.fill(color)
    if not sprite.collide_rect(spisok_ekzemlplarov[0], spisok_ekzemlplarov[10]) and points != 1:
        spisok_ekzemlplarov[10].blit_images()
    else:
        points = 1
    if sprite.spritecollide(spisok_ekzemlplarov[0], monsters, False):
        Win = False
        run = False
    if sprite.collide_rect(spisok_ekzemlplarov[0], spisok_ekzemlplarov[18]):
        Win = True
        run = False
    text = shrift.render('Points: ' + str(points), True, (255, 0, 0))
    window.blit(text, (580, 25))
    monsters.update()
    basic.blit_images()
    spisok_ekzemlplarov[0].dvijenie(barriers)
    spisok_ekzemlplarov[1].dvijenie(barriers)
    spisok_ekzemlplarov[2].dvijenie(barriers)
    spisok_ekzemlplarov[3].dvijenie(barriers)
    spisok_ekzemlplarov[4].dvijenie(barriers)
    spisok_ekzemlplarov[5].dvijenie(barriers)
    spisok_ekzemlplarov[6].dvijenie(barriers)
    spisok_ekzemlplarov[7].dvijenie(barriers)
    spisok_ekzemlplarov[18].blit_images()
    monsters.draw(window)
    bullets.update()
    bullets.draw(window)
    sprite.groupcollide(bullets, barriers, True, False)
    sprite.groupcollide(bullets, monsters, True, True)
    barriers.draw(window)

    
    time.delay(10)
    display.update()
window.fill(color)
while Win:
    window.blit(image_win, (0, 0))
    for events in event.get():
        if events.type == QUIT:
            exit()
    window.blit(text, (20, 400))
    display.update()
while not Win:
    window.blit(image_lose, (0, 0))
    for events in event.get():
        if events.type == QUIT:
            exit()
    display.update()

