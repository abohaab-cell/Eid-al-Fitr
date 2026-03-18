import random

from PR1 import index


def split_words(game_words):
    return game_words.split("$")

# print(split_words("hello$world$great$years$before$winter"))
def random_str(lst):
    x = split_words(lst)
    return random.choice(x)
lst = "hello$world$great$years$before$winter"


def get_guess_result(secret_word, guess_letter,currunt_word):
    currunt_word *= len(secret_word)
    for i in range(len(secret_word)):
        if guess_letter in secret_word:
            x = secret_word.index(guess_letter)
            currunt_word[x] = guess_letter
        else:
            continue
    return currunt_word


# l = random_str(lst)
print(get_guess_result("the","a",[]))










