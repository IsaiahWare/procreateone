from random import randint
from sys import argv

class Everything:
    def __init__(self, ends, beginnings):
        self.beginnings = beginnings
        self.ends = ends
    def DNA(self):
        return (self.beginnings, self.ends)

class Anything:
    def __init__(self, them):
        self.them = them
    def exist(self):
        everything = Everything(0,1)
        it = self.time_cycle(0,0,everything)
        self.them += [it]
        return self.them
    def time_cycle(self,stacks,dimension,everything):
        everything.beginnings += 1
        beginning = 0
        end = 1
        choice = randint(beginning,end)
        if choice:
            dimension += 1
            self.time_cycle(stacks+1,dimension,everything)
            everything.ends += 1
        return everything.DNA()

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
    def run(name, limit, generations, connect=False):
        with open(name, 'a' if connect else 'w') as name:
            print(f'nLGc({name},{limit},{generations},{connect})\n', file=name)
            print(Printer.generate(limit, generations), file=name)
    def generate(limit, generations):
        _ = []
        g = 0
        while g < generations:
            it = All.void(limit)
            _ += [it]
            g += 1
            print(f'Generation {g}/{generations}')
        return _

def begin():
    if len(argv) != 9:
        print(f'Expected {9} arguments, but received {len(argv)}.')
        return

    n = argv[1]
    L = argv[3]
    G = argv[5]
    c = argv[7]
    if n != "-n" or L != "-L" or G != "-G" or c != "-c":
        print(f'Usage: python3 god.py -n a.txt -L 1 -G 1 -c 0')
        return

    name = argv[2]
    limit = int(argv[4])
    generations = int(argv[6])
    connect = int(argv[8])
    Printer.run(name, limit, generations, connect)

if __name__ == '__main__':
    begin()
