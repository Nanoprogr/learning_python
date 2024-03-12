def guessing_game():
    print('in a the rang (1-10) try tu guess the correc number')
    while True:
        print('What is your guess')
        guess = input()
        
        if guess == '6':
            print(f' OK, {guess} is correct, congratulations')
            return False
        else:
            print(f'NO, {guess} is not correct')

guessing_game()