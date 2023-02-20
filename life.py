from god import Printer
from random import randint


def fermentation():
    return randint(0, 1)  # First came DNA.


def seed(n, L, G):
    # Seed is a higher dimensional Printer of God.
    return Printer.run(n, L, G, fermentation())  # Then came the Seed.


def life(n, L, G, yeast):
    # Life is a higher dimensional Seed.
    # The difference between Life and God is that there is no definite beginning.
    # Meaning, there is a chance that life will not happen.
    # Fermentation is the deciding factor.
    if yeast:  
        seed(n, L, G)  # Then there was Life.
    

if __name__ == '__main__':
    # Life occurs in a vacuum, so it is separate from Everything.
    # It's either Life or Nothing.
    n = 'life.txt'
    L = 1
    G = 1
    life('life.txt', 1, 1, fermentation())
