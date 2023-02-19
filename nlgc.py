from abstract import *
from blocks import *
from sys import argv

class Printer:
    def run(name, Limit, Generations, connect, echo):
        with open(name, 'a' if connect else 'w') as name:
            outcomes = Printer.generate(Limit, Generations, echo)
            print(outcomes, file=name)

    def generate(Limit, Generations, echo=False):
        outcomes = Outcomes()
        g = 0

        while g < Generations:
            molecule = All.be(Limit, echo)
            outcomes.add(molecule)
            g += 1
            print(f'Generation {g}/{Generations}')

        return outcomes

def start():
    if len(argv) != 11:
        print(f'Expected {11} arguments, but received {len(argv)}.')
        return

    n = argv[1]
    L = argv[3]
    G = argv[5]
    c = argv[7]  # Superposition (replace c with Superposition)
    e = argv[9]  # echo (replace e with echo)

    if n != "-n" or L != "-L" or G != "-G" or c != "-c" or e != "-e":
        print(f'Usage: python3 nlgc.py -n a.txt -L 1 -G 1 -c 1 -e 1')
        return

    name = argv[2]
    Limit = int(argv[4])
    Generations = int(argv[6])
    connect = int(argv[8])
    echo = int(argv[10])
    Printer.run(name, Limit, Generations, connect, echo)

if __name__ == '__main__':
    start()
