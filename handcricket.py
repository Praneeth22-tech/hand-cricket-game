import random
import sys

sys.stdout.reconfigure(encoding='utf-8')


def get_number(prompt):
    while True:
        try:
            number = int(input(prompt))

            if 1 <= number <= 6:
                return number
            else:
                print("Please enter a number between 1 and 6.")

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")


def hand_cricket():
    print("🏏 Welcome to Hand Cricket!")
    print("Rules: Choose a number between 1 and 6.")
    print("If your number matches the computer's, you're OUT!")

    # User bats first
    print("\n--- Your Batting Innings ---")

    runs = 0

    while True:
        user_shot = get_number("Play your shot (1-6): ")
        comp_ball = random.randint(1, 6)

        print(f"Computer bowled: {comp_ball}")

        if user_shot == comp_ball:
            print("You're OUT!")
            break
        else:
            runs += user_shot
            print(f"You scored {user_shot} runs. Total = {runs}")

    target = runs + 1

    print(f"\nYour final score: {runs}")
    print(f"Computer needs {target} runs to win.")

    # Computer bats
    print("\n--- Computer's Batting Innings ---")

    comp_runs = 0

    while comp_runs < target:
        user_ball = get_number("Bowl (1-6): ")
        comp_shot = random.randint(1, 6)

        print(f"Computer played: {comp_shot}")

        if user_ball == comp_shot:
            print("Computer is OUT!")
            break
        else:
            comp_runs += comp_shot
            print(f"Computer scored {comp_shot} runs. Total = {comp_runs}")

    # Match result
    print("\n--- Match Result ---")

    if comp_runs >= target:
        print("Computer wins! 🎉")
    else:
        print("You win! 🏆")


# Run the game
hand_cricket()