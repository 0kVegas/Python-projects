word = 'hello'
guess = ''
word_length = len(word)
display = ""
word_list = ''
new_word = ''


def replacement(replaced):
    global display
    for letter in replaced:
        if letter in 'abcdefghijklmnopqrstuvwxyz':
            display = display + '_'
        else:
            display = display + letter
    return display


print(replacement(word))


def back():
    global guess, word_list, new_word
    replacement(word)
    while word != new_word:
        guess = input('give me a letter: ')
        if guess in word:
            found = word.find(guess)
            for i in range(word_length - 1):
                word_list = list(display)
                word_list[found] = guess
            new_word = "".join(word_list)
            print(new_word)
        else:
            print("not found")


print(back())
