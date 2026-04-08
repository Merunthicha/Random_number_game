# Random Number Game
# Github: @Merunthicha
# Version: 1.1

# == IMPORT ==
import random as ran
from rich import print
from rich.panel import Panel


# == RANDOM GAME ==
# SET RAMGE
def random_game():
    while True:
        info_1 = """
Enter range of numbers do you want to play

Example
Start range of number: [cyan]1[/]
Last range of number: [cyan]100[/]

[red]Please don't use negative numbers[/]
"""
        print(Panel(info_1, title="RANDOM NUMBER GAME", expand=False))
        start_range = input("Start range: ")
        if not start_range.isdigit():
            print("Invalid!")
            continue
        start_range = int(start_range)

        last_range = input("Last range: ")
        if not last_range.isdigit():
            print("Invalid!")
            continue
        last_range = int(last_range)
        
        if start_range > last_range:
            print("Start must be less than end!")
            continue
        break
    
    random_number = ran.randint(start_range, last_range)

# GUESS
    info_2 = f"""
Great! Now guess the number between [cyan]{start_range}[/] and [cyan]{last_range}[/]
"""
    print(Panel(info_2, title="RANDOM NUMBER GAME", expand=False))
    while True:
        guess_number = input("Enter a number do you think: ")
        if not guess_number.isdigit():
            print("Please enter a valid number!")
            continue
        guess_number = int(guess_number)
        if guess_number > random_number:
            print(f"Lower than [green]{guess_number}[/]. Try again.")
            continue
        elif guess_number < random_number:
            print(f"Higher than [green]{guess_number}[/]. Try again.")
            continue
        else:
            print(f"Number {guess_number} is Correct!")
            while True:
                info_3 = """
Do you want to play this game again?

[Y] Yes
[N] No, back main menu
"""
                print(Panel(info_3, title="RANDOM NUMBER GAME", expand=False))
                choice = input("Play again?: ").upper()
                if choice == "Y":
                    return random_game()
                elif choice == "N":
                    return
                else:
                    print("[red]Invalid input! Please enter Y or N.[/]")
                    

# == CREATOR INFO ==

def creator_info():
    while True:
        info = """
[bold cyan]Name:[/] Merunthicha (Wanvisa Phumam)
[bold green]Github:[/] @Merunthicha
[bold yellow]Telegram:[/] @Merunthicha
[bold red]Youtube:[/] @Merunthicha

[R] Return
[E] Exit
"""
        print(Panel(info, title="CREATOR INFO", expand=False))
        answer = input("Enter your choice: ").upper()

        if answer == "R":
            return
        elif answer == "E":
            exit()
        else:
            print("Invalid input!")


# == MAIN ==
def main():
    while True:
        info = """
Welcome to Random Number Game (owo!)

[S] Start Game
[C] Creator
[E] Exit
"""
        print(Panel(info, title="[bold]MAIN MENU[/]", expand=False))
        answer = input("Enter your choice: ").upper()
        if answer == "S":
            random_game()
        elif answer == "C":
            creator_info()
        elif answer == "E" :
            exit()
            break
        else:
            print("Invalid input!")
        continue
        
# == RUN ==
if __name__ == "__main__":
    main()