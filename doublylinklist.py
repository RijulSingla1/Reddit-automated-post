class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def forward_traversal(self):
        a = self.head
        while a is not None:
            print(a.data,end =" ")
            a = a.next

    def backward_traversal(self):
        print()
        a = self.head
        while a.next is not None:
            a = a.next

        while a is not None:
            print(a.data,end = " ")
            a = a.prev


    def insertion_at_beginning(self,data):
        new_node = Node(data)
        a = self.head
        new_node.next = a
        a.prev = new_node
        self.head = new_node

    def insertion_at_end(self, data):
        print()
        new_node = Node(data)
        a = self.head
        while a.next is not None:
            a = a.next

        new_node.prev = a
        a.next = new_node

    def insertion_at_pos(self, data, pos):
        print()
        new_node = Node(data)
        a = self.head

        for i in range(1,pos-1):
            a = a.next

        new_node.prev = a
        new_node.next = a.next
        a.next.prev = new_node
        a.next = new_node

    def deletion_at_beginning(self):
        print()
        a = self.head
        self.head = a.next
        a.next = None
        self.head.prev = None

    def deletion_at_end(self):
        print()
        a = self.head.next
        b = self.head

        while a.next is not None:
            a = a.next
            b = b.next

        a.prev = None
        b.next = None

    def deletion_at_pos(self,pos):
        print()
        a = self.head.next #n2
        b = self.head #n1

        for i in range(1,pos-1):
            a = a.next
            b = b.next

        a.prev = None
        a.next.prev = b
        b.next = a.next
        a.next = None















n1 = Node(1)
dll = DoublyLinkedList()
dll.head = n1
n2 = Node(2)
n1.next = n2
n3 = Node(3)
n2.next = n3
n2.prev = n1
n3.prev = n2
dll.forward_traversal()
dll.backward_traversal()
dll.insertion_at_beginning(0)

dll.backward_traversal()
dll.insertion_at_end(4)
dll.forward_traversal()
dll.insertion_at_pos(1.5,3)
dll.forward_traversal()
dll.deletion_at_beginning()
dll.forward_traversal()
dll.deletion_at_end()
dll.forward_traversal()
dll.deletion_at_pos(3)
dll.forward_traversal()
dll.backward_traversal()






