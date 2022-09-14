#create a class for Cookies
# class Cookie:
#     def __init__(self, color):
#         self.color = color
#     def get_color(self):
#         return self.color

#     def set_color(self, color):
#         self.color = color

# cookie_one = Cookie("pink")
# cookie_two = Cookie("yellow")

# print("Cookie one is", cookie_one.get_color())
# print("Cookie two is", cookie_two.get_color())

# cookie_one.set_color("black")

# print("Cookie one is now", cookie_one.get_color())

class Node:
    #create node
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append_node(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def pop_item(self):
        if self.length == 0:
            return None
        temp = self.head
        prev = self.head

        while temp.next:
            prev = temp
            temp = temp.next
        self.tail = prev
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.value





    def prepend(self, value):
        #create new node with that value
        new_node = Node(value)
        # empty list
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        # not empty list
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True   

    def pop_first(self):

        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.tail = None
        return temp       

    def get_index(self, index):
        if index < 0 or index > self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp


    def set_value(self, index, value):
        temp = self.get_index(index)
        if temp:
            temp.value = value
            return True
        return False


    def insert_value(self, index, value):
        # for index out of range
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append_node(value)

        new_node = Node(value)
        temp = self.get_index(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True


    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_item()

        #have previous pointer on the index before the one to remove
        prev = self.get_index(index - 1)
        #to do a O(1) operation instead to iterate through the elements,
        #  set temp to prev.next
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -= 1
        return temp.value

    def reverse_ll(self):
        #need a variable to point to head first
        temp = self.head
        #then set head equals to tail
        self.head = self.tail
        #then set tail equals to temp
        self.tail = temp
        #need one variable pointing after temp
        after = temp.next
        #need one variable pointing before temp
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after





my_linked_list = LinkedList(1)
my_linked_list.append_node(2)
my_linked_list.append_node(3)
my_linked_list.append_node(4)
my_linked_list.reverse_ll()

my_linked_list.print_list()

#  (2) Items - Return 2 Node
# print(my_linked_list.pop_item())
# #  (1) Item - Returns 1 Node
# print(my_linked_list.pop_item())
# #  (0) Items - Returns None
# print(my_linked_list.pop_item())

# my_linked_list.print_list()




