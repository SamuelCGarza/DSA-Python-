from node import Node, Two_Way_Node

def length(head):
    counter = 0
    probe = head
    
    while probe != None:
        counter += 1
        probe = probe.next
        
    return counter

def insert(position, item, head):
    """Inserts a new node at a specified index within a linked structure."""
    if position <= 0 or head is None:
        head = Node(item, head)
    else:
        probe = head
        while position > 1 and probe.next != None:
            probe = probe.next
            position -= 1
        probe.next = Node(item, probe.next)
    return head
            
def pop(position, head):
    """Removes and returns an item at a specified index within a linked structure."""
    if position < 0 or position >= length(head):
        raise IndexError("Index out of bounds")
    
    if position <= 0 or head.next is None:
        removed_item = head.data
        head = head.next
    else:
        probe = head
        while position > 1 and probe.next.next != None:
            probe = probe.next
            position -= 1
        removed_item = probe.next.data
        probe.next = probe.next.next
    return (head, removed_item)

def make_two_way(head):
    """Takes a single linked structure as an argument and returns a double-linked structure."""
    probe = head.next
    head_2 = Two_Way_Node(head.data)
    tail = head_2
    while probe is not None:
        new_node = Two_Way_Node(probe.data)
        tail.next = new_node
        new_node.previous = tail
        tail = new_node
        probe = probe.next
    return (head_2, tail)
                
def print_structure(head):
    """Prints the elements in a linked structure."""
    current = head
    while current is not None:
        print(current.data, end = " ")
        current = current.next
    print("This is single linked structure")  # Add a newline to end the line of printed elements
         
def print_double_structure(tail):
    """Prints the elements in a double linked structure in reverse order."""
    probe = tail
    while probe != None:
        print(probe.data, end = " ")
        probe = probe.previous
    print("This is double linked structure from tail to head")
            
    

def main():
    """Tests modifications."""
    head = None
    head = insert(0, "1", head)
    print("1:", end=" ")
    print_structure(head)
    (head, item) = pop(0, head)
    print("1:", item, end=" ")
    print_structure(head)
    
    # Add five nodes to the beginning of the linked structure
    for count in range(1, 6):
        head = Node(count, head)
    
    print_structure(head)   
   
    
    (double_head, double_tail) = make_two_way(head)
    print_double_structure(double_tail)
  
    print_structure(double_head)
    
    print_structure(head)  


if __name__ == "__main__":
    main()

    