input_A = "ACS\nBDS\nDCS"
input_B = "AB\nCD"


class LoopOver:

    def __init__(self, string1, string2):
        # In list value i save all lines of input as lists with each elements of line
        # In variable size are exist size of matrix
        self.solution = []
        self.mixedUpBoard = []
        for line in string1.split('\n'):
            arr = []
            for sign in line:
                arr.append(sign)
            self.mixedUpBoard.append(arr)
        self.sizeA = len(arr)

        self.solvedBoard = []
        for line in string2.split('\n'):
            arr = []
            for sign in line:
                arr.append(sign)
            self.solvedBoard.append(arr)
        print(self.mixedUpBoard)
        # print(self.solvedBoard)

    def find_solution(self):
        output = []
        # particular solution for size = 2
        if self.size == 2:
            output.append()
            # find something

        return output

    def find_first_line(self):
        output = []
        return 0

    def left(self, n):
        self.mixedUpBoard[n] = self.mixedUpBoard[n][1:] + self.mixedUpBoard[n][:1]
        self.solution.append("L{}".format(n))

    def right(self, n):
        self.mixedUpBoard[n] = self.mixedUpBoard[n][-1:] + self.mixedUpBoard[n][:-1]
        self.solution.append("R{}".format(n))


a = LoopOver(input_A, input_B)
a.right(0)
print(a.solution)
print(a.mixedUpBoard)


'''
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
'''