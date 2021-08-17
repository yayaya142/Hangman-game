#region All Def

import random
def show_hidden_word(secret_word, old_letters_guessed):
    """show _ _ _ """
    secret_word = list(secret_word)
    guessed_string = ' '.join(
        letter if letter in old_letters_guessed else '_ ' for letter in secret_word)
    return (guessed_string)
    

def check_win(secret_word, old_letters_guessed):
    """ cheak if the user win or lose if lose need to add var num of tries + 1"""
    secret_word_list = list(secret_word)
    guessed_string = ''.join(
        letter if letter in old_letters_guessed else '_ ' for letter in secret_word_list)
    return True if guessed_string == secret_word else False

#region def HANGMAN photo (def = print_hangman)

#region HANGMAN photo database:
picture_1 = """
    x-------x"""
picture_2 = """
    x-------x
    |
    |
    |
    |
    |
"""
picture_3 = """
    x-------x
    |       |
    |       0
    |
    |
    |
"""
picture_4 = """
    x-------x
    |       |
    |       0
    |       |
    |
    |
"""
picture_5 = """
    x-------x
    |       |
    |       0
    |      /|\\
    |
    |
"""
picture_6 = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
"""
picture_7 = """
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
"""
#endregion HANGEMAN PHOTO database

# HANGMAN PHOTO dict:
HANGMAN_PHOTO = {'1': picture_1, '2': picture_2, '3': picture_3,
                 '4': picture_4, '5': picture_5, '6': picture_6, '7': picture_7, }

#^^ end HANGMAN photo dict

# HANGMAN num of tries def:

def print_hangman(num_of_tries):
    # num_of tries = real number of tries
    if num_of_tries == 1:
        print(HANGMAN_PHOTO["1"])
    elif num_of_tries == 2:
        print(HANGMAN_PHOTO["2"])
    elif num_of_tries == 3:
        print(HANGMAN_PHOTO["3"])
    elif num_of_tries == 4:
        print(HANGMAN_PHOTO["4"])
    elif num_of_tries == 5:
        print(HANGMAN_PHOTO["5"])
    elif num_of_tries == 6:
        print(HANGMAN_PHOTO["6"])
    elif num_of_tries == 7:
        print(HANGMAN_PHOTO["7"])

#^^ end HANGMAN num of tries def
#endregion


def check_valid_input(letter_guessed, old_letters_guessed):
    """ cheak if the input is correct or invalid.
    :parm letter_guessed: the letter that you guess
    :parm old_letters_guessed: the list of all the letter you already guess
    :type letter_guessed: str
    :type old_letter_guessed: list
    :return: True or False
    :rtype: bool
    """
    letter_guessed = letter_guessed.lower()
    if (letter_guessed in old_letters_guessed):
        return (False)
    elif letter_guessed.isalpha():
        if len(letter_guessed) == 1:
            return (True)
        else:
            return (False)
    elif not letter_guessed.isalpha():
        return (False)

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """ return if the input is correct or invalid, if True add the letter to the list, if False give Eror message.
    :parm letter_gussed: the letter that you guess
    :parm old_letters_gussed: the list of all the letter you already guess
    :type letter_gussed: str
    :type old_letters_guessed: list
    :return: if True return true and save the new letter in list, if False give messgage (x , the list of all the letter you guess , False)
    :rtype : str , list , bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed) == True:
        letter_guessed = (letter_guessed.lower())
        old_letters_guessed = old_letters_guessed.append(letter_guessed)
        return (True)
    else:
        print("")
        old_letters_guessed = sorted(old_letters_guessed)
        old_letters_guessed = " -> ".join(old_letters_guessed)
        return old_letters_guessed


def sound_effect(sound_name):
    from time import sleep
    import winsound
    import random
    #game over
    if sound_name == 'game_over':
        winsound.PlaySound("WilhelmScream", winsound.SND_ASYNC)
        sleep(1.8)
        winsound.PlaySound("game_over", winsound.SND_ASYNC)
        # sleep(5)
    #letter lose
    elif sound_name == "letter_lose":
        winsound.PlaySound("letter_lose", winsound.SND_ASYNC)
        # sleep(1)
    #game opening
    elif sound_name == "open":
        winsound.PlaySound("game_open", winsound.SND_ASYNC)
        # sleep(4)
    #letter won
    elif sound_name == "letter_won":
        winsound.PlaySound("letter_win", winsound.SND_ASYNC)
        # sleep(1)
    #button press
    elif sound_name == "button_press":
        winsound.PlaySound("button_press", winsound.SND_ASYNC)
    #game_won
    elif sound_name == "game_won":
        choose_sound = "1 2 3 4".split()
        choose_sound = random.choice(choose_sound)
        if choose_sound == "1":
            winsound.PlaySound("auditorium_applause", winsound.SND_ASYNC)
            # sleep(5)
        elif choose_sound == "2":
            winsound.PlaySound("crowd_cheering", winsound.SND_ASYNC)
            # sleep(4)
        elif choose_sound == "3":
            winsound.PlaySound("mario", winsound.SND_ASYNC)
            # sleep(2)
        elif choose_sound == "4":
            winsound.PlaySound("medieval_announcement", winsound.SND_ASYNC)
            # sleep(7)
    
