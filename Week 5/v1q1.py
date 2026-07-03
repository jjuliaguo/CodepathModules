"""
Write a function find_max() that takes in the head of a 
linked list and returns the maximum value in the linked list. 
You can assume the linked list will contain only numeric values.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you 
believe your solution has the stated time and space complexity.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def find_max(head):
    maxVal = 0
    current = head

    if not head:
        return None  # Return None if the linked list is empty

    maxVal = head.value  # Initialize maxVal with the value of the head node
    current = head.next  # Start from the next node
    while current:
        if current.value > maxVal:
            maxVal = current.value
        current = current.next

    return maxVal
#Example Usage:

head1 = Node(5, Node(6, Node(7, Node(8))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_max(head1))

head2 = Node(5, Node(8, Node(6, Node(7))))

# Linked List: 5 -> 8 -> 6 -> 7
print(find_max(head2))
# Expected Output:
""""

8
8
"""