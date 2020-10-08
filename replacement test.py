word = """"""
guess = ''
word_length = len(word)
display = ''
word_list = ''
new_word = ''
found = ''
wrong_letters = ''
attempt = 0


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
    global guess, word_list, new_word, found, display, wrong_letters, attempt
    while word != new_word:
        guess = input('give me a letter: ')
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
        else:
            print("not found")
            print(display)
            wrong_letters = wrong_letters + guess
            wrong_letters = (wrong_letters + ', ')
            print('wrong letters: ' + wrong_letters)
            attempt = attempt + 1


print(back())
print("IT'S DONE")
if attempt == 1:
    print('you did it with ' + str(attempt) + ' error')
else:
    print('you did it with ' + str(attempt) + ' errors')
