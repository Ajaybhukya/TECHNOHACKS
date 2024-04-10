import random
def user_choice():
    choice=input("Enter your choice[rock, paper, scissor]:").lower()
    while choice not in ["rock","paper","scissor"]:
        print("invalid choice")
        choice=input("Enter your choice[rock, paper, scissor]:").lower()
    return choice 
def computer_choice():
    return random.choice(["rock","paper","scissor"])
def determine_winner(user_ch, computer_ch):
    if user_ch==computer_ch:
        return "Both are tied"
    elif ((user_ch=="rock" and computer_ch=="scissor") or (user_ch=="paper" and computer_ch=="rock") or (user_ch=="scissor" and computer_ch=="paper")):
        return "You won"  
    else:
        return "computer win"
print("Let's play the rock, paper scissor game ")       
while True:
     user_ch=user_choice()
     computer_ch=computer_choice()
     print("Your choice",user_ch)
     print("computer choice",computer_ch)
     print(determine_winner(user_ch,computer_ch))
     play_again=input("Do you Want to continue : Yes or no:").lower()
     if play_again != "yes":
         print("thank you")
         break
     