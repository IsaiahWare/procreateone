from god import Printer
from random import randint

def fermentation():
    return randint(0,1) # First came DNA.

def seed(n, L, G):
    return Printer.run(n, L, G, fermentation()) # Then came the seed.

def life(n, L, G, c):
    if c: # Then maybe fermentation occurs.
        seed(n, L, G) # Then there was life.

if __name__ == '__main__':
    life('a.txt',1,1,1)
