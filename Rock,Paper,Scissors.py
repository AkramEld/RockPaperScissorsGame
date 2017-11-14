import random

while True:
    choice = ["Rock", "Paper", "Scissors"]

    userHand = raw_input("\nPlease pick between Rock, Paper or Scissors (type out the name correctly: ").title()

    computerHand = (random.choice(choice))

    def game(first, second):

        if userHand == computerHand:
            
            print("Computer picked", second)
            print("\ntie!")
            
        elif userHand == "Rock":
            if computerHand == "Scissors":
                
                print("Computer picked", second)
                print("\nYou Win!")
            else:
                
                print("Computer picked", second)
                print("\nYou Lose!")
                
        elif userHand == "Paper":
            if computerHand == "Rock":
                
                print("Computer picked", second)
                print("\nYou Win!")
            else:
               
                print("Computer picked", second)
                print("\nYou Lose!")
                
        elif userHand == "Scissors":
            if computerHand == "Paper":
               
                print("Computer picked", second)
                print("\nYou Win!")
            else:
               
                print("Computer picked", second)
                print("\nYou Lose!")

        else:
            print("\nPlease pick between Rock, Paper or Scissors (type out the name correctly:")

    game(userHand, computerHand)
