
import numpy as np
grid =[[0,9,0,1,0,0,0,0,0],[0,0,3,0,0,6,0,0,7],[8,0,0,0,0,0,0,2,5],[0,7,0,0,6,0,0,0,9],[0,0,0,7,0,4,0,0,0],[2,0,0,0,3,0,0,6,0],[9,5,0,0,0,0,0,0,8],[7,0,0,5,0,0,3,0,0],[0,0,2,0,0,9,5,7,0]]
print(np.matrix(grid))
def possible(x,y,n):
    global grid
    #print("yoooo")
    for i in range(0,9):
        if grid[x][i] == n:
            return False

    for j in range(0,9):
        if grid[j][y] == n:
            # flag = False# print( 'False')
            # print('flag2')
            return False

    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range (0,3):
        for j in range(0,3):
            if grid[x0 + i][y0 + j]==n:
                # flag = False
                # print('flag3')
                return False # print( 'False')
    # print('flag4')
    return True # print('True')

# possible(0,0,9)
print (grid[2][8])

def solve():
    global grid
    #print("heyy")
    for x in range(9):
        for y in range(9):
            if grid[x][y]==0:
                for n in range (1,10):
                    if possible(x,y,n):
                        grid[x][y] = n

                        solve()
                        grid[x][y] = 0
                return
    print(np.matrix(grid))
    input('another answer?')

solve()

