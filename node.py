class Node(object):
    
    def __init__(self, data, next = None):
        """Instantiates a Node with default next of None."""
        self.data = data
        self.next = next
        
class Two_Way_Node(Node):
    
    def __init__(self, data, previous = None, next = None):
        """Instantiates a TwoWayNode."""
        Node.__init__(self, data, next)
        self.previous = previous
        
