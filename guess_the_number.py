import random


def guess_number_between(min_number: int, max_number: int) -> int:
    """Ask the user for a guess, enforcing that it is an integer between the bounds."""
    while True:
        guess = input(f'Guess a number between {min_number} and {max_number}: ')
        try:
            guess = int(guess)
        except ValueError:
            print(f"'{guess}' is not a number")
            continue
        if guess < min_number or guess > max_number:
            print(f"'{guess}' is out of bounds")
            continue
        return guess


def check_guess(guess: int, generated_number: int) -> bool:
    """Return `True` if the user guessed correctly, otherwise return `False`"""
    if guess < generated_number:
        print('Too low!')
    elif guess > generated_number:
        print('Too high!')
    else:
        print('Correct!')
        return True
    return False

        
def play_again() -> bool:
    """Ask the user to play again, enforcing format of response.
    Return `True` if 'yes', `False` if 'no'."""
    while True:
        play_again = input('Play again? (y/n): ').lower()
        if play_again in ('y', 'yes'):
            return True
        elif play_again in ('n', 'no'):
            return False
        else:
            print('Cannot understand answer')


def main():
    # range in which random number may be
    MIN_NUMBER = 1
    MAX_NUMBER = 100

    # Flags for game loops
    playing = True
    guess_is_correct = False

    # main game loop
    while playing:
        random_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        
        while not guess_is_correct:
            guess = guess_number_between(MIN_NUMBER, MAX_NUMBER)
            guess_is_correct = check_guess(guess, random_number)

        playing = play_again()
        if playing:
            # reset `guess_is_correct` for the next game
            guess_is_correct = False
    print('Goodbye!')

if __name__ == '__main__':
    main()
