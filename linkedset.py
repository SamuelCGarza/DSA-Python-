
from node import Node

class LinkedSet(object):
    """An link-based bag implementation.""" 
    
    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it’s present."""
        self.items = None
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)
    
    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0

    
    def __len__(self):
        """Returns the number of items in self."""
        return self.size
    
    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"
    
    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = self.items
        while cursor != None:
            yield cursor.data
            cursor = cursor.next
                
    def __add__(self, item):
        """Returns a new bag containing the contents of self and other."""
        self.items = Node(item, self.items)
        self.size += 1
    
    def __eq__(self, other):
        """Returns True if self equals other, or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
            len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True
    
    def count(self, item):
        """Returns the number of instances of item in self."""
        return 0
    
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = None
        
    def clone(self):
        clone = LinkedSet(self)
        return clone
    
    def add(self, item):
        """Adds item to self."""
        if item in self:
            return
        else:
            new_node = Node(item)
            if self.items is None:
                self.items = new_node
            else: 
                probe = self.items
                while probe.next != None:
                    probe = probe.next
                probe.next = new_node
            self.size += 1
    
    def remove(self, item):
        """Precondition: item is in self. Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        
        # Check precondition and raise an exception if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for the node containing the target item
        # probe will point to the target node, and trailer
        # will point to the node before it, if it exists
        probe = self.items
        trailer = None
        for targetItem in self:
            if targetItem == item:
                break
        trailer = probe
        probe = probe.next
        # Unhook the node to be deleted, either the first one or
        # one thereafter
        if probe == self.items:
            self.items = self.items.next
        else:
            trailer.next = probe.next
        # Decrement logical size
        self.size -= 1