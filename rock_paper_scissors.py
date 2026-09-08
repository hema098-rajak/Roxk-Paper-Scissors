import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0
draws = 0

print("=" * 45)
print("        ROCK • PAPER • SCISSORS")
print("=" * 45)
print("First player to reach 5 points wins!")
print()

while player_score < 5 and computer_score < 5:

    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    player_input = input("Enter your choice (1/2/3): ").strip()

    if player_input not in ["1", "2", "3"]:
        print("❌ Invalid choice! Please enter 1, 2, or 3.")
        continue

    player_choice = choices[int(player_input) - 1]
    computer_choice = random.choice(choices)

    print(f"\n👤 You chose:      {player_choice.upper()}")
    print(f"🤖 Computer chose: {computer_choice.upper()}")

    # Decide winner
    if player_choice == computer_choice:
        print("🤝 It's a DRAW!")
        draws += 1

    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or
        (player_choice == "paper" and computer_choice == "rock")
        or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 YOU WIN THIS ROUND!")
        player_score += 1

    else:
        print("😔 COMPUTER WINS THIS ROUND!")
        computer_score += 1

    print("\n" + "-" * 45)
    print(f"👤 Your Score:      {player_score}")
    print(f"🤖 Computer Score:  {computer_score}")
    print(f"🤝 Draws:           {draws}")
    print("-" * 45)


# Final result
print("\n" + "=" * 45)
print("                 GAME OVER")
print("=" * 45)

if player_score > computer_score:
    print("🏆 CONGRATULATIONS! YOU WON THE GAME!")
elif computer_score > player_score:
    print("🤖 COMPUTER WON THE GAME!")
else:
    print("🤝 THE GAME ENDED IN A DRAW!")

print(f"\nFinal Score: You {player_score} - {computer_score} Computer")
print(f"Total Draws: {draws}")
print("\nThanks for playing! 🎮")