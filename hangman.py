#TODO: create number of wrong guesses
#TODO: create the board for hangman 
#TODO: checker to see if letter exists or not/guess counter

#TODO: if letter is added cant pick same letter again

from random import randint

def read_input():
    file=open('words.txt','r')
    f=file.readlines()

    new_list=[]
    for line in f:
        x="-"
        if x in line: 
            continue

        if line[-1]=='\n':
            new_list.append(line[:-1])
        
        else: 
         new_list.append(line)

    return new_list
guess=input("How many incorrect guesses do you want to allow? ")
new_list=read_input()
answer="hello"
#answer=new_list[randint(0,len(new_list)-1)]
board=[ ]
counter=0



for x in range(len(answer)):
    
    board.append("_ ")
   # print(" ")

def print_board():
    for x in range(len(answer)):
        print(board[x], end=" ")
#TODO: If the user inputs more than one character for their guess, tell them it's an invalid input and make them enter again

   
def input_validation():
    valid=False
    while valid==False: 
        user_input=input("What is your guess: ")
        if len(user_input)==1:
            return


def check_winner():
    x="_ "
    y=x in board
    if x in board:
        return False
    else:
        return True

    

  
print_board()
while counter<int(guess):
    

    user_input=input("What is your guess: ")
    if user_input in answer:
        for i in range(len(answer)):
            if user_input==answer[i]:
                board[i]=user_input
           
    else:
        counter+=1
    
    
    if check_winner()==True:
        print(f"Winner! The word was {answer}")
        exit()
        


    
    
        
    print_board()

if check_winner()==False:
        print(f"You Lose! the word was {answer}")

    
            

        

        
        
        

        