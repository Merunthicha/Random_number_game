# Random Number Game
# Github: @Merunthicha
# Version: 1.1

# == IMPORT ==
import random as ran

# == RANDOM GAME ==
def random_game():
    print("Enter range of numbers do you want to play (Ex. 1 and 100)")

    while True:
        start_range = input("Start range of number: ")
        if not start_range.isdigit():
            print("Please enter a valid number!")
            continue
        start_range = int(start_range)

        last_range = input("Last range of number: ")
        if not last_range.isdigit():
            print("Please enter a valid number!")
            continue
        last_range = int(last_range)
        
        if start_range > last_range:
            print("=" * 40)
            print("Start must be less than end!")
            continue

        print("=" * 40)
        break
    
    random_number = ran.randint(start_range, last_range)

    print(f"Great! Now guess the number between {start_range} and {last_range}")
    while True:
        guess_number = input("Enter a number do you think: ")
        if not guess_number.isdigit():
            print("Please enter a valid number!")
            continue
        guess_number = int(guess_number)

        if guess_number > random_number:
            print("=" * 40)
            print(f"Lower than {guess_number}. Try again.")
            continue
        elif guess_number < random_number:
            print("=" * 40)
            print(f"Higher than {guess_number}. Try again.")
            continue
        else:
            print("=" * 40)
            print(f"{guess_number} is Correct!")
            
        play_again = input("Play again? (y/n): ")
        if play_again.lower() == "n":
            break
        elif play_again == "y":
            random_game()
        break

# == CREATOR INFO ==
def creator_info():
    print("Name:      Merunthicha (Wanvisa Phumam)")
    print("Github:   @Merunthicha")
    print("Telegram: @Merunthicha")
    print("Youtube:  @Merunthicha")
    print("")
    print("[R] Return")
    print("[E] Exit")
    while True:
        answer = input("Enter the answer: ").upper()
        print("=" * 40)
        if answer == "R":
            main()
        elif answer == "E":
            break
        else:
            print("Enter only R or E")
            continue
        break



# == MAIN ==
def main():
    while True:
        print("Welcome to Random Number Game (owo!)")
        print("[1] Start Game")
        print("[2] Creator")
        print("[3] Exit")
        answer = input("Enter a number: ")
        print("=" * 40)

        if answer.isdigit():
            answer = int(answer)
            if answer == 1:
                random_game()
            elif answer == 2:
                creator_info()
            elif answer == 3 :
                print("Goodbye!")
            break
        else:
            print("Please typing a number only 1 or 2")
        break
        
# == RUN ==
if __name__ == "__main__":
    main()