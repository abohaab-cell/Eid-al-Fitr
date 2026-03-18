

class Node:
    all_list = []
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return f"{self.data} : {self.next}"
class LinkedList:
    def __init__(self):
        self.head = None


    def __repr__(self):
        if self.head is None:
            return False
        else:
            nd = self.head
            s = []
            while nd is not None:
                s.append(nd.data)
                nd = nd.next
            Node.all_list = s.copy()
            return s

    def insert_start(self,data):
        if self.head is None:
            return False
        else:
            ne = Node(data,None)
            ne.next = self.head
            self.head = ne


    def insert_start(self,data):
        if self.head is None:
            return False
        else:
            new_node = Node(data,None)
            a = self.head
            while a.next is not None:
                a = a.next
            a.next = new_node
            return new_node

    def serch(self,index):
        return Node.all_list[index]




n1 = Node(1)
l = LinkedList()
l.head = n1
n2 = Node(2)
n1.next = n2
n3 = Node(3)
n2.next = n3
n4 = Node(4)
n3.next = n4
n5 = Node(5)
n4.next = n5

l.insert_start(100)
l.insert_start(200)
l.insert_start(300)



print(l.__repr__())
print(20*'_')
print(l.serch(2))
