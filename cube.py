#defined matrices for each cube face
global whiteFace, yellowFace, greenFace, blueFace, redFace, orangeFace

whiteFace = [['w00','w01','w02'],
             ['w10','w11','w12'],
             ['w20','w21','w22']]

greenFace = [['g00','g01','g02'],
             ['g10','g11','g12'],
             ['g20','g21','g22']]

blueFace  = [['b00','b01','b02'],
             ['b10','b11','b12'],
             ['b20','b21','b22']]

yellowFace = [['y00','y01','y02'],
              ['y10','y11','y12'],
              ['y20','y21','y22']]

redFace = [['r00','r01','r02'],
           ['r10','r11','r12'],
           ['r20','r21','r22']]

orangeFace = [['o00','o01','o02'],
              ['o10','o11','o12'],
              ['o20','o21','o22']]
emptyFace = [[' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']]

def render():
    
    print("GreenFace : ")
    for row in greenFace:
        print(row)
    print("whiteFace : ")
    for row in whiteFace:
        print(row)
    print("BlueFace : ")
    for row in blueFace:
        print(row)
    print("YellowFace : ")
    for row in yellowFace:
        print(row)
    print("RedFace : ")
    for row in redFace:
        print(row)
    print("OrangeFace : ")
    for row in orangeFace:
        print(row)      

def L(n):
    for counter in range(n):
        for i in range(3):
            emptyFace[i][0] = whiteFace[i][0]
            whiteFace[i][0] = blueFace[i][0]
            blueFace[i][0] = yellowFace[i][0]
            yellowFace[i][0] = greenFace[i][0]
            greenFace[i][0] = emptyFace[i][0]

def D(n):
    for counter in range(n):
        for i in range(3):
            emptyFace[2][2-i] = greenFace[2][2-i]
            greenFace[2][i] = orangeFace[i][0]
            orangeFace[i][0] = blueFace[0][2-i]
            blueFace[0][i] = redFace[i][2]
            redFace[i][2] = emptyFace[2][2-i]

def B(n):
    for counter in range(n):
        for i in range(3):
            emptyFace[0][i] = whiteFace[0][i]
            whiteFace[0][i] = redFace[0][i]
            redFace[0][i] = yellowFace[2][2-i]
            yellowFace[2][2-i] = orangeFace[0][i]
            orangeFace[0][i] = emptyFace[0][i]


