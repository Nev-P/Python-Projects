import random
# Rock Paper Scissors

# Step 1> Tell the players the rules
# Step 2> give them their choices
def Intro():
    print("===================================================")
    print("I'm bored...Let's play rock, paper, scissors, Lizard, and Spock!")
    print("Type Rock, Paper, or Scissors.")
    print("Rock beats Scissors.")
    print("Scissors beats Paper.")
    print("Paper beats Rock.")
    print("Lizard beats Spock")
    print("Paper beats Spock")
    print("Spock beats rock")
    print("Spock beats Scissors")
    print("Rock beats Lizard ")
    print("Lizard beats Spock")
    print("Lizard beats Paper")
    print("Scissors beats lizard")
    print("==================================================")

Intro()
# Step 3> Players choose their moves
def playerTurn():
    print(" Type: Lizard, Spock, Rock, Paper, or Scissors")
    return input("Please select your option >>")
while temp.lower() != "rock" and temp != "paper" and temp != "scissors":
    temp = input("invalid number, try again >>")
    print("Your Move" + temp)
    
    return temp

playerChoice = playerTurn()
print(playerChoice)

def cpuTurn():
    print("=========== CPU TURN =========")
    return random.choice(["rock", "paper", "scissors"])

# Repeating a function
gameOver = None
playerScore = 0
CPUScore = 0
while gameOver != "n":
    playerChoice = playerTurn()
    cpuChoice = cpuTurn()

# Step 4> Players show their chooses
print("CPU's Move:" + cpuChoice)

# Step 5> Results of the match is determined
print("====== RESULTS ===============")

if playerChoice == cpuChoice:
    print("You and I have tied!")
elif playerChoice == "rock":
    if cpuChoice == "scissors":
        print("You have won with rock!")
        playerScore += 1
elif playerChoice == "paper":
    if cpuChoice == "scissors":
        print("I have won with scissors!")
        CPUScore += 1
elif playerChoice == "scissors":
    if cpuChoice == "paper":
        print("You have won with scissors!")
        CPUScore += 1
elif playerChoice == "scissors":
    if cpuChoice == "rock":
        print("I have won with rock!")
        CPUScore += 1
elif playerChoice == "Spock":
    if cpuChoice == "Lizard":
        print("You won with Lizard!")
        playerScore += 1
elif playerChoice == "Lizard":
    if cpuChoice == "Spock":
        print("I won with Lizard!")
        CPUScore += 1
elif playerChoice == "Paper":
    if cpuChoice == "Spock":
        print("You won with paper!")
        playerScore += 1
elif playerChoice == "Spock":
    if cpuChoice == "Paper":
        print("I won with paper!")
        CPUScore += 1
elif playerChoice == "Spock":
    if cpuChoice == "Scissors":
        print("You won with Spock!")
        playerScore += 1
elif playerChoice == "Spock":
    if cpuChoice == "Scissors":
        print("I won with Spock!")
        CPUScore += 1
elif playerChoice == "rock":
    if cpuChoice == "Spock":
        print("I won with Spock!")
        CPUScore += 1
elif playerChoice == "Spock":
    if cpuChoice == "rock":
        print("You won with Spock!")
        playerScore += 1
elif playerChoice == "Lizard":
    if cpuChoice == "rock":
        print("I won with Rock")
        CPUScore += 1
elif playerChoice == "Rock":
    if cpuChoice == "Lizard":
        print("You won with Rock!")
        playerScore += 1
elif playerChoice == "Lizard":
    if cpuChoice == "paper":
        print("You won with Lizard!")
        playerScore += 1
elif playerChoice == "paper":
    if cpuChoice == "Lizard":
        print("I won with Lizard!")
        CPUScore += 1
elif playerChoice == "Scissors":
    if cpuChoice == "Lizard":
        print("You won with Scissors!")
        playerScore += 1
elif playerChoice == "Lizard":
    if cpuChoice == "Scissors":
        print("I won with Scissors!")
        CPUScore += 1
elif playerChoice == "rock":
    if cpuChoice == "paper":
        print("You have won with paper!")
        playerScore += 1
    else:
        print("I have won with Paper!")
        CPUScore += 1

print("CPU's Current Score" + str(CPUScore))
print("Player's Current Score: " + str(playerScore))
gameOver = input("Do yu wnt to play again? Type 'n' or type in another choice.")

