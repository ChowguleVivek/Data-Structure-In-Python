# class to create node for 'Linked List'
class element:
    def __init__(self, value):
        self.value = value
        self.next = None


# class to create Linked list
class linkedList:
    # module to specify head of Linked list
    def __init__(self, head=None):
        self.head = head

    # method to add node at the tail of the linked list
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
