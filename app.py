class Rectangle:
    """ This is a class that reports on rectangles """

    def __init__(self, length, width):  # this init sets fields
        self.l = length

    def __init__(self, length, width):  # this init sets fields
        self.l = length
        self.w = width

    def area(self):  # find area
        return self.l * self.w

    def circum(self):  # find circumference
        return (self.l + self.w) * 2

    def isSquare(self):  # check if its a square
        if self.l == self.w:
            return "a square"

    """Question 2 if rectangle is tall or short"""

    def questionTwo(self):
        if self.l < self.w:  # print tall
            return "Tall"

        elif self.l > self.w:  # print short
            return "Short"
        else:
         return False
    """Question 3 for Diagonal"""

    def questionThree(self):
        return (self.l ** 2 + self.w ** 2) ** 0.5  # computes and return calculated Diagonal

    def isSilly(self):  # check if its silly
        if self.l <= 0 or self.w <= 0:
            return "is silly"

        else:
           return "is not silly"


# main method
def main():
    # set fields for three shapes
    s1 = Rectangle(20, 6)
    s2 = Rectangle(2, 20)
    s3 = Rectangle(-10, 10)
    # check on area
    print("Shape 1 area is", s1.area())
    print("Shape 2 area is", s2.area())
    # check on circumference
    print("Shape 1 circumference is", s1.circum())
    print("Shape 2 circumference is", s2.circum())

    # check if shape is silly
    print("Shape 2", s2.isSilly())
    print("Shape 3", s3.isSilly())
    # print(isSilly(-3,0))
    # modification
    print("Shape 1 diagonal is", s2.questionThree())  # check on diagonal modifications
    # see if shape is a square or not
    print("Shape 1 is", s1.questionTwo())
    print("Shape 2 is", s2.questionTwo())
    print("Shape 3 ", s3.questionTwo())


# start process
if __name__ == "__main__":
    main()