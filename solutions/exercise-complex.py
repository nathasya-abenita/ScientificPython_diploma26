# Exercise 7:
# Create your own class for complex numbers. Make sure all the arithmetic operations work and that you can print it.

class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # def add(self, other):
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    # def sub(self, other):
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    # def mul(self, other):
    def __mul__(self, other):
        return Complex(self.real*other.real - self.imag*other.imag, self.real*other.imag + self.imag*other.real)

    # def div(self, other):
    def __truediv__(self, other):
        return Complex((self.real*other.real + self.imag*other.imag)/(other.real**2 + other.imag**2), (self.imag*other.real - self.real*other.imag)/(other.real**2 + other.imag**2))

    # def print(self):
    def __str__(self):
        return str(self.real) + " + " + str(self.imag) + "i"
    
if __name__ == "__main__":
    a = Complex(1, 2)
    b = Complex(3, 4)
    print("a: ", a)
    print("b: ", b)
    print("a + b: ", a + b)
    print("a - b: ", a - b)
    print("a * b: ", a * b)
    print("a / b: ", a / b)


    

