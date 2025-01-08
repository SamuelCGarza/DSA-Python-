
from arrays import Array
from arraybag import ArrayBag

class ArraySortedBag(object):
    """An array-based bag implementation."""
    
    # Class Variable
    DEFAULT_CAPACITY = 10   
    
    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the contents of sourceCollection, if it’s present."""
        
        self.items = Array(ArraySortedBag.DEFAULT_CAPACITY)
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
        
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1
                
    def __add__(self, other):
        """Returns a new bag containing the contents of self and other."""
        
        result = ArraySortedBag(self)
        for item in other:
            result.add(item)
        return result
    
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
    
    def __contains__(self, target):
        """Implements binary search for support in ArraySortedBag."""
        
        left = 0
        right = len(self) - 1
        while left <= right:
            midpoint = (left + right) // 2
            if target == self.items[midpoint]:
                return midpoint 
            elif target < self.items[midpoint]:
                right = midpoint - 1
            else:
                left = midpoint + 1
        return False
                
    def count(self, item):
        """Returns the number of instances of item in self."""
        
        index = 0
        count = 0
        while index < len(self):
            if self.items[index] == item:
                count += 1
            index += 1
        print(count, "instances of", item, "in", self)
    
    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        
        self.size = 0
        self.items = Array(ArraySortedBag.DEFAULT_CAPACITY)
        
    def clone(self):
        """Creates a clone of self and returns it to caller."""
        
        clone = ArraySortedBag(self)
        return clone            
    
    def add(self, item):
        """Adds item to self."""
        
        if len(self) == len(self.items):
            temp = Array(len(self.items) * 2)
            for i in range(len(self)):
                temp[i] = self.items[i]
            self.items = temp  
            
        if self.isEmpty() or item >= self.items[len(self) - 1]:
            ArrayBag.add(self, item)
        else:
            index = 0
            while item > self.items[index]:
                index += 1
            for i in range(len(self), index, -1):
                self.items[i] = self.items[i - 1]
            # Insert item and update size
            self.items[index] = item
            self.size += 1
        
    
    def remove(self, item):
        """Precondition: item is in self. Raises: KeyError if item in not in self. Postcondition: item is removed from self."""
   
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        for i in range(targetIndex, len(self) - 1):
            self.items[i] = self.items[i + 1]
        self.size -= 1
        # 5. Check array memory here and decrease it if necessary
        if len(self) <= len(self.items) // 4 and len(self.items) > ArraySortedBag.DEFAULT_CAPACITY:
            temp = Array(len(self.items) // 2)
            for i in range(len(self)):
                temp[i] = self.items[i]
            self.items = temp