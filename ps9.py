# 6.00 Problem Set 9
#
# Name: c4nn1b4l
# Time: about 2 hours

import re
from string import *

class Shape(object):
    def area(self):
        raise AttributeException("Subclasses should override this method.")


class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side


class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius


#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.
class Triangle(Shape):
    def __init__(self, base, height):
        """
        base: base of the triangle
        height: height of the triangle
        """
        self.base = float(base)
        self.height = float(height)
    def area(self):
        """
        returns are of the trianlge
        """
        return (self.base * self.height)/2
    def __str__(self):
        return 'Triangle with base length ' + str(self.base) + ' and height ' + str(self.height)
    def __eq__(self, other):
        """
        Two triangles are equal if they have the same base and same height
        other: object to check for equality
        """
        return type(other) == Triangle and self.height == other.height and self.radius == other.radius


def getTypeAndSizes(ob):
    answer = []
    numeri = []
    answer.append(type(ob))
    for i in str(ob).split():
        try:
            numeri.append(float(i))
        except ValueError:
            pass
    return answer


#
# Problem 2: Create the ShapeSet class
#
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet:
    def __init__(self):
        """
        Initialize needed variables
        """
        self.shapez = []
        self.shapeSizes = []
        self.shapeTypes = []
        self.shapeAreas = []
        self.shapeTypesAndSizes = []
    def checkDuplicate(self, sh):
        if len(self.shapeSizes) == 0:
            return False
        elif str(sh) in self.shapeSizes:
            return True
        else:
            return False
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        if self.checkDuplicate(sh):
            raise ValueError('duplicate')
        else:
            self.shapeSizes.append(str(sh))
            self.shapeTypes.append(type(sh))
            self.shapeAreas.append(sh.area())
            self.shapeTypesAndSizes.append(getTypeAndSizes(sh))
            self.shapez.append(sh)
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        self.place = 0
        return self
    def __next__(self):
        if self.place >= len(self.names):
            raise StopIteration
        self.place += 1
        return self.shapeTypesAndSizes[self.place-1]
    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        circles = []
        squares = []
        triangles = []
        ite = 0
        for item in self.shapeTypes:
            if item == Circle:
                circles.append(self.shapeSizes[ite])
                ite += 1
            elif item == Square:
                squares.append(self.shapeSizes[ite])
                ite += 1
            elif item == Triangle:
                triangles.append(self.shapeSizes[ite])
                ite += 1
            else:
                pass
        answer = []
        for ans in circles:
            answer.append(ans)
        for ans in squares:
            answer.append(ans)
        for ans in triangles:
            answer.append(ans)
        return str(answer)


a = Circle(2.5)
b = Square(4.1)
c = Triangle(2.4,7.3)

d = ShapeSet()
d.addShape(a)
d.addShape(b)
d.addShape(c)

print(d)
        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    if type(shapes) != ShapeSet:
        raise TypeError('not a shapeset')
    else:
        answer = []
        maximum = max(shapes.shapeAreas)
        for she in shapes.shapez:
            if she.area() == maximum:
                answer.append(she)
            else:
                pass
        return tuple(answer)


#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    try:
        textfile = open(filename,"r")
    except FileNotFoundError:
        print("There is no shapes.txt!")
        return None
    readshape = ShapeSet()
    for line in textfile:
        obj = (line.rstrip('\n')).split(',')
        # print(obj)
        if obj[0] == "circle":
            component = Circle(float(obj[1]))
            readshape.addShape(component)
        elif obj[0] == "square":
            component = Square(float(obj[1]))
            readshape.addShape(component)
        elif obj[0] == "triangle":
            # print(obj)
            # print(Triangle(float(obj[1]),float(obj[2])))
            component = Triangle(float(obj[1]),float(obj[2]))
            readshape.addShape(component)
    return readshape

