# Program 1: Number Sorter
# Create a program that ask 4 numbers. 
# Print the 4 numbers from highest to lowest using only if-else statement.

def userInputs():
    firstInput = float(input("Enter 1st number: "))
    secondInput = float(input("Enter 2nd number: "))
    thirdInput = float(input("Enter 3rd number: "))
    fourthInput = float(input("Enter 4th number: "))
    return firstInput, secondInput, thirdInput, fourthInput

order = userInputs()

# I followed the tournament system where i make them compete with each other first then
# Compare the winners and losers to each other in order to find the order

# First Round
if order[0] >= order[1]:
    matchOneWin = order[0]
    matchOneLose = order[1]
else:
    matchOneWin = order[1]
    matchOneLose = order[0]
if order[2] >= order[3]:
    matchTwoWin = order[2]
    matchTwoLose = order[3]
else:
    matchTwoWin = order[3]
    matchTwoLose = order[2]

# Check if the loser on either match is actually higher than the winner on either match
if matchOneWin <= matchTwoLose:
    finalistOne = matchTwoLose
    loserOne = matchOneWin
else:
    finalistOne = matchOneWin
    loserOne = matchTwoLose
if matchTwoWin <= matchOneLose:
    finalistTwo = matchOneLose
    loserTwo = matchTwoWin
else:
    finalistTwo = matchTwoWin
    loserTwo = matchOneLose

# Check who will be the fourth and third
if loserOne >= loserTwo: 
    third = loserOne
    fourth = loserTwo
else:
    third = loserTwo
    fourth = loserOne

#Finals
if finalistOne >= finalistTwo:
    first = finalistOne
    second = finalistTwo
else:
    first = finalistTwo
    second= finalistOne

# Print the order from highest to lowest
list = [first,second,third,fourth]
print(list)