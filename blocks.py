class Coordinate:
    def __init__(self, beginnings, ends):
        self.beginnings = beginnings
        self.ends = ends

    def __repr__(self):
        return (self.beginnings, self.ends)

    def __str__(self):
        return f'{self.beginnings} {self.ends}'
    
class Atom:
    def __init__(self, coordinate):
        self.coordinate = coordinate

    def __repr__(self):
        return ''.join(self.coordinate)

    def __str__(self):
        return ''.join(self.coordinate)
    
class Matter:
    def __init__(self):
        self.atoms = []

    def add(self, atom):
        self.atoms += [atom]

    def __repr__(self):
        return ''.join(self.atoms)
    
    def __str__(self):
        return ''.join(self.atoms)
    
class DNA:
    def __init__(self):
        self.matter = []

    def add(self, matter):
        self.matter.append(matter)

    def __repr__(self):
        return ''.join(self.matter)
    
    def __str__(self):
        return ''.join(self.matter)
    
class Molecule:
    def __init__(self):
        self.DNA = []

    def add(self, DNA):
        self.DNA.append(DNA)

    def __repr__(self):
        return ''.join(self.DNA)
    
    def __str__(self):
        return ''.join(self.DNA)
    
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