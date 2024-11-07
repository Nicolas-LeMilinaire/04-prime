"""
    module docstring
"""

from math import sqrt

#### Fonction secondaire


def isprime(p):
    '''
        dfghjkjllkjhgf
    '''

    if p in (0, 1):
        return False

    for i in range(2, int(sqrt(p)+1)):

        if p % i == 0 :
            return False

    return True

#### Fonction principale



def main():

    """
    module docstring
    """

    # vos appels à la fonction secondaire ici
    isprime(5)
    isprime(69)
    isprime(733)
    isprime(1111)
    isprime(2223)

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
