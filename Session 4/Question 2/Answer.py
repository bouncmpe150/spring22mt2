
height = int(input())
width = int(input())

board = []

for _ in range(height):
    board.append([int(x) for x in input().split(" ")])


# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

new_board = [[0] * width]

for _ in range(height - 1):
    new_board.append([0 for _ in range(width)])



for i in range(height):
    for j in range(width):
        if board[i][j] == 0:
            #print(i, j)
            if i > 0 and i < height - 1 and j > 0 and j < width - 1:
                new_board[i][j] = board[i-1][j-1] + board[i-1][j] + board[i-1][j+1] + board[i][j-1] + board[i][j+1] + board[i+1][j-1] + board[i+1][j] + board[i+1][j+1]
            # corners
            elif i == 0 and j == 0: # top left
                new_board[i][j] = board[i+1][j] + board[i][j+1] + board[i+1][j+1]
            elif i == height - 1 and j == width - 1: # bottom right
                new_board[i][j] = board[i - 1][j] + board[i][j - 1] + board[i - 1][j - 1]
            elif i == 0 and j == width - 1: # top right
                new_board[i][j] = board[i+1][j] + board[i][j-1] + board[i+1][j-1]
            elif i == height - 1 and j == 0: # bottom left
                new_board[i][j] = board[i-1][j] + board[i][j+1] + board[i-1][j+1]
            elif i == 0:
                new_board[i][j] = board[i][j-1] + board[i][j+1] + board[i+1][j-1] + board[i+1][j] + board[i+1][j+1]
            elif j == 0:
                new_board[i][j] = board[i - 1][j] + board[i - 1][j + 1] + board[i][j + 1] + board[i + 1][j] + board[i + 1][j + 1]
            elif i == height - 1:
                new_board[i][j] = board[i - 1][j - 1] + board[i - 1][j] + board[i - 1][j + 1] + board[i][j - 1] + board[i][j + 1]
            elif j == width - 1:
                new_board[i][j] = board[i - 1][j - 1] + board[i - 1][j] + board[i][j - 1] + board[i + 1][j - 1] + board[i + 1][j]



print(new_board)

# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE