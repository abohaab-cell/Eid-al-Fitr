import random
from ctypes import oledll


def split_words(game_words):
    return game_words.split("$")

# print(split_words("hello$world$great$years$before$winter"))
def random_str(lst):
    x = split_words(lst)
    return random.choice(x)
lst = "hello$world$great$years$before$winter"


def get_guess_result(secret_word, guess_letter,currunt_word):
    z = []
    for i in secret_word:
        z.append(i)
    for j in secret_word:
        if guess_letter in z:
            currunt_word[z.index(guess_letter)] = guess_letter
        else:
            continue
    return currunt_word


# l = random_str(lst)
curr_word = get_guess_result("the","a",["_","_","_"])
print(curr_word)
curr_word = get_guess_result("the","e",curr_word)
print(curr_word)
curr_word = get_guess_result("the","t",curr_word)
print(curr_word)
curr_word = get_guess_result("the","h",curr_word)
print(curr_word)












