'''
As a biologist, you are working on editing a long strand of DNA represented as a linked list of nucleotides. 
Each nucleotide in the sequence is represented as a node in the linked list, 
where each node contains a character ('A', 'T', 'C', 'G') representing the nucleotide.

Given the head of the linked list dna_strand and two integers m and n, write a function edit_dna_sequence() 
that simulates the selective deletion of nucleotides in a DNA sequence. 
You will: 
- Start at the beginning of the DNA strand. 
- Retain the first m nucleotides from the current position. 
- Remove the next n nucleotides from the sequence. 
- Repeat the process until the end of the DNA strand is reached.

Return the head of the modified DNA sequence after removing the mentioned nucleotides.

Evaluate the time and space complexity of your solution. 
Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.

'''

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

def edit_dna_sequence(dna_strand, m, n):
    '''
    U: keep every m nodes and delete every n nodes sequentially
    P: 
    I:

    '''
    '''
    #while loop to traverse the linked list
        #traverse m nodes and keep the pointer there
        #traverse n nodes then prev pointer points to the new node
    '''
    curr = dna_strand
    temp = Node(-1, curr)

    while curr:
        m_counter = 1
        print(curr.value)
        while curr and m_counter < m:
            if not curr:
                return temp.next
            print(f'keeping: {m_counter} for value {curr.value}')
            curr = curr.next
            m_counter += 1

        if not curr:
            return temp.next
        
        prev = curr.next if curr.next else None
        # print(f'starting position to remove node from {prev.value}')
        n_counter = 0 #0
        while prev and n_counter < n:
            if not prev:
                break
            print(f'deleting: {n_counter} for value {prev.value}')
            prev = prev.next
            n_counter += 1
        # print(f'The end of the delete len {curr.value}')
        curr.next = prev if curr else None
        curr = curr.next
        # curr = curr.next

    return temp.next
# m = 2
# initial state: curr = 1, counter = 1
# while: 
#   curr = 2, counter = 2
# n = 3
# prev = curr = 2, counter = 0
# while:
#   curr = 3, counter = 1
#   curr = 4, counter = 2
#   curr = 5, counter = 3
# prev.next = curr.next = 6


dna_strand = Node(1, Node(2, Node(3, Node(4, Node(5, Node(6, Node(7, Node(8, Node(9, Node(10, Node(11, Node(12, Node(13)))))))))))))

print_linked_list(edit_dna_sequence(dna_strand, 2, 3))

'''
1 -> 2 -> 6 -> 7 -> 11 -> 12
Explanation: Keep the first (m = 2) nodes starting from the head of the linked List  
(1 -> 2) show in black nodes.
Delete the next (n = 3) nodes (3 -> 4 -> 5) show in red nodes.
Continue with the same procedure until reaching the tail of the Linked List.

'''