# students = {
# "Mohamed": {"grades": [100, 90, 80], "age": 20},
# "Ahmed": {"grades": [100, 95, 93], "age": 21},
# "Ali": {"grades": [85, 83, 87], "age": 19},
# "Sara": {"grades": [100, 94, 98], "age": 21}
# }

# for i in range(len(students["Mohamed"]["grades"])):
#     print(students["Mohamed"]["grades"][i])


#
# print(20*'_')
# for i in students:
#         if i == "Mohamed":
#             print("Mohamed",end=' ')
#             for j1 in students[i]:
#                 if j1 == "grades":
#                     print("grades")
#         if i == "Ali":
#             print("Ali",end=' ')
#             for j2 in students[i]:
#                 if j2 == "age":
#                     print("age")

# print()
# print(f"Sara age and grades, each grade on a sperate line like this:")
# for k in students["Sara"]["grades"]:
#     print(k)


#
#
# students = {
# "Mohamed": {"grades": {
# "math": 100,
# "english": 90,
# "science": 80,
# "arabic": 100,
# "history": 97},
# "school": "Codezilla"
# },
# "Ahmed": {"grades": {
# "math": 100,
# "english": 95,
# "science": 93,
# "arabic": 100,
# "history": 94},
# "school": "Codezilla"
# },
# "Ali": {"grades": {
# "math": 85,
# "english": 83,
# "science": 87,
# "arabic": 100,
# "history": 90},
# "school": "Al-Azhar"
# },
# "Sara": {"grades": {
# "math": 100,
# "english": 94,
# "science": 98,
# "arabic": 100,
# "history": 100},
# "school": "Al-Azhar"
# }
# }
#
# for i in students:
#     if i == "Mohamed":
#         print(i,end=' ')
#         for j in students[i]:
#             if j == "grades":
#                 print(j,end=' ')
#                 for k in students[i][j]:
#                     if k == "math":
#                         print("in ,Math",end=' ')
#                     if k == "english":
#                         print("and English")
#
#
#



#
#
# pizzas = {
# "Margherita": 100,
# "Pepperoni": 120,
# "Meat Lovers": 150,
# "Chicken": 130,
# "Cheese": 100,
# "Veggie": 120,
# "Hawaiian": 150,
# }

# for i,j in pizzas.items():
#     print(f"{i}: cost {j}")
#


# drinks = {
# "Coke": 30,
# "Sprite": 25,
# "Fanta": 25,
# "Pepsi": 30,
# "Tea": 20,
# "Coffee": 25,
# "Orange Juice": 30,
# "Mango Juice": 30
# }

# for value in drinks.values():
#     print(value)



# menu = {
# "Cheese pizza": 100,
# "Veggie pizza": 120,
# "Hawaiian pizza": 150,
# "Coke": 30,
# "Sprite": 25,
# "Fanta": 25,
# "Pepsi": 30
# }
#
# menu["Ice Cream"]=30
# menu["Chocolate Cake"]=60
# menu["Cheese Cake"]=70
# menu["Brownie"]=40
# menu["Donut"]=30

# print(menu)



# menu = {
# "Cheese pizza": 100,
# "Veggie pizza": 120,
# "Hawaiian pizza": 150,
# "Coke": 30,
# "Sprite": 25,
# "Fanta": 25,
# "Pepsi": 30
# }


# for i in menu.values():
#     i *= 1.2
#     print(i)
#




# pizzas = {"Margherita": 100, "Pepperoni": 120,
# "Meat Lovers": 150, "Chicken": 130}
#
# ask = input("Enter Pizza: ")
# if ask in pizzas:
#     print("Yes")
# else:
#     print("Make a Pizza program that asks the user about the"
# "wanted pizza, and if available, it prints the pizza and"
# "its price. otherwise, you should print a sorry"
# "message")




