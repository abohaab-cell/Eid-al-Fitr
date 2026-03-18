# list of available vegetables
vegetables = ['broccoli', 'eggplant', 'carrot', 'cabbage',
'cucumber', 'potato', 'garlic', 'pepper']


print("Wellcome at Codezilla Vegetables!\n")
vegetable = input("Enter the Vegetable you want to get: ")
print(20*'-')


if vegetable in vegetables:
    vegetable_kg = int(input("Enter the amount in kg: "))
    print(f"We will get you {vegetable_kg} kg of {vegetable} very soon")
else:
    vegetables1 = vegetables[-1]
    vegetables2 = vegetables[:-1]

    print(f"Sorry, we only only have {", ".join(vegetables2)} and {vegetables1}")



