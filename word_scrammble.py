

import random

words = ["coolant","codder","coollar","cockpit","coolie"]
word = random.choice(words)
guessed = ["_" for _ in word]
attempts = 2
while attempts > 0 and "_" in guessed:
    print(" Word: " , " ".join(guessed))
    guess = input("Guess a letter: ")
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct!")
    else:
        attempts -= 1
        print(f"Game over! The word was:", word)