class Node:
    def __init__(self,data):
        self.data=data
        self.next = None

n1 = Node(7)
print(n1.data)

class SinglyLinkedlist:
    def __init__(self):
        self.head = None
        #traversal
    def traversal(self):

        if self.head is None:
            print("Empty LL")
        else:
            a = self.head
            while a is not None:
                print(a.data, end = " ")
                a = a.next

    def insertion_at_beginning(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insertion_at_end(self,data):
        print()
        ne = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next
        a.next = ne

    def insertion_at_position(self,data,position):
        print()
        nib = Node(data)
        a = self.head #a = sll.head = nb
        for i in range(1,position - 1 ):
            a = a.next # 1 a = nb.next, n1 = n1.next, n2 = n2.next


        nib.next = a.next
        a.next = nib

    def deletion_at_begining(self):
        print()
        a = self.head
        self.head = a.next
        a.next = None

    def deletion_at_end(self):
        print()
        prev = self.head
        a = self.head.next
        while a.next is not None:
            prev = prev.next
            a = a.next

        prev.next = None

    def deletion_at_position(self,position):
        print()
        prev = self.head # n1
        a = self.head.next #n1.next

        for i in range(1,position - 1):
            prev = prev.next # prev = n1.next
            a = a.next          # a = n2.next

        prev.next = a.next
        a.next = None








n1 = Node(5)
sll = SinglyLinkedlist()
sll.head = n1
n2 = Node(10)
n1.next = n2
n3 = Node(15)
n2.next = n3

sll.insertion_at_beginning(2)
sll.traversal()
sll.insertion_at_end(6)
sll.traversal()
sll.insertion_at_position(11,4)
sll.traversal()
sll.deletion_at_begining()
sll.traversal()
sll.deletion_at_end()
sll.traversal()
sll.deletion_at_position(3)
sll.traversal()

print(type(n1.data))
print(type(n1.next))




