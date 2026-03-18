# class Employee:
#     def __init__(self,name,age,job):
#         self.name=name
#         self.age=age
#         self.job=job
#     def __str__(self):
#         return f"{self.name}-{self.age}-{self.job}"
#     # def __repr__(self):
#     #     return f"{self.name}-{self.age}-{self.job}"
#     def clct(self,hours,rate):
#         return (hours*rate)
#
# e = Employee("Islam",50,"Creator")
# # print(e.clct(50,2500))
# # e.name = "saeed_abuhani"
# # print(e.name)
# #
# print(e)
#
#
#


class Item:
    company = "abc"
    num_of_items = 0
    all_items = []
    def __init__(self,name,price,Quantity):
        self.name=name
        self.price=price
        self.Quantity=Quantity
        self.company="123"
        Item.num_of_items += 1
        Item.all_items.append(Item.num_of_items)
        Item.all_items.append(self)

    def __repr__(self):
        return (f"Name: {self.name}\n and nun_employee {Item.num_of_items}\n"
               f"the Price: {self.price}\n Quantity: "
                f"{self.Quantity}\nTotal Price:{self.price*self.Quantity}")
    # def say(self):
    #     print("Hello!")


#
# # Create an item
# item1 = Item("Atomic Habits", 10, 2)
# item2 = Item("Deep Work", 20, 1)
# item3 = Item("So Good They Can't Ignore You", 15, 3)
# item4 = Item("Digital Minimalism", 12, 2)
# # Display the number of items
# print(f"Number of items: {Item.num_of_items}")
# # result:
# # Number of items: 4
# # Display all items
# print(Item.all_items)
# # result:
# # [Item('Atomic Habits', 10, 2), Item('Deep Work', 20, 1),
# # Item('So Good They Can't Ignore You', 15, 3), Item('Digital
# # Minimalism', 12, 2)]
# # print each item in all_items
# for item in Item.all_items:
#     print(item)
#     print("##################")



#
# print(Item.all_employee)
# item1 = Item("Atomic Habits", 10, 2)
#
# # print(item1)
# # print(Item.num_employee)
# item2 = Item("Deep Work", 20, 1)
# # print(item2)
# # print(Item.num_employee)
# item3 = Item("Deep ", 5, 7)
# # for emplyee in Item.all_employee:
# #     print(emplyee)
#

# print(item3)
# print(Item.num_employee)
# print(Item.all_employee)
# Display item information
# print("Result item1:")
# item1.display()
# print("\n")
# print("Result item2:")
# item2.display()









class BankAccount:
    num_of_accounts = 0
    all_accounts = []
    bank_name = "Codezilla"
    def __init__(self,bank_name,balance):
        self.bank_name=bank_name
        self.balance=balance
        BankAccount.num_of_accounts += 1
        BankAccount.all_accounts.append(self)
    def __repr__(self):
        return f"Account Number: {self.bank_name}\nBalance: ${self.balance}"

    def add_money(self,add_balance):
        self.balance += add_balance
        print(f"added {add_balance} into account {self.bank_name}.")

    def display_balance(self):
        print(f"Account {self.bank_name} balance:{self.balance}")

    def withdraw(self,withrawing_money):
        if(withrawing_money <= 0):
            print("Insufficient funds or invalid amount.")
        elif self.balance - withrawing_money > 0:
            print("sufficient invalid amount.")
        else:
            print("Insufficient funds or invalid amount.")



print(BankAccount.bank_name) # Codezilla
account1 = BankAccount("5577", 1000)
account2 = BankAccount("1234", 2000)
print(BankAccount.num_of_accounts)
# 2
print(BankAccount.all_accounts)
# [BankAccount('5577', 1000), BankAccount('1234', 2000)]
account1.display_balance()
# Account 5577 balance: 1000
account2.display_balance()
# Account 1234 balance: 2000
account1.add_money(500) # added 500 into account 5577.
account1.display_balance() # Account 5577 balance: 1500
account2.withdraw(1000) # Withdrew 1000 from account 1234.
account2.display_balance() # Account 1234 balance: 1000
account1.withdraw(2000) # Insufficient funds or invalid amount.
account1.withdraw(-1000) # Insufficient funds or invalid amount.