text = """A computer is a digital electronic machine
that can be programmed to carry out sequences of
arithmetic or logical operations automatically"""

len_text = text.count(" ")
print(len_text)
print(f"Number of characters with space: {len(text)}")
print(f"Number of characters without space: {len(text)-len_text}")

"OR"


text = """A computer is a digital electronic machine that
can be programmed to carry out sequences of arithmetic or
logical operations automatically"""
# remove all spaces
new_text = text.replace(" ", "")
# get the number of characters
print("Number of characters with spaces: ", len(text))
print("Number of characters without spaces: ", len(new_text))



your_name = input("Enter your full name: ")
birth_date = input("Enter your birth date (dd-mm-yyy): ")
year_now = int(input("Enter the current year: "))
print(20*'-')
print(f"Hello, {your_name[:your_name.index(" ")]}\n"
      f"Wellcom at Age Calculater")
print(20*'-')
print(f"Your age is: {year_now-(int(birth_date.split("-")[2]))}")

operation_one = input("Enter The Operation: ")
print(20*'-')
operation_tow = operation_one.split(" ")
one = float(operation_tow[0])
tow = float(operation_tow[2])
result = 0
if(operation_tow[1] == "*"):
    result = one*tow
if(operation_tow[1] == "/"):
    result = one/tow
if(operation_tow[1] == "+"):
    result = one+tow
if(operation_tow[1] == "-"):
    result = one-tow
print(f"Multiplication result is {result}")

