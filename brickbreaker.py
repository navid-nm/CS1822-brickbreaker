
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


#class Interaction:
    def __init__(self, paddle, ball, keyboard, wall):
  #      self.paddle = paddle; self.keyboard = keyboard; self.ball = ball
   #     self.in_col = False
        self.wall=wall
        self.in_collision=True

 #   def update(self):
     #   if self.keyboard.right:
  #          self.paddle.vel.add(Vector(1, 0))
   #     elif self.keyboard.left:
    #        self.paddle.vel.add(Vector(-1, 0))
            
        if self.wall.hit(self.ball):
            if not self.in_collision:
                self.ball.bounce(self.wall.normal)
                self.in_collision = True
                
            else:
                self.in_collision = False
      #  if self.paddle.hit(self.ball) or 0 <= self.ball.pos.y <= 10:

       #     if not self.in_col:
        #        self.ball.bounce(self.paddle.normal)
         #       in_col = True
          #  else:
           #     self.in_col = False
        #self.ball.update()
        #self.paddle.update()

    #def draw(self, canvas):
     #   self.update();
      #  self.paddle.draw(canvas);
       # self.ball.draw(canvas);



#bpos = Vector(WIDTH/2, HEIGHT/2); bmov = Vector(1,4)
#ball = Ball(bpos, bmov, 15, 15, 'grey')
wall= Wall(0)

#kbd = Keyboard()
#paddle = Paddle(Vector((WIDTH / 2)-75, HEIGHT - 40), 40)
inter = Interaction(paddle, ball, kbd, wall)





#frame = sg.create_frame('Brickbreaker', WIDTH, HEIGHT)
#frame.set_draw_handler(inter.draw); frame.set_keydown_handler(kbd.keyDown); frame.set_keyup_handler(kbd.keyUp)
#frame.start()
