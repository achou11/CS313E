# File: Queens.py
# Description: Program solves Queens Problem for any size board greater than 4x4.
# Student's Name: Andrew Chou
# Student's UT EID: aoc349
# Course Name: CS 313E 
# Unique Number: 51320

# Date Created: 11/6/16
# Date Last Modified: 11/11/16

class QueensProblem():
    #Initialize the board
    def __init__ (self, num):
        self.board = []
        self.dim = num
        self.solutionCount = 0
        self.distinct = []
    
    

        for i in range (self.dim):
            row = []
            for j in range (self.dim):
                row.append('*')
            self.board.append(row)
      
     
    def __str__(self):
    
        stringBoard = ""
        
        for row in self.board:
            row_string = ""
            for col in row:
                row_string += col + "  "
            row_string += "\n"
            stringBoard += row_string
      
        return stringBoard
    
    
    #Method to determine whether certain coordinate on board is "safe"
    def isValidPlace(self, row, col):
    
        #Check horizontal and vertical paths
        for i in range (self.dim):
            if (self.board[row][i] == 'Q' or self.board[i][col] == 'Q'):
                return False
        
        #Check diagonal paths
        for i in range (self.dim):
            for j in range (self.dim):
                rowDiff = abs (row - i)
                colDiff = abs (col - j)
                if (rowDiff == colDiff) and (self.board[i][j] == "Q"):
                    return False
        return True


    #Method to find all solutions for n x n board
    def solve(self, n):

        if (n == self.dim):

            self.solutionCount += 1
            print("Solution #{}".format(self.solutionCount))
            print(self)
            print()
         
        else:
            for i in range (self.dim):
                if (self.isValidPlace(i,n)):
                    self.board[i][n] = "Q"
                    self.solve(n + 1)
                    self.board[i][n] = "*"

      
def main():

    print() 
    
    #Get board size from user
    dim = eval(input("Enter the size of the square board: "))
      
    while dim < 4:
        print("Invalid input.")
        dim = eval(input("Enter the size of the square board: "))
      
    print()
    
    queens = QueensProblem(dim)
    queens.solve(0)

    
main()
