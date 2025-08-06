import random

def attempt_checker(attempts):
    while attempts > 5 or attempts <= 0:
        print("\nNumber of attempts must be between 1 and 5.")
        attempts = int(input("Please enter a valid number of attempts (1-5): "))
    return attempts


def number_checker(user_input,start,end):
    while user_input > end or user_input < start:
        print(f"\nNumber must be between {start} and {end}.")
        user_input = int(input(f"Please enter a valid number ({start}-{end}): "))
    return user_input


def random_integer_generator(start,end):
    return random.randint(start, end)

def check_difference(difference):
    if difference == 1:
        print("You're very close!")
    elif 2 <= difference <= 3:
        print("You're not far away!")
    else:
        print("You're quite far away!")


def play_game(attempts, start, end, guessed_number, user_input):
    while attempts != 0:
        if user_input == guessed_number:
            print("\nCongratulations! You guessed the number correctly.")
            break
        else:
            attempts -= 1
            if attempts == 0:
                print(f"\nSorry, you've run out of attempts. The correct number was {guessed_number}.")
                break
            else:
                print(f"\nWrong guess! You have {attempts} attempts left.")
                
                difference = abs(user_input - guessed_number)
                check_difference(difference)


                user_input = int(input(f"Try again. Enter a number to guess between {start} - {end}: "))
                user_input = number_checker(user_input, start, end)
    


def game():
    print("\n---- WELCOME TO NUMBER GUESSING GAME ----\n")
    start = int(input("Enter the starting number for the guessing range: "))
    end = int(input("Enter the ending number for the guessing range: "))

    guessed_number = random_integer_generator(start, end)

    attempts = int(input("\nEnter the number of attempts you want to take (max 5) : "))
    attempts = attempt_checker(attempts)

    user_input = int(input(f"Enter a number to guess between {start} - {end}: "))
    user_input = number_checker(user_input, start, end)

    play_game(attempts, start, end, guessed_number, user_input)



game()


play_again = input("\nDo you want to play again? (yes/no): ")

while play_again.lower() == "yes":
    game()
    play_again = input("\nDo you want to play again? (yes/no): ")
else:
    print("\nThanks for playing! Goodbye!")