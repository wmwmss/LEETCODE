# Find the pattern and complete the function:
# int[][] spiral(int n);
# where n is the size of the 2D array.
# n = 3
# 1 2 3
# 8 9 4
# 7 6 5

# n = 4
# 1  2  3  4
# 12 13 14 5
# 11 16 15 6
# 10 9  8  7

def spiral(n:int):
    # recursively fill the rows and columns
    spiral_array = [[0 for j in range(n)] for i in range(n)]
    num = 0
    # special case of n = 1
    if n == 1:
        spiral_array[0][0] = num + 1
        print(spiral_array[0])
        return

    def fill(x, y, n, num):
        print("num "+str(num))
        # start at x row, y column, n elements
        if n == 0: return
        if n == 1:
            #spiral_array[x][y] = num + 1
            return
        #fill the outer rows and columns
        print("iter "+str(n)+" num "+str(num))
        for i in range(n-x):
            num = num + 1
            spiral_array[x][y+i] = num
            print("("+str(x)+","+str(y+i)+") "+"num "+str(num))
        for i in range(n-1-y):
            num = num + 1
            spiral_array[x+i+1][n-1] = num
            print("("+str(x+i+1)+","+str(n-1)+") "+"num "+str(num))
        for i in range(n-1-x):
            num = num + 1
            spiral_array[n-1][n-i-2] = num
            print("("+str(n-1)+","+str(n-i-2)+") "+"num "+str(num))
        for i in range(1,n-1-y):
            num = num + 1
            spiral_array[n-i-1][y] = num
            print("("+str(n-i-1)+","+str(y)+") "+"num "+str(num))
        #print("iter "+str(n)+" num "+str(num))
        fill(x+1, y+1, n-1, num)

    fill(0, 0, n, num)
    for i in range(n):
        print(spiral_array[i])

n = 12
spiral(n)
