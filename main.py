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
