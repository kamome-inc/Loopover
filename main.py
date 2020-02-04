input_A = "URHTP\nWOQKS\nFCLYG\nBDIXJ\nVNEAM"
input_B = "ABCDE\nFGHIJ\nKLMNO\nPQRST\nUVWXY"


class LoopOver:

    def __init__(self, string1, string2):
        # In list value i save all lines of input as lists with each elements of line
        # In variable size are exist size of matrix
        self.solution = []
        self.mixedUpBoard = []
        self.solvedBoard = []
        for line in string1.split('\n'):
            arr = []
            for sign in line:
                arr.append(sign)
            self.mixedUpBoard.append(arr)
        self.length = len(arr)
        self.height = len(self.mixedUpBoard)

        for line in string2.split('\n'):
            arr = []
            for sign in line:
                arr.append(sign)
            self.solvedBoard.append(arr)
        # print(self.mixedUpBoard)
        # print(self.solvedBoard)

    def left(self, n):
        self.mixedUpBoard[n] = self.mixedUpBoard[n][1:] + self.mixedUpBoard[n][:1]
        self.solution.append("L{}".format(n))

    def right(self, n):
        self.mixedUpBoard[n] = self.mixedUpBoard[n][-1:] + self.mixedUpBoard[n][:-1]
        self.solution.append("R{}".format(n))

    def up(self, n):
        arr = []
        for line in self.mixedUpBoard:
            arr.append(line[n])
        arr = arr[1:] + arr[:1]
        i = 0
        for line in self.mixedUpBoard:
            line[n] = arr[i]
            i += 1
        self.solution.append("U{}".format(n))

    def down(self, n):
        arr = []
        for line in self.mixedUpBoard:
            arr.append(line[n])
        arr = arr[-1:] + arr[:-1]
        i = 0
        for line in self.mixedUpBoard:
            line[n] = arr[i]
            i += 1
        self.solution.append("D{}".format(n))

    def find_solution(self):
        # type something
        return 0

    def find_first_line(self):
        for sign in self.solvedBoard[0]:
            move_col, move_row = self.find_the_distance(sign)
            col, row = self.find_xy(sign, self.mixedUpBoard)

            # moving rows
            if move_col <= 0:
                for i in range(abs(move_col)):
                    self.left(row)
            if move_col > 0:
                for i in range(move_col):
                    self.right(row)

            move_col, move_row = self.find_the_distance(sign)
            col, row = self.find_xy(sign, self.mixedUpBoard)

            # moving cols
            if move_row <= 0:
                for i in range(abs(move_row)):
                    self.up(col)
            if move_row > 0:
                for i in range(move_row):
                    self.down(col)
        return 1

    def find_the_distance(self, sign):
        mixed_x, mixed_y = self.find_xy(sign, self.mixedUpBoard)
        solved_x, solved_y = self.find_xy(sign, self.solvedBoard)
        distance_x = solved_x - mixed_x
        distance_y = solved_y - mixed_y
        return distance_x, distance_y

    @staticmethod
    def find_xy(sign, matrix):
        # x as column, y as line
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if sign == matrix[y][x]:
                    return x, y
        raise ValueError("Find_xy: '{}' not found!".format(sign))

    def output(self):
        print("Mixed:")
        print("l = " + str(self.length) + " h = " + str(self.height))
        for line in self.mixedUpBoard:
            print(line)
        print("Solved:")
        for line in self.solvedBoard:
            print(line)


a = LoopOver(input_A, input_B)
a.output()
print(a.find_first_line())
a.output()
print(a.solution)


