import numpy as np
class Board(object):    
    """
    Initialize board with green and red points for any cell.
    Find the rectangle that has the highest number of green points with
    constraint the required maximum red points
    """
    def __init__(self, height, width, red_locs, green_locs):
        self.width = width
        self.height = height
        self.red_locs = red_locs
        self.green_locs = green_locs
        self.board = self.init_board(height,width, red_locs, green_locs)
        print("The red and green locs are")
        print(red_locs)
        print(green_locs)
    def init_board(self, row, column, red_locs, green_locs):
        # g represents number of green pieces in coordinate (i,j)
        # r represents number of red pieces in coordinate (i,j)
        g=np.zeros((row, column))
        r=np.zeros((row, column))
        #print(r,g)
        #Count the number of pieces of red and green both in coordinate (i,j)
        for x,y in red_locs:
            r[x][y]=r[x][y]+1 #Counter will count each time red locs repeat the coordinate
        for x,y in green_locs:
            g[x][y]=g[x][y]+1
        #print(r)
        #print(g)
        return r,g #Return a tuple 0 for r and 1 for g
    def find_best_coordinates(self, max_red):
       # gcount represents number of green pieces in rectangle (0,0) to (i,j)
       # rcount represents number of red pieces in rectangle (0,0) to (i,j)
        #board = self.board
        gcount=np.zeros((self.height,self.width))#.reshape((width, height))
        rcount=np.zeros((self.height,self.width))
        #print(rcount,gcount)
        best_coordinate=(None,None)
        green_max = 0
        #print(self.height,self.width)
        for i in range(self.height):
            for j in range(self.width):
                        # If we're in [0][0]
                      if i is 0 and j is 0:
                          rcount[i][j] = self.board[0][i][j]
                          gcount[i][j] = self.board[1][i][j]
                          #print (i,j,rcount[i][j], gcount[i][j])
                      # If we're in first line
                      elif i is 0 and j is not 0:
                          rcount[i][j]=rcount[i][j-1]+self.board[0][i][j]
                          gcount[i][j]=gcount[i][j-1]+self.board[1][i][j]
                          #print (i,j,rcount[i][j], gcount[i][j])

                      else:
                          
                          rr=0# Defined variable to count the red pieces from (i,0) to (i.j) for i>1
                          gg=0# Defined variable to count the green pieces from (i,0) to (i.j) for i>1
                          
                          for p in range(j):
                              rr+=self.board[0][i][p]
                              gg+=self.board[1][i][p]
                          rcount[i][j]=rcount[i-1][j]+rr+ self.board[0][i][j]
                          gcount[i][j]=gcount[i-1][j]+gg+self.board[1][i][j]

                      # If we achieve max_red here, we store maximum green points           
                      if rcount[i][j] <= max_red and green_max < gcount[i][j]:
                          green_max = gcount[i][j]
                          best_coordinate=(i,j)
        print("The rcount and gcount Matrix are:")
        print(rcount)
        print(gcount)
        return best_coordinate
def test_board():
#Example 1
    print("Example 1:")
    print("Testing 3x1 board...")
    red_locs= [(0,0), (1,0), (2,0)]
    green_locs = [(1,0), (2,0)]
    board= Board(3, 1, red_locs, green_locs)
    max_red=2
    best = board.find_best_coordinates(max_red)
    print("The best coordinate for max_red=2 is ")
    print(best)
#Example 2
    print ("Example 2:")
    print("Testing 5x3 board...")
    red_locs= [(0,0), (1,0), (2,0),(2,2),(2,1),(2,1)]
    green_locs = [(1,0), (2,0)]
    board= Board(5, 3,red_locs, green_locs)
    #print("The 2D Board having MXN matrix of Red count tuple with MXN matrix of Green Count is")
    max_red=5
    best=board.find_best_coordinates(max_red)
    print("The best coordinate is for max_red=5 is" )
    print(best)
#Example 3
    print ("Example 3:")
    print("Testing 10,000 x 3 board...")
    red_locs = [(9000, 0), (1200, 2), (5000, 1)]
    board = Board(10000, 3, red_locs, green_locs)
    best=board.find_best_coordinates(2)
    print("The best coordinate for max_red=2 is")
    print(best)

#Test Case Usage Example
    print ("Example 4:")
    print("Testing 2x2 board...")
    red_locs = [(0,0), (1,1), (1,1)]
    green_locs = [(0,0), (0,1), (1,0)]
    board = Board(2, 2, red_locs, green_locs)
    #The 2D Board having MXN matrix of Red count tuple with MXN matrix of Green Count
    print(board)

    best=board.find_best_coordinates(1)
    print("The best coordinate for max_red=1 ")
    print(best)
    best=board.find_best_coordinates(2)
    print("The best coordinate for max_red=2")
    print(best)
    best=board.find_best_coordinates(3)
    print("The best coordinate for max_red=3")
    print(best)
if __name__ == "__main__":
    test_board()
