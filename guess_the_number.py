import random


def guess_number(generated_number: int, min_number: int, max_number: int) -> int:
    while True:
        guess = input(f'Guess a number between {min_number} and {max_number}: ')
        try:
            guess = int(guess)
        except ValueError:
            print(f"'{guess}' is not a number")
            continue

        if guess < min_number or guess > max_number:
            print(f"'{guess}' is out of bounds")
        elif guess < generated_number:
            print('Too low!')
        elif guess > generated_number:
            print('Too high!')
        else:
            print('Correct!')
            break

        
def play_again() -> bool:
        while True:
            play_again = input('Play again? (y/n)')
            if play_again.lower() in ('y', 'yes'):
                return True
            elif play_again.lower() in ('n', 'no'):
                return False
            else:
                print('Cannot understand answer')


def main():
    MIN_NUMBER = 1
    MAX_NUMBER = 100

    while True:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        guess_number(number, MIN_NUMBER, MAX_NUMBER)
        if not play_again():
            break


if __name__ == '__main__':
    main()
