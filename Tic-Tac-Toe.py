import random
# Steps in Order for Playing Tic-Tac-Toe

# Programming) Describing how to win
def intro():
    print("I'm Bored, let's play Tic-Tac-Toe")
    print("==================================================")
    print("board[0] + |  + board[1] +  |  + board[2]")
    print("---------")
    print("board[3] + | + board[4] + | + board[5]")
    print("---------")
    print("board[6] + | + board[7] + | + board[8]")
    print("Get 3 spots in a row to win!")
    print("===================================================")

intro()

# Step 1) Make the grid
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
def drawBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

# Step 2) State who's Circle and Who's X
gameSymbols = ["0","X"]
pSymbol = random.choice(gameSymbols)
gameSymbols.remove(pSymbol)
cpuSymbol = random.choice(gameSymbols)
print("The player has been assigned:" + pSymbol)
print("The CPU has been assigned:" + cpuSymbol)

# Step 3) Decide who goes first
player_turn = random.randint(0,1)
if player_turn == 0:
    print("You go first!")
    drawBoard()
else:
    print("I go first!")

# Step 4) Make your move
def playermove():
    print("Player, it's your turn.")
    temp = input("Please chose a space on the broad for your move >>")
    while not temp.isnumeric() or (int(temp) < 0 or int(temp) > 0) or board[int(temp)] != " ":
        temp = input("Please enter a valid number (0-8) >>")

    board[int(temp)] = pSymbol
    drawBoard()

# Step 5) Other player makes their move
def cpumove():
    print("It is my turn.")
    temp = random.randrange(0, 8)
    while board[int(temp)] != " ":
        temp = random.randrange(0, 8)
    board[int(temp)] = cpuSymbol
    drawBoard()

# Step 6) repeat steps 4 and 5 Until...
# Step 7) Someone wins

def winCheck(XOsymbol):
# Horiztional rows
    if board[0] == board[1] and board[1] == board[2] and board[0] == XOsymbol:
        return True
    elif board[3] == board[4] and board[4] == board[5] and board[3] == XOsymbol:
        return True
    elif board[6] == board[7] and board[7] == board[8] and board[6] == XOsymbol:
        return True
    # Vertical Rows
    elif board[0] == board[3] and board[3] == board[6] and board[0] == XOsymbol:
        return True
    elif board[1] == board[4] and board[4] == board[7] and board[1] == XOsymbol:
        return True
    elif board[2] == board[5] and board[5] == board[8] and board[2] == XOsymbol:
        return True
# Diagonal Rows
    elif board[0] == board[4] and board[4] and board[8] and board[0] == XOsymbol:
        return True
    elif board[2] == board[4] and board[4] == board[6] and board[2] == XOsymbol:
        return True
    else:
        return False

turns = 0
while turns < 9 and not winCheck(pSymbol) and not winCheck(cpuSymbol):
    if player_turn == 0:
        playermove()
        player_turn == 1
        if winCheck(pSymbol):
            print("You have won!")
    else:
        cpumove()
        player_turn = 0
        if winCheck(cpuSymbol):
            print("I have won!")

    turns += 1
    print("========================")

# Step 8) all turns have passed without a match. (a tie)
if not winCheck(pSymbol) and not winCheck(cpuSymbol):
    print("it is a tie! No one has won!")

# Play again? (write a function)
gameOver = None
playerScore = 0
CPUScore = 0
while gameOver != "n":
    playermove() = player_turn()
    cpumove() = cpu_turn()



