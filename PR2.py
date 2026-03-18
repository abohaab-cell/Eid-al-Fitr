# compny_name = "codezilla"
# name = input("Enter your name: ")
# birthday = input("Enter your birthday: ")
#
# print(f"{compny_name}\n{name[-3:]}\n{birthday}\n")


name_full = input("Enter your full name: ")
print(f"Hello,{name_full.title()[:name_full.index(" ")]}!\n"
      f"Welcome to Codezilla!")



#----------------------------
 # id = first 3 characters of company name + - + last 2
 # characters of name + birth year


x1 = input("Enter your name: ")
x2 = input("Enter your company name: ")
x3 = int(input("Enter your birth year: "))
x4 = input("Enter your email: ")
print(50*'-')
print(f"Hello,{x1.title()[:name_full.index(" ")]}!\n"
      f"Welcome at Codezilla!")
print(50*'-')

print(f"your id is: {x2[:3].lower()}-{x1[-2:].lower()}{x3}")
clicing_x4 = x4.index("@")
print(f"your email is: {x4[:clicing_x4]+"@codezilla.com"}")



