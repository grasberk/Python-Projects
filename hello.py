
from random import randint

board = [[" " for _ in range(3)] for _ in range(3)]

# fill the board with random X                                                                                                                               
for i in range(5):
   board[randint(0,2)][randint(0,2)]  = "X"

# print the board                                                                                                                                            
[print(board[i]) for i in range(3)]
print()

# Get the column from the user                                                                                                                               
i = int(input("Enter a column to convert: "))

# TODO: Do the conversion and store it in a variable called vert
#[x,x,o]

vert=[]
for j in range(3):
   vert.append(board[j][i])


# Print the conversion                                                                                                                                       
print()
print(f"This is column {i}")
print(vert)
