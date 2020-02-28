try:    import pygame; import SimpleGUICS2Pygame.simpleguics2pygame as sg
except: import simplegui as sg
try:    from user304_rsf8mD0BOQ_1 import Vector
except: from V1 import Vector
import math

WIDTH = 800
HEIGHT = 600
y1 = HEIGHT-60; y2 = HEIGHT-35

class Paddle:
    def __init__(self, pos, radius=10):
        self.pos = pos
        self.vel = Vector()
        self.normal = Vector(0, 1)
        self.radius = max(radius, 10)
        self.colour = 'White'

    def draw(self, canvas):
        global x1, x2
        canvas.draw_polygon([(self.pos.x, y1), (self.pos.x, y2), (self.pos.x + 150, y2), (self.pos.x + 150, y1)], 5, "white")

    def hit(self, ball):
        h = self.pos.y-35 <= ball.pos.y <= self.pos.y
        return h

    def update(self):
        if self.pos.x < 0:
            self.pos = Vector(WIDTH, HEIGHT - 40)
        elif self.pos.x > WIDTH:
            self.pos = Vector(0, HEIGHT - 40)

        self.pos.add(self.vel);
        self.vel.multiply(0.85)


class Ball:
    def __init__(self, pos, vel, radius, border, color):
        self.pos = pos; self.vel = vel
        self.radius = radius; self.border = 1
        self.color = color

    def offset_l(self):
        return self.pos.x - self.radius

    def update(self):
        self.pos.add(self.vel)

    def draw(self, canvas):
        canvas.draw_circle(self.pos.get_p(),self.radius,self.border,
                           self.color, self.color)
    def bounce(self, normal):
        self.vel.reflect(normal)


class Keyboard:
    def __init__(self):
        self.right = False; self.left = False

    def keyDown(self, key):
        if key == sg.KEY_MAP['right']:
            self.right = True
        elif key == sg.KEY_MAP['left']:
            self.left = True

    def keyUp(self, key):
        if key == sg.KEY_MAP['right']:
            self.right = False
        elif key == sg.KEY_MAP['left']:
            self.left = False


class Interaction:
    def __init__(self, paddle, ball, keyboard):
        self.paddle = paddle; self.keyboard = keyboard; self.ball = ball
        self.in_col = False

    def update(self):
        if self.keyboard.right:
            self.paddle.vel.add(Vector(1, 0))
        elif self.keyboard.left:
            self.paddle.vel.add(Vector(-1, 0))

        if self.paddle.hit(self.ball) or 0 <= self.ball.pos.y <= 10:

            if not self.in_col:
                self.ball.bounce(self.paddle.normal)
                in_col = True
            else:
                self.in_col = False
        self.ball.update()
        self.paddle.update()

    def draw(self, canvas):
        self.update();
        self.paddle.draw(canvas);
        self.ball.draw(canvas);



bpos = Vector(WIDTH/2, HEIGHT/2); bmov = Vector(1,3)
ball = Ball(bpos, bmov, 15, 15, 'grey')

kbd = Keyboard()
paddle = Paddle(Vector((WIDTH / 2)-75, HEIGHT - 40), 40)
inter = Interaction(paddle, ball, kbd)





frame = sg.create_frame('Brickbreaker', WIDTH, HEIGHT)
frame.set_draw_handler(inter.draw); frame.set_keydown_handler(kbd.keyDown); frame.set_keyup_handler(kbd.keyUp)
frame.start()
