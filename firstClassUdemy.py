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



    



my_linked_list = LinkedList(40)
my_linked_list.append_node(2)
my_linked_list.print_list()




