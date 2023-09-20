from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 0
t = 0

while(1):
    while (x < 800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x-30,90)
        x = x + 10
        delay(0.01)
    while (y < 510):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(770,y+90)
        y = y + 10
        delay(0.01)
    while (x > 0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x-30,600)
        x = x - 10
        delay(0.01)
    while (y > 30):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(0,y+90)
        y = y - 10
        delay(0.01)
    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x-30,90)
        x = x + 10
        delay(0.01)  
    while (t < 360):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x = x+(math.cos(math.pi/180*t)) * 25
        y = y+(math.sin(math.pi/180*t)) * 25
        t = t+5
        delay(0.01)
    t = 0
