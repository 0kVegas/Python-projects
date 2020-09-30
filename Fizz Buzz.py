# I need 2 numbers that when a multiple of theirs arrives it switches with fizz or buzz
# when those two numbers combine it turns into a fizzbuzz
# I need a way of collecting those two numbers

fizz = int(input('Which number is fizz?: '))
buzz = int(input('which number is buzz?: '))


for i in range(1, 101):
    fizz_mult = i % fizz
    buzz_mult = i % buzz

    if fizz_mult == 0 and buzz_mult == 0:
        print('Fizz Buzz')
    elif fizz_mult == 0:
        print('Fizz')
    elif buzz_mult == 0:
        print('Buzz')
    else:
        print(i)
