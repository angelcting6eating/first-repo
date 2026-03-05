guess = 0
tries = 0
while guess != 8 and tries < 5:
    guess = int(input('Guess the number, you get 5 guesses:'))
    tries += 1
    print('try again, you have', 5 - tries, 'tries left')
    if tries == 5:
        print('you ran out of tries')
        exit()
if guess == 8:
    print('you got it')
    exit()
