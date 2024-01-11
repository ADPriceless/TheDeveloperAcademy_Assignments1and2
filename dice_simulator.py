import random


def main():
    # range of dice rolls
    MIN_NUMBER = 1
    MAX_NUMBER = 6

    # main loop: ask the user if they want to roll the dice,
    # break out of loop if answer is 'no'
    while True:
        answer = input('Do you want to roll the dice? (y/n): ').lower()
        if answer in ('n', 'no'):
            print('Goodbye!')
            break
        elif answer in ('y', 'yes'):
            roll = random.randint(MIN_NUMBER, MAX_NUMBER)
            print(f'The dice rolled {roll}!')
        else:
            print('Sorry, I didn\'t understand that answer!')
            continue


if __name__ == '__main__':
    main()
