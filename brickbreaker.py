import simplegui as sg

x1 = 300; x2 = 440
y1 = 500; y2 = 525

offset = 0;

def draw(cnv):
    global x1, x2
    x1 += offset; x2 += offset
    cnv.draw_polygon([(x1 + offset, y1), (x1 + offset, y2), (x2 + offset, y2), (x2 + offset, y1)], 5, "white")

def keyup(key):
    global offset
    if key == sg.KEY_MAP['right']:
        offset = 0
    elif key == sg.KEY_MAP['left']:
        offset = 0

def keydown(key):
    global offset
    if key == sg.KEY_MAP['right']:
        offset = 7;
    elif key == sg.KEY_MAP['left']:
        offset = -7;


fr = sg.create_frame("main", 800, 600)
fr.set_draw_handler(draw); fr.set_keydown_handler(keydown); fr.set_keyup_handler(keyup)
fr.start()


