import turtle
turtle.setup(650,350,200,200)
turtle.penup()
turtle.width(20)
turtle.fd(-250)
turtle.pendown()
turtle.pencolor("gold")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40*2/3)
turtle.done()#用来保持绘画结束界面不消失