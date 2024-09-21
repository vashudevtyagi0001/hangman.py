import random

words = ["apple", "banana", "cherry", "date", "elderberry"]

word = random.choice(words)

guessed = ["_"] * len(word)

incorrect_guesses = set()

lives = 6

print("Welcome to Hangman!")
print("You have", lives, "lives.")

while lives > 0:
   
    print(" ".join(guessed))
    print("Incorrect guesses:", ", ".join(incorrect_guesses))

   
    guess = input("Guess a letter: ").lower()

    
    if guess in word:
      
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
       
        incorrect_guesses.add(guess)
        lives -= 1
        print("Incorrect! You have", lives, "lives left.")

    
    if "_" not in guessed:
        print("Congratulations! You won!")
        break

if lives == 0:
    print("Game over! The word was", word)