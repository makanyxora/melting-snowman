WORDS = ["python", "git", "github", "snowman", "meltdown"]
import random
from ascii_art import STAGES
secret_word = random.choice(WORDS)
print(secret_word)
word_game = []
display_word = ""
mistakes = 0
def get_random_word():

    return random.choice(WORDS)


def display_game_state(mistakes, secret_word , guessed_letter):
    print(STAGES[mistakes])
    # Build a display version of the secret word
    display_word = ""
    #print("You guessed: ", secret_word)
    for letter in secret_word:
        if letter in guessed_letter:
            display_word += letter
        else:
            display_word += '_'

    print("Word: ", display_word)
    print("\n")
    return display_word


def play_game():
    # Use a breakpoint in the code line below to debug your script.
    print('Welcome to Snowman Meltdown! \n' )
    # For now, display the initial game state.

    secret_word = get_random_word()
    mistakes = 0
    guessed_letter = []
    current_game_word = display_game_state(mistakes, secret_word, guessed_letter)

    # Prompt user for one guess (logic to be enhanced later)
    while mistakes < 3 and (current_game_word) != (secret_word):
        guess = input("Guess a letter: ").lower()
        print("You guessed:", guess)

        if guess in secret_word:
            guessed_letter.append(guess)
            display_game_state(mistakes, secret_word, guessed_letter)
        else:
            mistakes +=1
            display_game_state(mistakes, secret_word, guessed_letter)

        current_game_word = display_game_state(mistakes, secret_word, guessed_letter)
        if current_game_word == secret_word:
            print("Congratulations! You saved the snowman! ☃️")
        elif mistakes >= 3 :
            print("Oh no! The snowman melted! ⛄")
            print("The secret word was:", secret_word)