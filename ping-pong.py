from pygame import *

font.init()
font = font.Font(None,70)

x1 = 5
x2 = 660
y1 = 250
y2 = 300
class GameSprite(sprite.Sprite):
        def __init__(self, player_image, speed, rect_x, rect_y,x, y):
                super().__init__()
                self.image = transform.scale(
                        image.load(player_image),
                        (x, y)
                )
                self.speed = speed
                self.rect = self.image.get_rect()
                self.rect.x = rect_x
                self.rect.y = rect_y
        def reset(self):
                window.blit(self.image, (self.rect.x, self.rect.y))
class Player1(GameSprite):
        def update(self):
                keys_pressed = key.get_pressed()
                if keys_pressed[K_w] and self.rect.y > 0:
                        self.rect.y -= self.speed
                if keys_pressed[K_s] and self.rect.y < 380:
                        self.rect.y += self.speed

class Player2(GameSprite):
        def update(self):
                keys_pressed = key.get_pressed()
                if keys_pressed[K_UP] and self.rect.y > 0:
                        self.rect.y -= self.speed
                if keys_pressed[K_DOWN] and self.rect.y < 380:
                        self.rect.y += self.speed

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption('Догонялки')

clock = time.Clock()

FPS = 120


bg = transform.scale(
        image.load('bg.jpeg'),
        (700, 500)
    )

#задай фон сцены
sprite1 = Player1('wall.png', 5, x1,y1, 20, 150)
sprite2 = Player2('wall.png', 5, x2,y2, 20, 150)

ball = GameSprite('ball.png', 2, 350, 250, 40,40)


speed_x = 2
speed_y = 2
finish = False
game = True
while game:
    clock.tick(FPS)
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(bg, (0, 0))
        sprite1.reset()
        sprite2.reset()
        ball.reset()
        sprite1.update()
        sprite2.update()
        ball.rect.x += speed_x
        ball.rect.y -= speed_y
        if ball.rect.y <= 0:
            speed_y *= -1
        if ball.rect.y >= 470:
            speed_y *= -1
        if sprite.collide_rect(sprite1, ball):
            speed_x *= -1
        if sprite.collide_rect(sprite2, ball):
            speed_x *= -1
        if ball.rect.x >= 670:
            lose = font.render(
                'Player 2 Lose!', True, (255, 0, 0)
            )
            window.blit(lose, (200,250))
            finish = True

        if ball.rect.x <= 4:
            lose = font.render(
                'Player 1 Lose!', True, (255, 0, 0)
            )
            window.blit(lose, (200,250))
            finish = True    
            
        
    display.update()
        
