#TODO: create user input for number of rounds
#TODO: take user input rock rock,paper,scissors
#TODO: chose computers input radomize
#TODO: determine winner (cyclical,modulus)


from random import randint

rounds= input("How many rounds would you like to play: ")
print(" ")
human_wins=0
computer_wins=0

while human_wins <= int(rounds)/2 and computer_wins <= int(rounds)/2:
    player=input("Would you like to play rock(r), paper(p) or scissors(s): ")


    if player=="r":
        ans=0
    if player=="p":
        ans=1
    if player=="s":
        ans=2
    #rock gets beat by paper, gets beat by scissor, gets beat by rock



    comp_ans=randint(0,2)
    if comp_ans==0:
        print("Computer picked rock")
    if comp_ans==1:
        print("Computer picked paper")
    if comp_ans==2:
        print("Computer picked scissors")

    
    #modulus
    if ans==(comp_ans+1)%3:
        
        human_wins+=1
        print("Player wins")
        print(" ")
    elif ans==comp_ans:
        print("It is a tie")
        print(" ")
    else: 
        computer_wins+=1
        print("Computer wins")
        print(" ")

        


print(f"Player1's score is {human_wins} and Computer's score is {computer_wins}")