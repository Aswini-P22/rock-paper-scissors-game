import random
player_score=0
computer_score=0
print("GAME START")
options = ("rock" , "paper","scissors")
run=True
while run:
    user_choice =None
    computer_choice=random.choice(options)
    while user_choice not in options:
        user_choice=input("Enter rock / paper / scissors: ")
    print(f"Player chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if(user_choice == computer_choice):
        print(f"Both player chose {user_choice} , It's a tie")
    elif (user_choice == "rock"):
        if(computer_choice == "scissors"):
            print("Rock smashes Scissors , You Win")
            player_score+=1
        else:
            print("Paper covers Rock , You Lose")
            computer_score+=1
    elif (user_choice == "paper"):
        if(computer_choice == "rock"):
            print("Paper covers rock , You Win")
            player_score+=1
        else:
            print("Scissors cuts Paper , You Lose")
            computer_score+=1
    else:
        if(computer_choice =="paper"):
            print("Scissors cuts Paper , You Win")
            player_score+=1
        else:
            print("rock smashes Scissors, You Lose")
            computer_score+=1
    s=input("Want to Play Again? (y/n)")
    if not s == 'y':
        run =False
print(f"Your Score {player_score}")
print(f"Computer Score {computer_score}")

