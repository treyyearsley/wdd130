print('Welcome to the word guessing game!')
word = input('What is your guess?')
iterCount = 1;

while word.lower() !='antler':
    print('Your guess was not correct')
    word = input('What is your guess?')
    iterCount = iterCount + 1;
print('Congratulations, You guessed it!')
print(f'It took you {iterCount} guesses.')
