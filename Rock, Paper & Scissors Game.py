#Rock, Paper & Scissors Game 
import random  # Import the random module to generate random choices for the computer

# List of choices available for the game
choices = ["rock", "paper", "scissors"]

# Function to play the game
def play_game():
    user_score = 0  # Variable to keep track of the user's score
    computer_score = 0 
    #ties = 0  # Variable to keep track of the computer's score

    print("Welcome to the Rock, Paper, Scissors game!")
    print("Type 'exit' at any time to stop playing.\n")

    while True:
        # Ask the user to input their choice
        user_choice = input("Enter your choice- 'rock', 'paper', or 'scissors'?\n") .lower()

        # If the user wants to exit the game
        if user_choice == "exit":
            print(f"\nFinal Scores:")
            print(f"Your score: {user_score}")
            print(f"Computer's score: {computer_score}")
            #print(f"Ties: {ties}")
            
            print("Thanks for playing! Goodbye!!")
            break

        # Validate user input
        if user_choice not in choices:
            print("Oops!! Invalid input. Please enter 'rock', 'paper', or 'scissors'.\n")
            continue

        # Get the computer's random choice
        computer_choice = random.choice(choices)

        # Print both choices
        print(f"\nYou chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine the winner and update the score
        if user_choice == computer_choice:
            print("It's a tie!!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            user_score += 1  # Increase user's score
        else:
            print("Computer wins!")
            computer_score += 1  # Increase computer's score

        # Show the current scores
        print(f"Scoreboard: You: {user_score} | Computer: {computer_score}\n")
# Start the game
play_game()
