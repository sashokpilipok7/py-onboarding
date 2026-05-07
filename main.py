


from turtle import Turtle

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

one = Turtle()
forward = 30
deg = 60

for color in colors:
    for second_color in colors:
        one.color(color)
        one.forward(forward)
        one.right(deg)
    one.right(deg)
    
