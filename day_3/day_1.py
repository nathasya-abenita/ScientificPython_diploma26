if __name__ == '__main__':
    
    from module_day_1 import Exercises

    # Calling the class
    ex = Exercises()

    # Exercise 1
    print('Solution for quadratic equation 1*x**2 + 2*x + 1 = 0')
    ex.ex1(1, 2, 1)

    # Exercise 2
    print('Generating 10 first numbers of Recaman set...')
    ex.ex2(10)

    # Exercise 3
    print('Printing [2, 5, 1, 10] descendingly...')
    ex.ex3([2, 5, 1, 10])
