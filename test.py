word = 'hello'
word_replaced = False
word_length = len(word)
guess = input('enter letter: ')


# -----Replacing System-----
def word_replace(replaced):
    word_display = ""
    for letter in replaced:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            word_display = word_display + '_'
        else:
            word_display = word_display + letter
    return word_display


correct = word_replace(word)


# -----Re Replace-----
def replace(words):
    changed = correct.replace(correct[words], guess)
    return changed


# -----Right Words-----
def right_words(attempt):
    global correct
    global word_replaced
    for letter in attempt:
        if letter in word:
            for i in range(word_length - 1):
                check = -1
                check = check + 1
                word_replaced = False
                found = word.find(guess, check)

                while not word_replaced:
                    replace(found)
        else:
            correct = correct
    return correct


while correct != word:
    guess = input('enter letters: ')
    word_replace(word)
    right_words(guess)
    print(correct)
