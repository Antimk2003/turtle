import turtle
import colorsys 
turtle.bgcolor("red")
turtle.tracer(100)
h = 0.4
def draw(ang,n):
    turtle.circle(5+n,60)
    turtle.left(ang)
    turtle.circle(5+n,60)
for i in range(200):
    c = colorsys.hsv_to_rgb(h, 1 , 1)
    h +=0.005
    turtle.color(c)
    turtle.pensize(5)
    draw(90,i*2)
    draw(120,i*2.5)   