#region ascii
game_over = """
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼"""

game_win = """

                                            _   _                                       _ 
                                           | | | |                                     | |
  _   _  ___  _   _  __      _____  _ __   | |_| |__   ___    __ _  __ _ _ __ ___   ___| |
 | | | |/ _ \| | | | \ \ /\ / / _ \| '_ \  | __| '_ \ / _ \  / _` |/ _` | '_ ` _ \ / _ \ |
 | |_| | (_) | |_| |  \ V  V / (_) | | | | | |_| | | |  __/ | (_| | (_| | | | | | |  __/_|
  \__, |\___/ \__,_|   \_/\_/ \___/|_| |_|  \__|_| |_|\___|  \__, |\__,_|_| |_| |_|\___(_)
   __/ |                                                      __/ |                       
  |___/                                                      |___/                        

"""
#endregion ascii

#region random word
"""return a random word depend on what the player press. 
1 = animal 
2 = color 
3 = food and drink 
4 = sport 
5 = random 
:return = return the secert word"""

animal = "badger bat deer fox hare mole mouse otter rabbit rat squirrel crow dove goose hawk heron owl peafowl pigeon robin ant bee fly spider frog snake".split()
color = "red blue yellow purple green orange brown grey black white pink".split()
food_and_drink = "asparagus beef bread broccoli butter corn garlic honey lamb pepper pork rice spaghetti sugar apple avacado bacon beer buritto cake carrots cheese chicken catfish chips coffee crab dates donuts eggs milk pizza".split()
sport = "archery darts snooker golf cycling badminton football squash tennis boxing judo rugby wrestling fishing rowing saling kayaking skiing fencing polo".split()
random_category = "badger bat deer fox hare mole mouse otter rabbit rat squirrel crow dove goose hawk heron owl peafowl pigeon robin ant bee fly spider frog snake red blue yellow purple green orange brown grey black white pink asparagus beef bread broccoli butter corn garlic honey lamb pepper pork rice spaghetti sugar apple avacado bacon beer buritto cake carrots cheese chicken catfish chips coffee crab dates donuts eggs milk pizza archery darts snooker golf cycling badminton football squash tennis boxing judo rugby wrestling fishing rowing saling kayaking skiing fencing polo".split()


def random_word_type(number):
    number = int(number)
    category = ""
    word = ""
    if number == 1:
        category = animal
    elif number == 2:
        category = color
    elif number == 3:
        category = food_and_drink
    elif number == 4:
        category = sport
    elif number == 5:
        category = random_category
    word = random.choice(category).lower()
    return (word)
#endregion random word

#endregion

#region opning
play_again = "y"
while play_again == "y":
    sound_effect("open")
    print("""                      

                                    welcome the the game hangman



                        _    _                                         
                        | |  | |                                        
                        | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
                        |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
                        | |  | | (_| | | | | (_| | | | | | | (_| | | | |
                        |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                            __/ |                      
                                            |___/
    """)
#endregion

#region chose diffclty 
    print ("")
    print("Pick a number to choose category")
    print("""
1  animal
2  color
3  food and drink
4  sport 
5  random category""")
    pick_number = input("Enter number: ")
    sound_effect("button_press")
    word = (random_word_type(pick_number))
    word = word.lower()
    print ("")
    print ("the secret word have:", len(word), "letters")
    print ("""
You have seven attempts to guess the secrect word
if you fail the man will HANG!...""")
    old_letters_guessed_game = []
    print ("""

    """)
    print(show_hidden_word(word, old_letters_guessed_game))
#endregion

#region guessed:

    word = word
    old_letters_guessed_game = []
    num_of_tries_game = 0
    while int(num_of_tries_game) < 7 and check_win(word, old_letters_guessed_game) == False:
        print ("")
        new_letter = input("Enter a letter: ")
        if new_letter == "huckgame":
            print (word)
        
        print ("""


        








        
        """)
        old_letters_guessed_game.append(new_letter)
        print(" ", show_hidden_word(word, old_letters_guessed_game))
        if new_letter in list(word):
            print ("""
        correct""")
            sound_effect("letter_won")
            print(try_update_letter_guessed(new_letter, old_letters_guessed_game))
        else:
            num_of_tries_game += 1
            print_hangman(num_of_tries_game)
            sound_effect("letter_lose")
            print(try_update_letter_guessed(new_letter, old_letters_guessed_game))
    if check_win(word, old_letters_guessed_game) == True:
        sound_effect("game_won")
        print (game_win)
    elif int(num_of_tries_game) == 7:
        sound_effect("game_over")
        print (game_over)
        print ("""
        """)
        print ("The word was", word)

        
    
    play_again = input("do You want to play agian? press Y/N:" )
    play_again= play_again.lower()
    
    

#endregion gussed











