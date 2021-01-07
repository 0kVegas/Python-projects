# -----VARIABLES-----
phrase = str(input('please enter the binary string: '))
word = ''
num_of_spaces = phrase.count(' ')
# ----- DICTIONARY-----
dictionary = {'00000': ' ', "00001": 'a', '00010': 'b', '00011': 'c', '00100': 'd', '00101': 'e', '00110': 'f',
              '00111': 'g', '01000': 'h', '01001': 'i', '01010': 'j', '01011': 'k', '01100': 'l', '01101': 'm',
              '01110': 'n', '01111': 'o', '10000': 'p', '10001': 'q', '10010': 'r', '10011': 's', '10100': 't',
              '10101': 'u', '10110': 'v', '10111': 'w', '11000': 'x', '11001': 'y', '11010': 'z'}


# -----PROCESS-----
def translator(space_count):
    global word
    for i in range(space_count + 1):
        letter_num = phrase.split(' ')[i]
        letter = dictionary[letter_num]
        word = word + letter
    return word


print(translator(num_of_spaces))
