# a list of pizzas
pizzas = [
    'Margherita',
    'Pepperoni',
    'Super Supreme',
    'Hawaiian',
    'Meat Lovers',
    'Cheese Lovers'
]
print("please, Enter the number of the pizza"
      "you want to order:")
i = 0
while(i < len(pizzas)):
    print(f"{i}.{pizzas[i]}")
    i+=1
print("\n\n")



index = int(input("Enter the number of pizzas "
                  "you want : "))

print(50*'-')

print(f"Thanks for choosing\n"
      f"Codezillas Pizza!\n"
      f"Pleas, Enjoy your time\n"
      f"While we get {index} Meat Lovers pizza ready\n"
      f"for you")



# a list of hot drinks, soda, and juices
drinks = [
# hot drinks
['Tea', 'Herbs', 'Hot Cider', 'Coffee', 'Hot Chocolate'],
# soda
['Coke', 'Pepsi', 'Fanta', 'Sprite', 'Mirinda'],
# juices
['Lemonade', 'Orange Juice', 'Mango Juice',
'Strawberry Juice', 'Apple Juice']
]



print(f"Please, Enter the type of the drink"
      f" you want to order:")

print(f"{1}.{"hot drinks"}")
print(f"{2}.{"soda"}")
print(f"{3}.{"juices"}")

index3 = int(input(f"Please, Enter the number of the drink"
      f" you want to order:"))

print("\n")

i1 = 0
for i in drinks[index3-1]:
    print(f"{i1}.{i}")
    i1+=1


print("\n")

x = int(input("Enter "))

print(50*'-')

print(f"Thank for choosing Codezillas Caf'e!\n"
      f"Plasee, Enjoy your timer\n"
      f"While we get {drinks[index3-1][x]} reade for you.")




# a list of students’ ids
students = [
# Codezilla school
['1100', '1101', '1102', '1103', '1104',
'1105', '1106', '1107', '1108', '1109'],
# Al Dorra school
['2100', '2101', '2102', '2103', '2104',
'2105', '2106', '2107', '2108', '2109'],
# Mostafa Kamel school
['3100', '3101', '3102', '3103', '3104',
'3105', '3106', '3107', '3108', '3109']
]



id1 = int(input("Enter student id : "))
print(50*'-')
index4 = -1
flag = 0
for i in students:
    index4 += 1
    for j in i:
        if index4 == 0:
            if int(j) == id1:
                flag = 1
                print("Student is in Codezilla school")
                break
        if index4 == 1:
            if int(j) == id1:
                flag = 1
                print("Student is in Al Dorra school")
                break
        if index4 == 2:
            if int(j) == id1:
                flag = 1
                print("Student is in Mostafa Kamel school")
                break

if(flag == 0):
    print("Sorry, Student is not in our records")



















