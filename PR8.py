# num = input("Enter your (*,/,+,-): ")
# num1 = int(input("Enter your num1: "))
# num2 = int(input("Enter your num2: "))
#
# match num:
#     case "*":
#         print(num1*num2)
#     case "/":
#         print(num1 / num2)
#     case "+":
#         print(num1 + num2)
#     case "-":
#         print(num1 - num2)
#     case _:
#         print("Error!")

print(20*'-')

# Employees and their offices
cairo = ['Islam Mahfouz', 'Mohamed Mesilhy',
'Hatem Elmaghraby', 'Kareem Embaby']
riyadh = ['Mohamed Gouda', 'Ayman Hamed',
'Seif Ali', 'Adham Wael']
casablanca = ['Ahmed Ashraf', 'Abd El-Rahman Mahrous',
'Islam Sheta', 'Mohamed Medhat', 'Mahmoud Nasser']
dubai= ['Ahmed Alaa', 'Kareem Abd-Elmeged',
'Osama Ashraf', 'Mohamed Mostafa', 'Ahmed Bedeir']

names = input("Enter your numes: ")
match names:
    case 'cairo' | 'egypt':
        print(f"The employees in {names} are: {",".join(cairo)}")
    case 'riyadh':
        print(f"The employees in {names} are: {",".join(riyadh)}")
    case 'casablanca':
        print(f"The employees in {names} are: {",".join(casablanca)}")
    case 'dubai':
        print(f"The employees in {names} are: {",".join(dubai)}")
    case _:
        print("Not find")