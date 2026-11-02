# List of secret words
import random
WORDS = ["python", "git", "github", "snowman", "meltdown"]
word_game = []

# Snowman ASCII Art stages
STAGES = [
     # Stage 0: Full snowman
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     ( : ) 
     """,
     # Stage 1: Bottom part starts melting
     """
      ___  
     /___\\ 
     (o o) 
     ( : ) 
     """,
     # Stage 2: Only the head remains
     """
      ___  
     /___\\ 
     (o o) 
     """,
     # Stage 3: Snowman completely melted
     """
      ___  
     /___\\ 
     """
 ]

def get_random_word():

    return random.choice(WORDS)
def display_game_state(mistakes, secret_word , guessed_letter):
    print(STAGES[mistakes])
    # Build a display version of the secret word

    display_word = ''
    for letter in secret_word:
        if letter == guessed_letter:
            display_word += letter
        else:
            display_word += '_'

    print("Word: ", display_word)
    print("\n")


def play_game():
    # Use a breakpoint in the code line below to debug your script.

    print("i am here fun play_game")
    print('Welcome to Snowman Meltdown! \n' )
    # For now, display the initial game state.

    secret_word = get_random_word()
    mistakes = 0
    guessed_letter = []

    # Prompt user for one guess (logic to be enhanced later)

    display_game_state(mistakes, secret_word, guessed_letter)
    guess = input("Guess a letter: ").lower()
    print("You guessed:", guess)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    play_game()