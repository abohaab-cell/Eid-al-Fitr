# class A:
#     all_number = 0
#     list_type_A = []
#     def __init__(self,name,age):
#         self.__name = name
#         self.__age = age
#         A.all_number += 1
#         A.list_type_A.append(self)
#     def __repr__(self):
#         return  (f"Your name is : {self.__name}\n"
#                  f"and the age is : {self.__age}")
#     def  print(self):
#         print("Hello Python!")
#
#     def set(self,age1):
#         self.__age = age1
#     def get(self):
#         return self.__age
# a1 = A("k",2)
# a2 = A("r",3)

# for i in A.list_type_A:
#     print(i)
# print(a1._A__age)



class Number:
    def __init__(self,number):
        self.number = number
    def __repr__(self):
        return f"Your number is : {self.number}"

    @staticmethod
    def __check_number(number):
        return len(number)==10

    @property
    def get_number(self):
        return self.number

    @get_number.setter
    def set1(self,new_number):
        if Number.__check_number(new_number):
            self.number = new_number
            return self.number
        else:
            return False


n1 = Number("123456899")
n2 = Number("125488881")
# print(n1)
# print(n2)
# print(50*'-')
#
# n1.set1("1256666669")
# print(n1.number)

n1.set1 = "1000000007"
print(n1.get_number)







