import random
'''
# Print the rules of the game
print("Winning rules of the game ROCK PAPER SCISSORS:")
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins")
'''

while True:
    # Ask user for their choice
    print("\nEnter your choice: \n1 - Rock \n2 - Paper \n3 - Scissors")
    choice = int(input("Your choice: "))

    # Validate user input
    while choice not in [1, 2, 3]:
        choice = int(input("Please choose a valid option (1, 2, or 3): "))

    # User choice to string
    if choice == 1:
        user_choice = "Rock"
    elif choice == 2:
        user_choice = "Paper"
    else:
        user_choice = "Scissors"

    print(f"User's choice: {user_choice}")

    # Computer's random choice
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissors"

    print(f"Computer's choice: {comp_choice_name}")

    # Decide the winner
    if choice == comp_choice:
        print("It's a tie!")
    elif (choice == 1 and comp_choice == 2) or (choice == 2 and comp_choice == 3) or (choice == 3 and comp_choice == 1):
        print("Computer wins!")
    else:
        print("You win!")

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
