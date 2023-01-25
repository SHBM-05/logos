import turtle

colors = ['red' , 'yellow' , 'green' , 'purple' ,'blue' ,'pink']
t= turtle.Pen()
t.speed(40)
turtle.bgcolor("black")
for x in range(300):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

turtle.done()
t.speed(30)
turtle.bgcolor("black")
for x in range(300):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(59)

turtle.done()

