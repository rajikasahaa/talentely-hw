#hangman

import random
def hangman():
    stages = [
        '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
''', 
        '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
''', 
        '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
''', 
        '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', 
        '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', 
        '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', 
        '''
  +---+
  |   |
      |
      |
      |
      |
=========
'''
    ]

    words = ["hangman", "programming", "developer", "software", "java", "algorithm", "freelancing", "blockchain", "engineering", "python"]
    word = random.choice(words)
    guessed_letters = []
    tries = len(stages) - 1
    guessed = False

    print("Hangman Game")
    print(stages[tries])
    print("_" * len(word))

    while not guessed and tries > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed that letter.")
            elif guess not in word:
                print(f"{guess} is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job! {guess} is in the word.")
                guessed_letters.append(guess)
            
            word_completion = ""
            for letter in word:
                if letter in guessed_letters:
                    word_completion += letter
                else:
                    word_completion += "_ "
            print(stages[tries])
            print(word_completion)

            if "_" not in word_completion:
                guessed = True
        else:
            print("Invalid input. Enter a single letter.")

        print(f"You have {tries} tries left.")

    if guessed:
        print("Congratulations, you guessed it right!")
    else:
        print(f"Unfortunately, you ran out of tries. The word was '{word}'. Please do play again.")

hangman()
