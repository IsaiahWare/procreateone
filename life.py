from god import Printer

# Proof of Concept for Life.
# Doesn't actually work.

def life(n, L, G):
    seed(n, L, G, fermentation(1))


def fermentation(DNA):
    return DNA # First came DNA.


def seed(n, L, G, c):
    return Printer.run(n, L, G, c, True) # Then came the seed.

if __name__ == '__main__':
    seed("a.txt", 1, 1, 1)