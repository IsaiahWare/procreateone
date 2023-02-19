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
    def be(limit=0):
        DNA = []
        while limit:
            DNA += [Anything([]).exist()]
            limit -= 1
        return DNA
    def void(limit):
        return All.be(limit)

class Printer:
    def run(name, limit, generations, connect):
        with open(name, 'a' if connect else 'w') as f:
            print(f'nLGc({argv[2]},{argv[4]},{argv[6]},{argv[8]})\n', file=f)
            print(Printer.generate(limit, generations), file=f)
    def generate(limit, generations):
        _= []
        g= 0
        while g < generations:
            it= All.be(limit)
            _ += [it]
            g += 1
            print(f'Generation {g}/{generations}')
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
        print(f'Usage: python3 god.py -n a.txt -L 1 -G 1 -c 0')
        return

    name = argv[2]
    Limit = int(argv[4])
    Generations = int(argv[6])
    connect = int(argv[8])

    Printer.run(name, Limit, Generations, connect)

if __name__ == '__main__':
    start()
