"""
Defines a matrix class to support simple matrix arithmetic.
"""
from grid import Grid
from arrays import Array
# Write your code below:
class Matrix(Grid):

    def __init__(self, rows, columns, fillValue = None):
        super().__init__(rows, columns, fillValue)

    
    def __add__(self, other):
        if(isinstance(other,Matrix) and self.getHeight() == other.getHeight() and self.getWidth() == other.getWidth()):   
            result = Grid(self.getHeight(), self.getWidth())
            for i in range(self.getHeight()):
                for j in range(self.getWidth()):
                    result.data[i][j] = self.data[i][j] + other.data[i][j]
            return result
        raise Exception("Width and Height of Matrices to be added must be equal")

    def __sub__(self, other):
        if(isinstance(other,Matrix) and self.getHeight() == other.getHeight() and self.getWidth() == other.getWidth()):   
            result = Grid(self.getHeight(), self.getWidth())
            for i in range(self.getHeight()):
                for j in range(self.getWidth()):
                    result.data[i][j] = self.data[i][j] - other.data[i][j]
            return result
        raise Exception("Width and Height of Matrices to be added must be equal")

    def __mul__(self,other):
        if(isinstance(other,Matrix) and self.getWidth() == other.getHeight()):
            result = Grid(self.getHeight(), other.getWidth())
            for i in range(self.getHeight()):
                for j in range(other.getWidth()):
                    result.data[i][j] = 0
                    for k in range(self.getWidth()):
                        result.data[i][j] += (self.data[i][k] * other.data[k][j])
            return result
        raise Exception("Width and Height of Matrices to be added must be equal")


def main():
    m1 = Matrix(3, 3, 2)
    m2 = Matrix(3, 3, 4)
    print(m1 + m2)
    m1 = Matrix(4, 4, 2)
    m2 = Matrix(4, 4, 4)
    print(m2 - m1)
    m1 = Matrix(2, 3, 2)
    m2 = Matrix(3, 2, 4)
    print(m1 * m2)

if __name__ == "__main__": main()
