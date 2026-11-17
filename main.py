Web VPython 3.2
box(pos=vec(5, 0, 0), length=3, height=0.5 , width=3, color=color.blue)
cylinder(pos=vec(5, 0, 0), axis=vec(0, 1, 0), color=color.white)
b = box (pos=vec(0, 1, 0),size=vec(2,2,2),texture = "https://static.wikia.nocookie.net/chiikawa/images/9/93/TastyKurimanju.png/revision/latest/thumbnail/width/360/height/450?cb=20241009083145&path-prefix=ko")
while True :
    rate(100)
    k = keysdown()
    if 'd' in k : 
        b.pos.x = b.pos.x + 0.1
    if 's' in k : 
        b.pos.y = b.pos.y + -0.1
    if 'w' in k : 
        b.pos.y = b.pos.y + 0.1
    if 'a' in k : 
        b.pos.x = b.pos.x + -0.1

20261116

Web VPython 3.2

box(pos=vec(5, 0, 0), length=3, height=0.5, width=3, color=color.blue)

c = cylinder(pos=vec(5, 0, 0), axis=vec(0, 1, 0), color=color.white)

b = sphere(pos=vec(0, 1, 0), size=vec(2, 2, 2),
           texture="https://static.wikia.nocookie.net/chiikawa/images/9/93/TastyKurimanju.png/revision/latest/thumbnail/width/360/height/450?cb=20241009083145&path-prefix=ko")

box(texture="https://i.postimg.cc/W1f7KffN/86c746ef4de6d4282636fc56b1194277-thumb-w1920.webp",
    pos=vec(0, 0, -3), size=vec(40, 30, 1))

colors = [color.white, color.red, color.blue, color.green]

def move(x, y):
    b.pos.x = b.pos.x + x
    b.pos.y = b.pos.y + y

def check():
    if abs(mag(c.pos - b.pos)) < 1:
        c.color = color.yellow
    else:
        c.color = color.white


while True:
    rate(100)
    k = keysdown()

    if 'd' in k:
        move(0.1, 0)
    if 's' in k:
        move(0, -0.1)
    if 'w' in k:
        move(0, 0.1)
    if 'a' in k:
        move(-0.1, 0)

    if '1' in k:
        b.color = colors[0]
    if '2' in k:
        b.color = colors[1]
    if '3' in k:
        b.color = colors[2]
    if '4' in k:
        b.color = colors[3]
        
        check()

20261117

Web VPython 3.2
box(pos=vec(5, 0, 0), length=3, height=0.5, width=3, color=color.blue)

c = cylinder(pos=vec(5, 0, 0), axis=vec(0, 1, 0), color=color.white)

b = sphere(pos=vec(0, 1, 0), size=vec(2, 2, 2),
           texture="https://static.wikia.nocookie.net/chiikawa/images/9/93/TastyKurimanju.png/revision/latest/thumbnail/width/360/height/450?cb=20241009083145&path-prefix=ko")

box(texture="https://i.postimg.cc/W1f7KffN/86c746ef4de6d4282636fc56b1194277-thumb-w1920.webp",
    pos=vec(0, 0, -3), size=vec(40, 30, 1))

colors = [color.white, color.red, color.blue, color.green]

while True:
    rate(100)
    k = keysdown()

    if 'd' in k:
        b.pos.x += 0.1
    if 'a' in k:
        b.pos.x -= 0.1
    if 'w' in k:
        b.pos.y += 0.1
    if 's' in k:
        b.pos.y -= 0.1

    if '1' in k:
        b.color = colors[0]
    if '2' in k:
        b.color = colors[1]
    if '3' in k:
        b.color = colors[2]
    if '4' in k:
        b.color = colors[3]

    if abs(mag(c.pos - b.pos)) < 1:
        c.color = b.color
    else:
        c.color = color.white


