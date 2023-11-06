#!/usr/bin/env python
# coding: utf-8

# In[8]:


class NQueenSolver:
    
    def __init__(self,N,x,y):
        self.N = N
        self.x = x
        self.y = y
        self.ld = [0] * (2*N-1)
        self.rd = [0] * (2*N-1)
        self.cl = [0] * N
        
    def printSolution(self,board):
        print("\nN-Queen Backtracking Solution")
        print("Given initial position : row - ",self.x," , column - ",self.y)
        for i in range(N):
            for j in range(N):
                print(board[i][j],end=" ")
            print()
            
    def solveNQueen(self,board,col):
        if col>= self.N:
            return True
        if col == self.y:
            return self.solveNQueen(board,col+1)
        for i in range(N):
            if i==self.x:
                continue
            if (self.ld[i-col + self.N-1] != 1 and self.rd[i+col] != 1) and self.cl[i] !=1:
                board[i][col]=1
                self.ld[i-col + self.N-1] = self.rd[i+col] = self.cl[i] = 1
                if self.solveNQueen(board, col+1):
                    return True
                board[i][col]=0
                self.ld[i-col + self.N-1] = self.rd[i+col] = self.cl[i] = 0
        return False
    
    def solve(self):
        board = [[0 for i in range(self.N)]for j in range(self.N)]
        board[self.x][self.y]=1
        self.ld[self.x - self.y + self.N-1 ] = self.rd[self.x + self.y] = self.cl[self.x] = 1
        if not self.solveNQueen(board,0):
            print("Solution does not exist")
            return False
        self.printSolution(board)
        return True


# In[9]:


while True:
    print("\nN-Queen Backtracking Solver :")
    print("1. Solve N-Queens")
    print("2. Exit")
    choice = input("Enter your choice : ")
    if choice == "1":
        N = int(input("Enter the size of the chessboard (N): "))
        x = int(input("Enter the row for the initial position of the 1st queen     : "))
        y = int(input("Enter the column for the initial position of the 1st queen  : "))
        if x < 0 or x >= N or y < 0 or y >= N:
            print("Invalid initial queen position. Try again.")
        else:
            NQBt=NQueenSolver(N, x, y)
            NQBt.solve()
    elif choice == "2":
        print("Exiting..........")
        break
    else:
        print("Invalid choice. Please enter 1 or 2.")

