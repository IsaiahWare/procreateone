from random import randint
from sys import argv

class Everything:
    def __init__(self, ends, beginnings):
        self.beginnings = beginnings
        self.ends = ends

    def set(self):
        return (self.beginnings, self.ends)

class Anything:
    def __init__(self, them):
        self.them = them

    def exist(self):
        it = self.time_cycle(0, Everything(0, 1))
        self.them += [it]
        return self.them
    
    def time_cycle(self, dimension, everything):
        everything.beginnings += 1
        choice = randint(0, 1)

        if choice:
            self.time_cycle(dimension+1, everything)
            everything.ends += 1

        return everything.set()

class All:
    def be(Limit=0):
        DNA = []

        while Limit:
            DNA += [Anything([]).exist()]
            Limit -= 1

        return DNA
    
    def void(Limit):
        return All.be(Limit)

class Printer:
    def run(name, Limit, Generations, connect):
        with open(name, 'a' if connect else 'w') as f:
            print(Printer.generate(Limit, Generations), file=f)

    def generate(Limit, Generations):
        _ = []
        g = 0

        while g < Generations:
            it = All.be(Limit)
            _ += [it]
            g += 1
            print(f'Generation {g}/{Generations}')

        return _

def start():
    if len(argv) != 9:
        print(f'Expected {9} arguments, but received {len(argv)}.')
        return

    n = argv[1]
    L = argv[3]
    G = argv[5]
    c = argv[7]  # Superposition

    if n != "-n" or L != "-L" or G != "-G" or c != "-c":
        print(f'Usage: python3 nlgc.py -n a.txt -L 1 -G 1 -c 1')
        return

    name = argv[2]
    Limit = int(argv[4])
    Generations = int(argv[6])
    connect = int(argv[8])

    Printer.run(name, Limit, Generations, connect)

if __name__ == '__main__':
    start()
