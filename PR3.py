word = input("Enter a word: ")
ask = input(f"Does the word start with a vowel? 🤔🤔\n")
cheak_list_vowel = "iouae"
print(20*'-')
if ask == "NO":
    print(f"Bravoo! 🎉🎉🎉🎉")
    print(f"Codezilla does not start with vowel 🥳🥳🥳")
elif ask == "yes":
    if word[0].lower() not in cheak_list_vowel:
        print("Let's try again 😃😃😃")
    else:
        print(f"Bravoo! 🎉🎉🎉🎉\n")
        print(f"{word} start with vowel 🥳🥳🥳")
