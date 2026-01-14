class ComplexNumber:
    """ 
    To construct a complex number
    (a + i*b)
    and its arithmetic operation 
    """

    def __init__ (self, a=0, b=0):
        self.a = a
        self.b = b

    def __add__ (self, other):
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNumber(a, b)
    
    def __sub__ (self, other):
        a = self.a - other.a
        b = self.b - other.b
        return ComplexNumber(a, b)
    
    def __mul__ (self, other):
        a, b = self.a, self.b
        c, d = other.a, other.b
        return ComplexNumber(
            a*c - b*d,
            b*c + a*d
            )
    
    def __truediv__ (self, other):
        if (other.a == 0) and (other.b == 0):
            print('Division with zero!')
        else:
            a, b = self.a, self.b
            c, d = other.a, other.b
            denom = c**2 + d**2
            return ComplexNumber(
                (a*c + b*d) / denom, 
                (b*c - a*d) / denom
                )
    
    def __str__ (self):
        return f"Complex number with real part of {self.a} and imaginary part of {self.b}"
    
if __name__ == '__main__':

    # Define complex numbers using the class
    a, b, c, d = 1, 2, 3, 2
    num1 = ComplexNumber(a, b)
    num2 = ComplexNumber(c, d)

    # Test sum
    print(num1 + num2)
    print(complex(a, b) + complex(c, d))

    # Test substraction
    print(num1 - num2)
    print(complex(a, b) - complex(c, d))

    # Test multiplication
    print(num1 * num2)
    print(complex(a, b) * complex(c, d))

    # Test division
    print(num1 / num2)
    print(complex(a, b) / complex(c, d))

    # Test silly division
    num1 / ComplexNumber(0, 0)