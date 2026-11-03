import random
from ascii_art import STAGES

"""Initialize the parameters"""
word_game = []
display_word = ""
mistakes = 0
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Return a randomly selected word from WORDS."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word , guessed_letter):
    """Display the snowman stage and the current word progress."""
    print(STAGES[mistakes])

    # Build a display version of the secret word
    display_word = ""


    for letter in secret_word:
        if letter in guessed_letter:
            display_word += letter
        else:
            display_word += '_'

    print("Word: ", display_word)
    print("\n")

    return display_word


def play_again():
    """Ask the player whether they want to play again."""
    play_again = input("\nWould you like to play again? yes(y) or no(n) "
                       ).lower()

    if play_again == "y" or play_again == "yes":
        play_game()
    else:
        print("THANK YOU FOR YOUR GAME")

    return


def play_game():
    """Run one round of Snowman Meltdown."""
    print('Welcome to Snowman Meltdown! \n' )

    # Initialize a new game.
    secret_word = get_random_word()
    mistakes = 0
    guessed_letter = []

    current_game_word = display_game_state(
        mistakes, secret_word, guessed_letter
    )

    # Continue until the word is guessed or the snowman melts.
    while mistakes < 6 and (current_game_word) != (secret_word):
        guess = input("Guess a letter: ").lower()

        # Validate the user's input.
        while guess in guessed_letter:
            print("You already guessed this letter!")
            guess = input("Guess a letter: ").lower()

        while len(guess) != 1 or not (guess.isalpha()) or not guess.isascii():
            guess = input("\n✓please enter just ONE letter: "
                          ).lower()

        print("You guessed:", guess)

        if guess in secret_word:
            guessed_letter.append(guess)
            current_game_word = display_game_state(
                mistakes, secret_word, guessed_letter
            )
        else:
            mistakes +=1
            display_game_state(
                mistakes, secret_word, guessed_letter
            )

       # Check whether the player has won or lost.
        if current_game_word == secret_word:
            print("Congratulations! You saved the snowman! ☃️")

        elif mistakes >= 6 :
            print("Oh no! The snowman melted! ⛄")
            print("The secret word was:", secret_word)

    play_again()