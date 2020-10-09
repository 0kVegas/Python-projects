# -----Imports-----
import random
# -----Potential Words-----
potential_words = {
    1: 'cat',
    2: 'dog',
    3: 'bird',
    4: 'banana',
    5: 'animal',
    6: 'location'
}
# -----Random Word Selection-----
basic = [1, 2, 3, 4, 5, 6]
list_num = random.randint(1, 7)
# -----Variables-----
word = potential_words[list_num]
guess = ''
word_length = len(word)
display = ''
word_list = ''
new_word = ''
found = ''
wrong_letters = ''
error = 0


# -----Playing Board-----
def hanged(fails):
    if fails == 0:
        print('  ___________')
        print('  |         |')
        print('  |')
        print('  |')
        print('  |')
        print(' / \ ')
    elif fails == 1:
        print('  ___________')
        print('  |         |')
        print('  |         0')
        print('  |')
        print('  |')
        print(' / \ ')
    elif fails == 2:
        print('  ___________')
        print('  |         |')
        print('  |         0')
        print('  |         |')
        print('  |')
        print(' / \ ')
    elif fails == 3:
        print('  ___________')
        print('  |         |')
        print('  |         0')
        print('  |        /|')
        print('  |')
        print(' / \ ')
    elif fails == 4:
        print('  ___________')
        print('  |         |')
        print('  |         0')
        print('  |        /|\ ')
        print('  |')
        print(' / \ ')
    elif fails == 5:
        print('  ___________')
        print('  |         |')
        print('  |         0')
        print('  |        /|\ ')
        print('  |        /')
        print(' / \ ')
    elif fails == 6:
        print('  ___________')
        print('  |         |')
        print('  |         0')
        print('  |        /|\ ')
        print('  |        / \ ')
        print(' / \ ')


# -----Replacement-----
def replacement(replaced):
    global display
    for letter in replaced:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            display = display + '_'
        else:
            display = display + letter
    return display


print(replacement(word))


# -----Putting Words Back-----
def back():
    global guess, word_list, new_word, found, display, wrong_letters, error, word
    while word != new_word:
        print(hanged(error))
        if error == 6:
            return 'YOU LOSE'
        else:
            guess = input('give me a letter: ')
            word = word.upper()
            guess = guess.upper()
            if guess in word:
                for i in range(word_length - 1):
                    found = word.find(guess, i)
                    word_list = list(display)
                    word_list[found] = guess
                    if word_list[-1] == word_list[found] and word_list[-1] != word[found]:
                        word_list[-1] = '_'
                    else:
                        new_word = "".join(word_list)
                        display = new_word
                print(display)
                if word == new_word:
                    print('YOU WON')
            else:
                print("not found")
                print(display)
                wrong_letters = wrong_letters + guess
                wrong_letters = (wrong_letters + ', ')
                print('wrong letters: ' + wrong_letters)
                error = error + 1


# -----Final Result-----
print(back())
