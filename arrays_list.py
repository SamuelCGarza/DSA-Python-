"""
File: arrays.py
An Array is like a list, but the client can use
only [], len, iter, and str.
To instantiate, use
<variable> = Array(<capacity>, <optional fill value>)
The fill value is None by default.
"""

class Array(object):
    """Represents an array."""
    
    def __init__(self, capacity, fill_value = None):
        """Represents an array object."""
        self.items = list()
        self.logical_size = 0
        self.capacity = capacity
        self.fill_value = fill_value
        
        for count in range (capacity):
            self.items.append(fill_value)
            
    def __len__(self):
        """Return the capacity of the array."""
        return len(self.items)
    
    def __str__(self):
        """Retrun a string representation of the array."""
        return str(self.items)
    
    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)
    
    def __getitem__(self, index):
        """Subscript operator for access at index."""
        if 0 <= index or index < self.size():
            return self.items[index]
        else:
            raise IndexError("Index is out of array bounds. Please enter valid index.")
     
    def __setitem__(self, index, new_item):
        """Subscript operator for replacmoent at index."""
        if 0 <= index or index < self.size():
            self.items[index] = new_item
        else:
            raise IndexError("Index is out of array bounds. Please enter valid index.")
       
    def size(self):
        """Returns the logical size of the array"""
        return self.logical_size
    
    def grow(self):
        """Doubles the size of the array object"""      
        temp = Array(len(self) * 2, self.fill_value)
        for i in range(self.size()):
            temp[i] = self.items[i]
        self.items = temp
        
    def shrink(self):
        """Halves the size of the array object"""
        temp = Array(len(self) // 2, self.fill_value)
        for i in range(self.size()):
            temp[i] = self.items[i]
        self.items = temp
       
    def insert(self, index, item):
        """Inserts an item at a specified index within the array."""
        if len(self) == self.size():
            self.grow()
            
        if index >= self.size():
            self.items[self.size()] = item 
        else:
            index = max(index, 0)
            for i in range(self.size(), index, -1):
                self.items[i] = self.items[i - 1]
            self.items[index] = item 
        self.logical_size += 1         
            
    def pop(self, index):
        """Removes and returns the element at the specified index"""
        if index < 0 or index >= len(self):
            raise IndexError("Invalid index. Please enter index with array bounds.")
        
        if self.items[index] == None:
            return None
            
        removed_item = self.items[index]
        for i in range(index, self.size() - 1):
            self.items[i] = self.items[i + 1]
            
        self.items[self.size() - 1] = self.fill_value
        self.logical_size -= 1
        
        if self.size() <= len(self) // 4 and len(self) > self.capacity:
            self.shrink()
        return removed_item
    
    def __eq__(self, other):
        """Returns True if the two arrays are equal or
        False otherwise."""
        if self is other: return True
        if self.size() != other.size(): return False
        if type(self) != type(other): return False
        for i in range(self.size()):
            if self.items[i] != other.items[i]:
                return False
        return True
    
    
def main():   
    """Test code for Array class"""   
    new_array = Array(10, 0)
    print(f"Array: {new_array}")
    print(f"Logical size: {new_array.size()}")
    print()
    
    new_array.grow()
    print(f"Array: {new_array}")
    print(f"Logical size: {new_array.size()}")
    print()   
     
    new_array.insert(0, 1)
    print(f"Array: {new_array}")
    print(f"Logical size: {new_array.size()}")
    print()

    new_array.insert(1, 1)
    print(f"Array: {new_array}")
    print(f"Logical size: {new_array.size()}")
    print()
   
    print(f"Array: {new_array}")
    removed = new_array.pop(1)
    print(f"Array: {new_array}")
    print(f"Logical size: {new_array.size()}")
    print(f"Popped item: {removed}")
    print()
    
    array_2 = Array(10,0)
    new_array.grow()
    array_2.insert(0, 1)
    array_2.insert(1, 1) 
    array_2.pop(1)   
    print(f"Array 2: {array_2}")
    blean = array_2 == new_array
    print(blean)

                
if __name__ == "__main__":
    main()