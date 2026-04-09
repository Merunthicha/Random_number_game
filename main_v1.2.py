# Random Number Game
# Github: @Merunthicha
# Version: 1.2

# == IMPORT ==
import random as ran
from rich import print
from rich.panel import Panel

# == MESSAGE ==
enter_a_letter = "[bold red]![/] Please enter a letter"
enter_your_choice = "Enter your choice: "

# CHOICES
def enter_only(choices):
    return f"[bold red]![/] Please enter only {' '.join(list(choices.keys()))}"


# MAIN MESSAGE
def main_message():
    info = """
Welcome to Random Number Game (owo!)

[S] Start Game
[C] Creator
[E] Exit
"""
    print(Panel(info, title="[bold cyan]MAIN MENU[/]", expand=False))

# CREATOR MESSAGE
def creator_message():
    info = """
[bold cyan]Name:[/] Merunthicha (Wanvisa Phumam)
[bold green]Github:[/] @Merunthicha
[bold yellow]Telegram:[/] @Merunthicha
[bold red]Youtube:[/] @Merunthicha

[R] Return
[E] Exit
"""
    print(Panel(info, title="[bold cyan]CREATOR INFO[/]", expand=False))

# RANDOM GAME MESSAGE
def random_game_message():
    info = """
Choose your desired dificulty level

Level:
[1] Easy
[2] Medium
[3] Hard
[C] Custom

[cyan][R] Return
"""
    print(Panel(info, title="[bold yellow]RANDOM NUMBER GAME[/]", expand=False))

# PLAY AGAIN MESSAGE
def play_again_message():
    info = """
Do you want to play this game again?

[Y] Yes
[N] No, back main menu
"""
    print(Panel(info, title="[bold yellow]RANDOM NUMBER GAME[/]", expand=False))

# == CUSTOM RANGE ==
def custom_range():
    print(Panel(
        """Enter range of numbers do you want to play

Example: 
Start range of number: [cyan]1[/]
Last range of number: [cyan]100[/]

[red]! Please don't use negative numbers[/]"""
, title="[bold yellow]RANDOM NUMBER GAME[/]", expand=False))
    while True:
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
    return start_range, last_range
                    
# == CREATOR INFO ==
def creator_info():
    choices = {
        "R": main,
        "E": exit
    }
    creator_message()
    while True:
        choice = input(enter_your_choice).upper()
        if choice in choices:
            choices[choice]()
            break
        elif choice.isdigit():
            print(enter_a_letter)
            continue
        else:
            print(enter_only(choices))

# == MAIN ==
def main():
    choices = {
        "S": random_game,
        "C": creator_info,
        "E": exit
    }
    main_message()
    while True:
        choice = input("Enter your choice: ").upper()
        if choice in choices:
            choices[choice]()
        elif choice.isdigit():
            print(enter_a_letter)
            continue
        else:
            print(enter_only(choices))

# == RANDOM GAME ==
def random_game():
    random_game_message()
    choices = {
        "1": (1, 10),
        "2": (1, 50),
        "3": (1, 100),
        "C": "Custom",
        "R": "Return"
    }
    while True:
        choice = input(enter_your_choice).upper()
        if choice in choices:
            if choice == "C":
                start_range, last_range = custom_range()
            elif choice == "R":
                main()
                break
            else:
                start_range, last_range = choices[choice]
            break
        else:
            print(enter_only(choices))
            continue
    
    # RANDOM NUMBER
    random_number = ran.randint(start_range, last_range)
    print(Panel(f"[green]Great![/] Now guess the number between [cyan]{start_range}[/] and [cyan]{last_range}[/]", title="[bold yellow]RANDOM NUMBER GAME[/]", expand=False))

    #GUESS LOOP
    while True:
        guess_number = input("Enter a number you think: ")
        if not guess_number.isdigit():
            print("Please enter a valid number!")
            continue
        guess_number = int(guess_number)
        if guess_number > random_number:
            print(f"Lower than [green]{guess_number}[/]. Try again.")
        elif guess_number < random_number:
            print(f"Higher than [green]{guess_number}[/]. Try again.")
        else:
            print(f"Number [green]{guess_number}[/] is Correct!")
            break
    # PLAY AGAIN
    play_again_message()
    choices = {
        "Y": random_game,
        "N": main
    }
    while True:
        choice = input(enter_your_choice).upper()
        if choice in choices:
            choices[choice]()
            break
        elif choice.isdigit():
            print(enter_a_letter)
        else:
            print(enter_only(choices))
        
# == RUN ==
if __name__ == "__main__":
    main()