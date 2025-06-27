import random

choices = ["rock", "paper", "scissors"]

while True:
    user_score = 0
    computer_score = 0

    while user_score < 3 and computer_score < 3:
        print("\nChoose your move:")
        print("1. Rock 🪨")
        print("2. Paper 📄")
        print("3. Scissors ✂️")
        user_input = int(input("Your move: "))
        user_move = choices[user_input - 1]
        computer_move = random.choice(choices)

        print(f"\nYou chose: {user_move}")
        print(f"Computer chose: {computer_move}")

        if user_move == computer_move:
            print("It's a draw!")
        elif (user_move == "rock" and computer_move == "scissors") or \
             (user_move == "paper" and computer_move == "rock") or \
             (user_move == "scissors" and computer_move == "paper"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

    print("\n🏁 Game Over!")
    print(f"Final Score — You: {user_score}, Computer: {computer_score}")
    if user_score == 3:
        print("🎉 You won the game!")
    else:
        print("💻 Computer won the game!")

    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again != "y":
        print("👋 Thanks for playing! See you soon.")
        break