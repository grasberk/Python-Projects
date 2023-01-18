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
board2=[]
board3=[]
board4=[]
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

        

def rotate_board():
    global board2
    column_one=[board[0][0],board[1][0],board[2][0]]
    column_two=[board[0][1],board[1][1],board[2][1]]
    column_three=[board[0][2],board[1][2],board[2][2]]
    board2=[column_one, column_two,column_three]


    



def check_space(list1):
        
    for i in list1:
        if (i==" "):
            return True
        
    return False

def check_for_twins(list1, letter):
    for i in range(3):
        for j in range(i+1,3):
            if list1[i]==list1[j] and list1[i]==letter:
                
                return True

#horizontal win checker function
def horizontal_check(row_list, letter):
    if check_space(row_list)==True and check_for_twins(row_list, letter)==True:
        for i in range(3):
            if(row_list[i]==" "):               
                return i

def random_move():
    row=randint(0,2)
    column=randint(0,2)
    while board[row][column]!=" ":
        row=randint(0,2)
        column=randint(0,2)
    board[row][column]="O"

#find vertical position and return horizontal values

def column_to_row(letter):
    j=0
    for elem in board2:
        value=horizontal_check(elem,letter)
        if value !=None:
            return (value,j)
            
        j+=1

#diagonals
def diagonal_check(letter):
    diagonal_up=[board[2][0],board[1][1],board[0][2]]
    diagonal_down=[board[0][0],board[1][1],board[2][2]]
    k=0
    
    value_up=horizontal_check(diagonal_up,letter)
    if value_up !=None:
        if value_up==2:
            k=0
        if value_up==1:
            k=1
        if value_up==0:
            k=2
        print(k)
        print(value_up)
        return (k,value_up)
    
    j=0
   
    value_down=horizontal_check(diagonal_down,letter)
    if value_down !=None:
        if value_down==2:
            j=2
        if value_down==1:
            j=1
        if value_down==0:
            j=0
        print(j)
        print(value_down)
        return (j,value_down)
    j+=1


def block_win(letter):
    for elem in board:
        value=horizontal_check(elem, letter)
        if value != None:
            elem[value]="O"
            return True
#block vertical win
    rotate_board()
    location=column_to_row(letter)
    if location !=None:
        x=location[0]
        y=location[1]
        board[x][y]="O"
        return True
#block diagonal wins
    diag_values=diagonal_check(letter)
    if diag_values!=None:
        x=diag_values[0]
        y=diag_values[1]
        board[x][y]="O"
        return True
    
def computer( ):
#only place O if comp can win otherwise check for matching X
    if block_win("O")==True:
        return
    if block_win("X")==True:
        return
#random move
    else:
        random_move()
        


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
    
    computer()
    create_new_board()

    #check for winner
    if check_winner('X')==True:
        print("player 1 won!")
        break

    if check_winner('O')==True:
        print("Computer won!")
        create_new_board()
        break
    
