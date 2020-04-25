import random
word = [
    'khiar',
    'shalgham',
    'havij',
    'sik',
    'bus'
]
while True:
    start = input("press S to start or enter Q to quit")
    if start.lower() == 'q':
        break
    secret_word = random.choice(word)
    bad_guesses = []
    good_guesses = []
    while len(bad_guesses) < 5 and len(good_guesses) != len(list(secret_word)):
        for letter in secret_word:
            if letter in good_guesses:
                print(letter, end='')
            else:
                print('_', end='')
        print('')
        print('strikes: {}/5'.format(len(bad_guesses)))
        print('')
        guess = input("guess a letter").lower()
        if len(guess) != 1:
            print("you can only a letter guess: ")
            continue
        elif guess in bad_guesses or guess in good_guesses:
            print("you have already guess that letter")
            continue
        elif not guess.isalpha():
            print("you can only guess letters")
        if guess in secret_word:
            good_guesses.append(guess)
            if len(good_guesses) == len(list(secret_word)):
                print("you win the word was {}".format(secret_word))
                break
        else:
            bad_guesses.append(guess)
    else:
        print("you wrong my secret word was {}".format(secret_word))


