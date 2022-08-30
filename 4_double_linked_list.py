



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None





class DoubleLinkedList:
    def __init__(self, value):    
        new_node = Node(value)  
        self.head = new_node
        self.tail = new_node        
        self.length = 1


        
        
        
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
            


    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True




    def pop(self):
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
        
        



    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
        return True





    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp






    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length - 1, index, -1):
                temp = temp.prev
        return temp








    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False





    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        before = self.get(index - 1)
        after = before.next

        new_node.prev = before
        new_node.next = after
        before.next = new_node
        after.prev = new_node

        self.length += 1
        return True




    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp










'''

# test LinkedList.method(), wait O_O, it's DoubleLinkedList

print('# create a DoubleLinkedList')
my_doubly_linked_list = DoubleLinkedList(1)
print('# test append(2), append(3), append(4)')
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.print_list()
print()
print()
print()
print()





print('# test pop()')
print('# to remove the last Node, do not care else')
my_doubly_linked_list.pop()

print('# to print the linkedlist right now')
my_doubly_linked_list.print_list()

print("\n# to remove the last Node, print it's object")
print(my_doubly_linked_list.pop())

print("\n# to remove the last Node, and get it's value")
print(my_doubly_linked_list.pop().value)

print('\n# to print the linkedlist right now')
my_doubly_linked_list.print_list()
print()
print()
print()
print()





print('# test prepend()')
my_doubly_linked_list.prepend(2)
my_doubly_linked_list.prepend(3)
my_doubly_linked_list.prepend(4)
print('# to print the linkedlist right now')
my_doubly_linked_list.print_list()
print()
print()
print()
print()





print('# test pop_first()')
print('# to remove the first Node, do not care else')
my_doubly_linked_list.pop_first()
print('# to print the linkedlist right now')
my_doubly_linked_list.print_list()
print()
print()
print()
print()




print('# test get(1)')
print(my_doubly_linked_list.get(1).value)
print()
print()
print()
print()




print('# test set_value(0, 23)')
my_doubly_linked_list.set_value(1, 23)
print('# to print the linkedlist right now')
my_doubly_linked_list.print_list()
print()
print()
print()
print()




print('# test insert(2, 76)')
my_doubly_linked_list.insert(2, 76)
print('# to print the linkedlist right now')
my_doubly_linked_list.print_list()
print()
print()
print()
print()







print('# test remove()')
my_doubly_linked_list.remove(0)
print('# to print the linkedlist right now')
my_doubly_linked_list.print_list()
print()
print()
print()
print()


'''




