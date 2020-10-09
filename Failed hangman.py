# -----Imports-----
import random

# -----Global Variables------
global attempt_count
global guess_letters
global correct_letters
global wrong_letters
global wrong_letter_guess_count

# -----Potential Words-----
potential_words = {
    1: 'cat',
    2: 'dog',
    3: 'bird',
    4: 'banana',
    5: 'animal',
    6: 'location'
}

# -----Lists-----
basic = [1, 2, 3, 4, 5, 6]

# -----Word Generator-----
list_num = random.randint(1, 7)
word = potential_words[list_num]


# -----Replacing System-----
def word_replace(replace):
    word_display = ""
    for letter in replace:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            word_display = word_display + '_'
        else:
            word_display = word_display + letter
    return word_display


correct = word_replace(word)


# -----Right Words-----
def right_words(guess):
    global correct
    for letter in guess:
        if letter in word:
            correct = correct + guess
        else:
            correct = correct
    return correct


# -----Game Display-----
def display():
    if wrong_letter_guess_count == 0:
        print("")
        print(correct)
    elif wrong_letter_guess_count == 1:
        print("0")
        print(correct)
    elif wrong_letter_guess_count == 2:
        print('0')
        print('|')
        print(correct)
    elif wrong_letter_guess_count == 3:
        print(' 0')
        print('/|')
        print(correct)
    elif wrong_letter_guess_count == 4:
        print(' 0')
        print('/|\ ')
        print(correct)
    elif wrong_letter_guess_count == 5:
        print(' 0')
        print('/|\ ')
        print('/')
        print(correct)
    elif wrong_letter_guess_count == 6:
        print(' 0')
        print('/|\ ')
        print('/ \ ')
        print(correct)
