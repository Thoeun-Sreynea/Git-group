import random

def play_game():
    choices = ["rock" , "paper" , "scissors"]

    print ("Welcome to Rock_Paper_Scisor")

    user_choice = input("Please Enter your choice (rock , paper , scissors): ").lower()

    if user_choice not in choices : 
        print("The choices is not corrent! Please try again !")
        return
    computer_choice = random.choice(choices)
    print(f"Computer choice is  : {computer_choice}")

    if user_choice == computer_choice:
        print("You are Equel with computer")
    elif(user_choice == "rock" and computer_choice =="scissors" or
        user_choice == "paper" and computer_choice =="rock"or 
        user_choice == "scissors" and computer_choice == "paper") :
        print ("Congratulation! You are win!")
    else :
        print("You lose! Try again next time!")

play_game()
