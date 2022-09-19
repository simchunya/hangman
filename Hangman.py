import requests
import json
import random
import string

url = "https://www.randomlists.com/data/words.json"
web = requests.get(url)
words = (json.loads(web.text))
a = words.values()
word_list = list(a)[0]
lives = 10

def get_valid_word():
    word = random.choice(word_list).upper()
    while "-" in word or " " in word:
        word = random.choice(word_list).upper()

    return word

def hangman():
    word = get_valid_word().upper()
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    sorted_used_letters = set()
    global lives

    while len(word_letters) > 0 and lives > 0:

        print("you have used these characters", " ".join(sorted_used_letters))

        hidden_word = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(hidden_word))
        print(f"You have {lives} lives remaining")

        user_letter = input(f"enter a letter to see if it's in the word\n").upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print("that letter is not in the word. You lost 1 life")

        elif user_letter in used_letters:
            print((f"You have already used that character {user_letter}. Please try again"))

        else:
            print("You entered an invalid character, please try again")

        sorted_used_letters = sorted(used_letters)
    if lives == 0:
        print(f"You lost with no lives remaining. The word was {word}")
    else:
        print(f"you Guessed it! the word is {word} with {lives} lives remaining")

get_valid_word()
hangman()








