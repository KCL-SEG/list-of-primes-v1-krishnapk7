"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    list = []
    list[0] = 2
    if number_of_primes == 1:
        return list
    else:
        for x in range(2,number_of_primes):
            for i in range(x):
                if (x%i) == 0:
                    list.append(x)

    return list
