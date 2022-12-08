
from re import X
import turtle

sc=turtle.Screen()
turtle.turtles()
sc.title("Tic Tac Toe")
sc.bgcolor('cyan')
def coss():
    turtle.speed(5)
    turtle.pendown()
    turtle.right(135)
    turtle.forward(100*(2)**(1/2))
    turtle.penup()
    turtle.left(135)
    turtle.forward(100)
    turtle.left(135)
    turtle.pendown()
    turtle.forward(100*(2)**(1/2))
    turtle.penup()
    turtle.setposition(0,0)
    turtle.right(135)

def cir():
    turtle.speed(5)
    turtle.circle(50)
    turtle.penup()
    turtle.setposition(0,0)

def design():
    turtle.speed(10)
    turtle.penup()
    turtle.setposition(-150,150)
    turtle.pendown()
    turtle.color('red')
    turtle.forward(300)
    turtle.backward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.backward(300)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(200)
    turtle.backward(300)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.backward(300)

turtle.penup()
turtle.setposition(0,300)
turtle.write("The Game only goes for 3 steps Max each player so far....", align="center")

Winner=[{0,1,2,3},{0,1,4,7},{0,1,5,9},{0,2,5,8},{0,3,6,9},{0,3,5,7},{0,4,5,6},{0,7,8,9}]

cro={"1":(-150,250),"2":(-50,250),"3":(50,250),"4":(-150,150),"5":(-50,150),"6":(50,150),"7":(-150,50),"8":(-50,50),"9":(50,50)}
circ={"1":(-50,200),"2":(50,200),"3":(150,200),"4":(-50,100),"5":(50,100),"6":(150,100),"7":(-50,0),"8":(50,0),"9":(150,0)}
cros=[]
circle=[]
used=cros+circle
design()

while True:
    try:
        turtle.penup()
        cross=turtle.textinput("Cross","1-9")

        used=cros+circle
        turtle.setposition(cro.get(cross))
        if int(cross) in used:
            turtle.penup()
            turtle.setposition(0,-300)
            turtle.write("{} is already used, better luck next time.".format(cross),align="center",font=20)
            y=turtle.textinput("It is already used", "press enter to close the game")
            if y=="":
                turtle.clear()
                turtle.write("Click once to close the game",align="center",font=20)
                turtle.exitonclick()
                break
            
        cros.append(int(cross))
        turtle.pendown()
        if len(cros)>3:
            turtle.penup()
            turtle.setposition(0,-200)
            turtle.write("OVER, You used all 3 steps",font=20,align="center")
            break
        coss()
        if cros in Winner:
            turtle.penup()
            turtle.setposition(0,-300)
            turtle.write("Cross wins",font=4)
            break
        

        turtle.penup()
        cirle=turtle.textinput("Circle","1-9")
        used=cros+circle
        circle.append(int(cirle))
        if int(cirle) in used:
            turtle.penup()
            turtle.setposition(0,-300)
            turtle.write("{} is already used, better luck next time.".format(cirle))
            y=turtle.textinput("It is already used", "press enter to close the game")
            if y=="":
                turtle.clear()
                turtle.write("Click once to close the game")
                turtle.exitonclick()
                break
        turtle.setposition(circ.get(cirle))
        turtle.pendown()
        cir()

        if circle in Winner:
            turtle.penup()
            turtle.setposition(0,-300)
            turtle.write("Circle wins",font=4)
            break
            
        if len(circle)>3:
            turtle.penup()
            turtle.setposition(0,-200)
            turtle.write("TIED",font=20,align="center")
            break
    except ValueError:
        pass
    except TypeError:
        pass
turtle.exitonclick()
