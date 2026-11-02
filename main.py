# List of secret words
import random
WORDS = ["python", "git", "github", "snowman", "meltdown"]
word_game = []

def get_random_word():

    return random.choice(WORDS)


def play_game():
    # Use a breakpoint in the code line below to debug your script.
    #print('Welcome to Snowman Meltdown!\n\n')
    print("i am here fun play_game")
    #######snow man body parts##########

    head_top = " ___ "
    head_bottom = "/___\\"
    face = "(ö ö)"
    body_top = "( : )"
    body_bottom = "( : )"

    #####################################
    counter = 0


    list_snowman_parts = [
        head_top,
        head_bottom,
        face,
        body_top,
        body_bottom,
    ]

    print('Welcome to Snowman Meltdown! \n' )
    random_word = get_random_word()
    for part in list_snowman_parts:
        print("\033[97m"+ part+ "\033[96m")

   # print( f"Word: \n", end="")
    print(random_word)
    print(f"Word: ", end="")

    for dash in range(0,len(random_word)):
        #user_guess = input("Guess a letter:")
        print("_", end="")
        word_game.append('_')
    print('\n\n')
    while counter < 3:
        user_guess = input("Guess a letter:")
        if user_guess in random_word:
           # print(f"{user_guess}", end = '')
            index_guess = list(random_word).index(user_guess)
            word_game[index_guess] = user_guess
            for item in word_game:
                print(item , end=" ")

        print('\n')


        counter += 1
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    play_game()
assert get_random_word()