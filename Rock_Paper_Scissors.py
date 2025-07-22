import random

user_score = 0
computer_score = 0
while True:
    print("\nRock Paper Scissors GAME")
    print("------------------------")
    print(f"Score: You {user_score} - {computer_score} Computer")
    user_choice = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()

    if user_choice=='q':
        print("\nFinal Score:")
        print(f"You: {user_score}  Computer: {computer_score}")
        print("Thanks for playing!")
        break

    if user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        continue

    choices = ['rock','paper','scissors']
    computer_choice = random.choice(choices)

    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice=='rock' and computer_choice=='scissors') or \
         (user_choice=='paper' and computer_choice== 'rock') or \
         (user_choice =='scissors' and computer_choice=='paper'):
        print("You win this round!")
        user_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1