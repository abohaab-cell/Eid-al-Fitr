class Stack:
    def __init__(self):
        self.full = int(input("Enter your NumFull in Stack: "))
        self.size = 0
        self.stack = []

    def __repr__(self):

        print("[",end=' ')
        for i in self.stack:
            print(i,end=',')
        print("]")

    def empty(self):
        return self.size!=0
    def push(self,data):
        if self.size == self.full:
            return None
        else:
            self.stack.append(data)
            self.size += 1

    def top(self):
        return self.stack[0]


s1 = Stack()
s1.push(100)
s1.push(22)
s1.push(31)
s1.push(47)
s1.__repr__()
print(20*'_')
print(s1.top())
print(s1.empty())







