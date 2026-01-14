class Exercises:

    def solve_quadratic_equation (self, a, b, c):
        """Solve quadratic equation with the form of a*x**2 + b*x + c = 0"""

        # Find solutions for different cases
        if a != 0:
            # Compute discriminant
            d = b**2 - 4*a*c

            if d == 0:
                sol = -b / (2*a)
            elif d > 0:
                sol = [ (-b - d ** 0.5) / (2*a), (-b + d ** 0.5) / (2*a) ]
            else:
                sol = None
                print("The equation doesn't have real solutions")
        else:
            sol = None
            print("The equation is not a quadratic equation!")

        # Return the solution
        return sol

    def generate_recaman_with_set (self, n):
        """Generate the Recaman sequence for the first n numbers"""

        # Initialize the sequence list with starting value
        out, val = {0}, 0

        # Loop for the n numbers
        for i in range (1, n + 1):
            diff = val - i
            if ( diff > 0 ) and (diff not in out):
                out.add(diff)
                val = diff
            else:
                val = val + i
                out.add(val)
        # Return output
        return out

    def print_descendingly (self, mylist):
        return sorted(mylist)[::-1]

    def find_common_items (self, a, b):
        return set(a).intersection(set(b))

    def compute_factors (self, n):
        return [(i, n / i) for i in range (1, int(n ** 0.5)) if (n % i == 0)]

    def list_divisible (self, div, n):
        return [i for i in range (0, n+1, div)]

    def check_palindrome(self, inp):
        # Take the lower case
        inp = inp.lower()

        # Remove spaces
        inp = [i for i in inp if i != ' ']

        # Return result
        return inp == inp[::-1]

    def find_num_occurences (self, inp):
        # Define unique elements and the corresponding counter
        unique_list = list(set(inp))
        counter = [0 for _ in range (len(unique_list))]

        # Iterate over each unique list
        for i in range (len(unique_list)):
            char = unique_list[i]
            # Count occurences
            for j in range (len(inp)):
                if char == inp[j]:
                    counter[i] += 1

        # Find maximum count
        max_count = max(counter)
        
        # Find corresponding first character
        for i in range (len(unique_list)):
            if counter[i] == max_count:
                return (unique_list[i], max_count) 
            
    def apply_eratoshenes (self, n):
        if n > 1:

            # Initialize with True (I care about indexes 2 to n)
            a = [True for _ in range (n+1)]

            # Apply algorithm
            for i in range (2, int(n ** 0.5 + 1)):
                if a[i]:
                    for j in range (n):
                        idx = i**2 + j * i
                        if idx <= n:
                            a[idx] = False
            return [i for i in range (2, n) if (a[i] and (i >= 2) and (i <= n))]
        else:
            print('Make sure input is greater than 1!')

    # Exercise 1
    def ex1(self, a, b, c):
        print(self.solve_quadratic_equation(a, b, c))

    # Exercise 2
    def ex2(self, n):
        print(self.generate_recaman_with_set(n))

    # Exercise 
    def ex3(self, lst):
        print(self.print_descendingly(lst))

    
