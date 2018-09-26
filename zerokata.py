from turtle import *
ch=Pen()
ch.speed('fastest')

setup(600,600)
bgcolor('black')
ch.pensize(10)
ch.pencolor('red')
def cto(x,y):  #for moving cursor without drawing
	ch.up()
	ch.goto(x,y)
	ch.down()

cto(-100,290)
ch.goto(-100,-290)
cto(100,290)
ch.goto(100,-290)
cto(-290,100)
ch.goto(290,100)
cto(-290,-100)
ch.goto(290,-100)
#def tellpos(x,y):
#	print(x,y)
def zero(x,y):
	cto(x,y)
	ch.color("green")
	ch.circle(50)
def kata(x,y):
	ch.pencolor('yellow')
	ch.up()
	ch.goto(x+20,y+20)
	ch.down()
	ch.goto(x-20,y-20)
	ch.up()
	ch.goto(x-20,y+20)
	ch.down()
	ch.goto(x+20,y-20)

kiskibari = 0

def bari(x,y):
    global kiskibari
    if kiskibari%2==0:
        zero(x,y)
    else:
        kata(x,y)

    kiskibari+=1

onscreenclick(bari)
done()