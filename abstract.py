from blocks import *
from random import randint

class Anything: # Everything shouldn't have access to Anything
    def __init__(self):
        self.matter = Matter()

    def exist(self):
        coordinate = Coordinate(0,1)

        atom = self.time_cycle(0, coordinate)
        self.matter.add(atom) 
        return self.matter # return all matter in this Reality
    
    def time_cycle(self, dimension, coordinate):
        choice = randint(0, 1) # TODO Simulate randint(0,1) using time cycles

        if choice:
            self.time_cycle(dimension+1, coordinate)
            coordinate.ends += 1

        return Atom(coordinate)
    
class All:
    def be(Limit=0, echo=False):
        dna = DNA()

        while Limit:
            matter = Anything().exist()
            dna.add(matter)
            Limit -= 1

        return dna

class Outcomes:
    def __init__(self):
        self.molecules = []

    def add(self, molecule):
        self.molecules.append(molecule)

    def __repr__(self):
        return ''.join(self.molecules)
    
    def __str__(self):
        print(self.molecules)
        return ''.join(self.molecules)