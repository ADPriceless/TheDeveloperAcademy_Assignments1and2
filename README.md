# TheDeveloperAcademy_Assignments1and2
Repo for the solutions to Assignments 1 &amp; 2: Dice Rolling Simulator and Guess The Number, respectively

## Dice Rolling Simulator
### Structure
- The min and max roll values are set by two constants
- Inside a while loop:
    - the program ask the user if they want to roll the dice
    - the answer is then checked:
        - if the answer is 'no', the program exits
        - if the answer is 'yes', a random number is generated and printed
        - if the answer is in an invalid format, the program says so and asks the user again whether they want to roll the dice

## Guess The Number
### Structure
#### `main` function
- contains a `while` loop that:
    - generates a random number
    - asks the user to guess the number (`guess_number` function)
    - when the user has guessed correctly, it asks if they want to play again (`play_again` function)

#### `guess_number` function
- inside a `while` loop:
    - asks the user to guess the number
    - checks the format of the number
    - checks whether the number is higher or lower than the generated number and gives feedback
    - if the answer is correct, break out of the loop

#### `play_again` function
- asks the user if they want to play again
- checks the format of the answer
- returns `True` or `False`, depending on whether the user enters 'yes' or 'no'