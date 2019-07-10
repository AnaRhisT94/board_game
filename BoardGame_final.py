def board(row,column,red_locs,green_locs):
    # g represents number of green pieces in coordinate (i,j)
    # r represents number of red pieces in coordinate (i,j)
    g=[[0] * column for i in range(row)]
    r=[[0] * column for i in range(row)]
    #Count the number of pieces of red and green both in coordinate (i,j)
    for rd,rd1 in red_locs:
        r[rd][rd1]=r[rd][rd1]+1 #Counter will count each time red locs repeat the coordinate
    for gd,gd1 in green_locs:
        g[gd][gd1]=g[gd][gd1]+1
    #print(r)
    return r,g #Return a tuple 0 for r and 1 for g
def find_best_coordinates(board, max_red):
   # gcount represents number of green pieces in rectangle (0,0) to (i,j)
   # rcount represents number of red pieces in rectangle (0,0) to (i,j)
    width=len(board[0][0])
    height=len(board[0])
    gcount=[[0] * width for i in range(height)]
    rcount=[[0] * width for i in range(height)]
    best_coordinate=(0,0)
    #Initialize Gmax which is maximum Green pieces in (i,j)
    GMax=0
    best_coordinate=(None,None)
    for i in range(height):
        for j in range(width):
      
            for k in range (i+1):
                for l in range (j+1):
                  rcount[i][j]=rcount[i][j]+board[0][k][l]
                  gcount[i][j]=gcount[i][j]+board[1][k][l]
            if rcount[i][j]==max_red and gcount[i][j]>GMax:
                GMax=gcount[i][j]
                best_coordinate=(i,j)
    #print(rcount)
    #print(gcount)
    return best_coordinate
def test_board():
#Example 1
    print("Testing 3x1 board...")
    red_locs= [(0,0), (1,0), (2,0)]
    green_locs = [(1,0), (2,0)]
    vboard= board(3, 1,red_locs, green_locs)
    #print(vboard)
    max_red=2
    best=find_best_coordinates(vboard,max_red)
    print("The best coordinate is ")
    print(best)
#Example 2
    print("Testing 5x3 board...")
    red_locs= [(0,0), (1,0), (2,0),(2,2),(2,1),(2,1)]
    green_locs = [(1,0), (2,0)]
    vboard= board(5, 3,red_locs, green_locs)
    #print("The 2D Board having MXN matrix of Red count tuple with MXN matrix of Green Count is")
    #print(vboard)
    max_red=5
    best=find_best_coordinates(vboard,max_red)
    print("The best coordinate is ")
    print(best)
#Example 3
    print("Testing 10,000 x 3 board...")
    red_locs = [(9000, 0), (1200, 2), (5000, 1)]
    vboard = board(10000, 3, red_locs, green_locs)
    best=find_best_coordinates(vboard, 2)
    print(best)

#Test Case Usage Example
    print("Testing 2x2 board...")
    red_locs = [(0,0), (1,1), (1,1)]
    green_locs = [(0,0), (0,1), (1,0)]
    vboard = board(2, 2, red_locs, green_locs)
    print("The 2D Board having MXN matrix of Red count tuple with MXN matrix of Green Count is")
    print(vboard)

    best=find_best_coordinates(vboard,1)
    print("The best coordinate is red_max=1 ")
    print(best)
    best=find_best_coordinates(vboard,2)
    print("The best coordinate is red_max=2")
    print(best)
    best=find_best_coordinates(vboard,3)
    print("The best coordinate is red_max=3")
    print(best)


test_board()


