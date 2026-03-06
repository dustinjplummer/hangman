print("Welcome to Hangman")

# part 1
# We need the computer to pick a RANDOM word
import random
# We need the computer to choose from a LIST of words
words = ["mascara", "powder", "necklace", "banglets", "bracelets"]
# Store the randomly selected word in a variable to reference
secret_word = random.choice(words)

# print(secret_word)

# part 2
# We need to display the secret word without the letters for people to guess
display = []

# For each letter in our secret word, append an _ to our display
for letter in secret_word:
    display.append("_")

# print(secret_word)
print(display)
# We need to create a way for people to guess letters
# guess = input("Guess a letter:").strip().lower
# # We need to create a way to check if letter player used is in the secret word
# # for each position in our secret word, if the letter the player picks in that secret word, then find the position in our display and replace it
# for position in range(len(secret_word)):
#     secret_word_letter = secret_word[position]

#     if secret_word_letter == guess:
#         display[position] = guess

# print(display)

# while the word is not complete, and the game is not over, we get prompted for a new guess
    
game_over = False
while not game_over:

    guess = input("Guess a letter:").strip().lower()

    if(len(guess)) != 1:
        print("Please enter only ONe character")
        
# We need to create a way to check if letter player used is in the secret word
# for each position in our secret word, if the letter the player picks in that secret word, then find the position in our display and replace it
    for position in range(len(secret_word)):
        secret_word_letter = secret_word[position]

        if secret_word_letter == guess:
            display[position] = guess

    print(display)

    if "_" not in display:
        game_over = True
        print("You are a smart cookie")

print(len("Mississippi"))
print(len(""))
print(len("a"))