try:    import pygame; import SimpleGUICS2Pygame.simpleguics2pygame as sg
except: import simplegui as sg
try:    from user304_rsf8mD0BOQ_1 import Vector
except: from V1 import Vector
import math


WIDTH = 800
HEIGHT = 600
y1 = HEIGHT-60; y2 = HEIGHT-35


bricks = []
x = 0 
score = 0

#start coord
xx  = 30 #pointx[0]
y = 50   #pointx[1] and pointy[1]
yx = 160 #pointy[0]
pointx = xx,y

def add_brick(): 
    global x, bricks, xx, yx, y
    x += 1

    #centre line for bricks
    pointx = xx,y
    pointy = yx,y
    points = (pointx, pointy)

    #height of brick 
    width = 50
    colour = "white"

    brick = Bricks(points, width, colour, bricks)
    bricks.append(brick)

    xx += 150
    yx += 150

    if xx > 700:
        y += 70
        xx = 30 
        yx = 160

    if y > 300:
        y +=0
        xx = WIDTH 
        yx = WIDTH


class Bricks:
    def __init__(self, points, width, colour, bricks):
        self.pos = points
        self.width = width
        self.colour = colour
        self.bricks = bricks
        self.visible = True

    def draw(self, canvas):
        if self.visible:
            canvas.draw_polygon(self.pos, self.width, self.colour)
        
    def hit(self, ball, singlebrick):
        if self.bricks[singlebrick].visible:
            h = self.pos[0][1]<= ball.pos.y <= self.pos[0][1] + 40 and self.pos[0][0] - 40 <= ball.pos.x <= self.pos[0][0] + 140
            if h:
                self.bricks[singlebrick].visible = False
                
            #self.bricks[singlebrick].visible = False
            """
            print("self.pos.x:")
            print(self.pos[0][0])
            print("ball.pos.x:")
            print(ball.pos.x)"""
        else:
            h = False
        return h 

    
class Paddle:
    def __init__(self, pos, radius=10):
        self.pos = pos
        self.vel = Vector()
        self.normal = Vector(0, 1)
        self.radius = max(radius, 10)
        self.colour = 'black'

    def draw(self, canvas):
        global x1, x2
        canvas.draw_polygon([(self.pos.x, y1), (self.pos.x, y2), (self.pos.x + 150, y2), (self.pos.x + 150, y1)], 5, "white")
        frame.set_canvas_background("black")

    def hit(self, ball):
        h = self.pos.y-40 <= ball.pos.y <= self.pos.y and self.pos.x-20 <= ball.pos.x <= self.pos.x + 171
        return h 

    def update(self):
        if self.pos.x < 0:
            self.pos = Vector(WIDTH, HEIGHT - 40)
        elif self.pos.x > WIDTH:
            self.pos = Vector(0, HEIGHT - 40)

        self.pos.add(self.vel);
        self.vel.multiply(0.85)
        
        
class Wall:
    def __init__(self, x):
        self.x = x
        self.normal = Vector(1,0)
        self.edge_r = x
        self.edge_l = WIDTH - 40

    def hit(self, ball):
        if (ball.offset_l() <= self.edge_r) == True:
            h = (ball.offset_l() <= self.edge_r)
            print("left wall")
            return h

        if (ball.offset_l() >= self.edge_l) == True:
            h = (ball.offset_l() >= self.edge_l)
            print("right wall")
            return h


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
    def __init__(self, paddle, ball, keyboard, bricks, wall, bricknum):
        self.paddle = paddle
        self.keyboard = keyboard
        self.ball = ball
        self.bricks = bricks
        self.in_col = False; self.in_collision = True
        self.wall = wall
        self.bricknum = bricknum

    def update(self, canvas):
        global score
        
        if self.keyboard.right:
            self.paddle.vel.add(Vector(1, 0))
        
        elif self.keyboard.left:
            self.paddle.vel.add(Vector(-1, 0))
            
        if self.wall.hit(self.ball):
            if not self.in_collision:
                self.ball.bounce(self.wall.normal)
                self.in_collision = True
            else:
                self.in_collision = False
                
        if self.paddle.hit(self.ball) or 0 <= self.ball.pos.y <= 10:
            if not self.in_col:
                
                self.ball.bounce(self.paddle.normal)
                in_col = True
            else:
                self.in_col = False

                
        for a in range(0, len(self.bricks)):
            if self.bricks[a].hit(self.ball, a):
                if not self.in_col:
                    self.ball.bounce(self.paddle.normal)
                    #specific brick col:
                    #self.bricks[0].bricks[14].visible = False
                    score += 10
                else:
                    self.in_col = False
                    
        self.ball.update()
        self.paddle.update()

    def draw(self, canvas):
        global score
        self.update(canvas)
        self.paddle.draw(canvas)
        self.ball.draw(canvas)
        
        del self.bricks[self.bricknum:]
        for a in range(0, len(self.bricks)):
            self.bricks[a].draw(canvas)
        
        canvas.draw_text("Score: " + str(score), (5, 15) , 19, "white")


bpos = Vector(WIDTH/2, 500); bmov = Vector(1,-9)
ball = Ball(bpos, bmov, 15, 15, 'white')
kbd = Keyboard()

paddle = Paddle(Vector((WIDTH / 2)-75, HEIGHT - 40), 40)

wall = Wall(0)
add_brick = sg.create_timer(12, add_brick)
add_brick.start()

inter = Interaction(paddle, ball, kbd, bricks, wall, 15)
frame = sg.create_frame('Brickbreaker', WIDTH, HEIGHT)
frame.set_draw_handler(inter.draw); frame.set_keydown_handler(kbd.keyDown); frame.set_keyup_handler(kbd.keyUp)
frame.start()
