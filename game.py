#print a board
#take in user input of 'X' or 'O'
#store user input in given location
#TODO: pretty board
#TODO: take row+column as one input


from random import randint

#create board
board=[
      [' ',' ',' '],
      [' ',' ',' '],
      [' ',' ',' ']
    ]
#set winner to false
winner=False
#create a board

def create_new_board():
    counter2=0
    for i in board: 
        counter=0
        for x in i:
            
            counter+=1
            print(x, end='')
            if(counter<3):
             print(end=' '+"|")
                
        print(" ")
        
        counter2+=1
        if(counter2<3):
            print("-------")
        
 

#AI
#TODO: if there is horizontal line with two same value and empty space play your piece
#TODO: if there is Vertical line with two same value and empty space play your piece
#TODO: if there is diagonal line with two same value and empty space play your piece
#TODO: if it doesnt fall into any of the above categories play random
#Write me a function that takes a list, i.e. [' ', 'X', ' '] and returns True if it contains an empty space and false otherwise
# Instead of iterating over the elements in a list, iterate over the positions in the board.
def check_space(list1):
        
    for i in list1:
        if (i==" "):
            return True
        
    return False

def check_for_twins(list1):
    for i in range(3):
        for j in range(i+1,3):
            if list1[i]==list1[j] and list1[i]!=" ":
                return True
def computer( ):
#horizontal win
    horizontal_check()
    
    
    def random_move():
        row=randint(0,2)
        column=randint(0,2)
        while board[row][column]!=" ":
            row=randint(0,2)
            column=randint(0,2)
        board[row][column]="O"
            
#horizontal
#vertical
#diagianl


    
    
            
        
    random_move()
def create_row():
    row=[]
    for j in range(3):
        row.append(board[j][i])
        return row
    

#horizontal function
def horizontal_check(row):
    if check_space(row)==True and check_for_twins(row)==True:
        for i in range(3):
            if(row[i]==" "):               
                return i

#vertical wins
def vertical_twins():
    #[0][0]-[1][0]-[2][0]
    #[0][0]-[0][1]-[0][2]


    pass

            
    
    

#diagonal wins
    



#check for winner
def check_winner(symbol):
#horizontal wins

    if board[0][0]==symbol and board[0][1]==symbol and board[0][2]==symbol:
        
        return True
    
    
    if board[1][0]==symbol and board[1][1]==symbol and board[1][2]==symbol:
        return True
    
    
    if board[2][0]==symbol and board[2][1]==symbol and board[2][2]==symbol:
        return True
  
    
    
#vertical wins
    if board[0][0]==symbol and board[1][0]==symbol and board[2][0]==symbol:
        return True
    
    if board[0][1]==symbol and board[1][1]==symbol and board[2][1]==symbol:
        return True
    
    
    if board[0][2]==symbol and board[1][2]==symbol and board[2][2]==symbol :
        return True
    
    
#diagonal wins
    if board[0][0]==symbol and board[1][1]==symbol and board[2][2]==symbol :
        return True
    
        
    if board[0][2]==symbol and board[1][1]==symbol and board[2][0]==symbol:
       return True
   
    

#single user input
def user_input():
    user=input("enter row and column")
    row=int(user[0])
    column=int(user[1])
    return row, column




while winner==False:
 
    #player1
    
    value=user_input()
    board[value[0]][value[1]]='X'
    create_new_board()
    #check for winner
    if check_winner('X')==True:
        print("player 1 won!")
        break
    
        
    
        
     #player2
   # value=user_input()
    #board[value[0]][value[1]]='O'
    #create_new_board()
    #check for winner
   # if check_winner('O')==True:
    #    print("player 2 won!")
    #    break

     #computer
    #random_move()
    computer()
    if check_winner('O')==True:
        print("Computer won!")
        create_new_board()
        break
    print("      ")
    create_new_board()
    print("      ")
    print("      ")
    print("      ")
