input_ = "ABCDEFGHI".replace('\n', '')
s = 0
m = []

for i in range(3):
    a = []
    for j in range(3):
        a.append(input_[s])
        s+=1
    m.append(a)


def right(n):
    m[n][0], m[n][1], m[n][2] = m[n][2], m[n][0], m[n][1]


def left(n):
    m[n][0], m[n][1], m[n][2] = m[n][1], m[n][2], m[n][0]


def up(n):
    m[0][n], m[1][n], m[2][n] = m[1][n], m[2][n], m[0][n]


def down(n):
    m[0][n], m[1][n], m[2][n] = m[2][n], m[0][n], m[1][n]

def output_m(mass):
    for i in range(3):
        print()
        for j in range(3):
            print(mass[i][j], end=' ')
