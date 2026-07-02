
import random

stats = {
    "games_played": 0,
    "games_won": 0,
    "games_lost": 0,
    "best_score": None
}


def choose_level():
    print("\nChoose Difficulty")
    print("1. Easy   (1-10, 8 attempts)")
    print("2. Medium (1-50, 6 attempts)")
    print("3. Hard   (1-100, 4 attempts)")

    while True:
        choice = input("Enter choice (1-3): ")

        if choice == "1":
            return 10, 8
        elif choice == "2":
            return 50, 6
        elif choice == "3":
            return 100, 4

        print("Invalid choice. Please try again.")


def show_stats():
    print("\n----- Statistics -----")
    print("Games Played :", stats["games_played"])
    print("Games Won    :", stats["games_won"])
    print("Games Lost   :", stats["games_lost"])

    if stats["best_score"] is None:
        print("Best Score   : No wins yet")
    else:
        print("Best Score   :", stats["best_score"], "attempts")

    print("----------------------")


def play_game():
    stats["games_played"] += 1

    max_num, attempts = choose_level()
    secret_number = random.randint(1, max_num)

    print(f"\nGuess a number between 1 and {max_num}")

    for attempt in range(1, attempts + 1):

        print(f"\nAttempts Left: {attempts - attempt + 1}")

        while True:
            try:
                guess = int(input("Enter your guess: "))

                if guess < 1 or guess > max_num:
                    print(f"Please enter a number between 1 and {max_num}")
                    continue

                break

            except ValueError:
                print("Please enter a valid whole number.")
        difference = abs(guess-secret_number)
        if difference == 0:
            print(f"\nCongratulations! You guessed the number in {attempt} attempts.")

            stats["games_won"] += 1

            if (
                stats["best_score"] is None
                or attempt < stats["best_score"]
            ):
                stats["best_score"] = attempt
                print("New Best Score!")

            return

        elif difference <= 3:
            print("Very Close!")

        elif difference <= 10:
            print("Close!")

        elif difference <= 20:
            print("Not too far.")

        else:
            print("Far away.Try again")

    print(f"\nGame Over! The correct number was {secret_number}")
    stats["games_lost"] += 1


def main():
    print("=== Number Guessing Game ===")

    while True:
        play_game()

        show_stats()

        again = input("\nPlay again? (y/n): ").lower().strip()

        if again != "y":
            print("\nFinal Statistics")
            show_stats()
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()

