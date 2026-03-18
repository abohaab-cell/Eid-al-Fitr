import  random


num = int(input("Enter a number 1 and 20: "))
num1 = random.randint(1,20)
print(num1)
if num == num1:
    print("You Win!")
else:
    print("You Lost!")
print(50*'-')


x = ["for Heads","for Tails"]
y = random.choice(x)
print(y)
print("Guess the coin flip!\n")
print(f"1 for Heads\n")
print(f"2 for Tails\n")
num_str = input(" ")
if(num_str == "1"):
    c = "for Heads"
    if(c == y):
        print("The Coin us Heads")
        print("You Win!")
    else:
        print("The Coin us Heads")
        print("You Lost!")

if(num_str == "2"):
    c = "for Tails"
    if (c == y):
        print("The Coin us Heads")
        print("You Win!")
    else:
        print("The Coin us Heads")
        print("You Lost!")



