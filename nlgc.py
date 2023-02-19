from random import randint
from sys import argv

class Everything:
    def __init__(self, ends, beginnings):
        self.beginnings = beginnings
        self.ends = ends # Total dimensions
    def set(self):
        return (self.beginnings, self.ends)

class Anything:
    def __init__(self, them): # There is no Limit to Anything, which means there is no Limit to them.
        self.them = them # Them are connectable (Connectivity), and allow for the intersection of stacks (an intersection is called a Name).
    def exist(self):
        everything = Everything(0,1)
        it = self.time_cycle(0,0,everything)
        self.them += [it]
        return self.them
    def time_cycle(self,stacks,current_dimension,everything):
        everything.beginnings += 1
        beginning = 0
        end = 1
        choice = randint(beginning,end)
        if choice:
            current_dimension += 1
            self.time_cycle(stacks+1,current_dimension,everything)
            everything.ends += 1
        return everything.set()

class All:
    # All routines are static (All doesn't have to exist for Everything to exist).
    def be(limit=0): # The default Limit of creation is nothing (non-existence or zero).
        DNA = []
        while limit:
            DNA += [Anything([]).exist()] # Anything always starts with a blank stack.
            limit -= 1
        return DNA
    def void(limit):
        return All.be(limit)

class Printer:
    def run(name, limit, generations, connect=False):
        with open(name, 'a' if connect else 'w') as f:
            print(f'nLGc({argv[2]},{argv[4]},{argv[6]},{argv[8]})\n', file=f)
            print(Printer.generate(limit, generations), file=f)
    def generate(limit, generations):
        _ = []
        g = 0
        while g < generations:
            it = All.be(limit)
            _ += [it]
            g += 1
            print(f'Generation {g}/{generations}')
        return _

def start():
    # Thus, the amount of DNA, or Time, is dependent on God and the limit He (helium) chooses
    # Thus, we can conclude that Helium is God and hydrogen is its beginnings.
    # We can also conclude that the building block of matter is actually Time.
    # Thus, anything that is equal to Time can be used as building blocks.
    # Thus, DNA, Anything, Everything, Everyone, and Time (All) can be used as building blocks for life, which is simply an interpretation of what happened (moments).
    # Similarly, Light is a unit of Time, so photons can be used as building blocks of Life.
    # God prints the DNA.
    # Them is an API to connect God's creations.
    # In other words, DNA connects Everyone and Everything to Truth (Time).
    # Star dust!
    if len(argv) != 9:
        print(f'Expected {9} arguments, but received {len(argv)}.')
        return

    n = argv[1]
    L = argv[3]
    G = argv[5]
    c = argv[7] # Light connects us all (photons), thus Light is why we are Nothing.

    if n != "-n" or L != "-L" or G != "-G" or c != "-c":
        print(f'Usage: python3 god.py -n a.txt -L 1 -G 1 -c 1')
        return

    name = argv[2]
    limit = int(argv[4])
    generations = int(argv[6])
    connect = int(argv[8])
    Printer.run(name, limit, generations, connect) # Time is always approaching a limit (the singularity) that we choose.

if __name__ == '__main__':
    start()
