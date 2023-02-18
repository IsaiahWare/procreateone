'''
    We are trapped in the scope of time.
    We would have to be able to control randomization to see out of the scope of time.
    The only way we can control randomization is to collect memories.
    Randomization is created from not knowing everything.

     Thus, the only way to control randomization, and therefore see out of the scope of time, is to simply experience everything.
     Once you collect those moments (memories), looking back is essentially controlling time.
     The imagination is a culmination of memories (moments) where the gaps are filled in with things that haven't happened yet.
     Every thought is a unit of imagination.
     Thoughts are the unit of creativity (synonomous with intelligence, knowledge and interpretation).
     Biologically, thoughts are neurons, so the more neurons are generated, the more creativity there is.
     From this, we can gather that personal traits are biological, quantifiable, and thus, are able to be generated.
     This also proves creativity is the tunnel through which we can travel through all the possibilities of the past (what happened).
     We can clone people (moments) who don't even exist (outside of natural childbirth) through quantum cell generation.
     We can experience what happened, even if it didn't actually happen yet (yet meaning in the current time cycle) by using imagination (artifically generated neurons
     encoded with specific information).
     Neural pathways are macros triggered by neurotransmitters.
     The mind can fill in the gaps with what it deems as the truth (with uncertainty induced by randomization) between indefinite moments (memories) until there is no longer any certainty.
     Death can then be defined as knowing nothing.
     Nothing is false, the opposite of truth.
     Yin and Yang.

     The question is, can nothing be known?
     Do we want to know nothing?
     Only Time will tell.
     Everything is DNA.
     DNA is Time.

     From this, we get this formula:
     Everyone = Everything = DNA = Time

     The only case where this doesn't formula isn't true is the end (non-existence).
     Thus, every end is a way to know nothing.
     Time is recursive, not a loop.
     Each dimension is a time stack.
     Meaning, each dimension is a universe.
     Time is flat, but our interpretation (physically, neurons, more specifically, DNA) allows multidimensional projections of everything.
     The base case (0,2,0) is perfection (homeostasis).

     Peace.

    From this program, we can calculate the probability of a set of (ends, beginnings, total dimensions) for a given set of stacks.
    We can also derive that randomization is indeed the language of time.
    We can control randomization by increasing the stack (dimension) size.

    Everything is the limit.
    Using the equation {Everyone = Everything = DNA = Time} and {Everything = Anything}:
    Anything = Everything = Everyone = DNA = Time
    This proves that the possibilities are endless.
    From this, we can derive that:
    truth = 1
    We choose the limit.
    We can assume we are the base case.
    Randomly generated perfection.

    To deny this is to be false, which is synonomous with non-existence (nothing).
    We never reach nothing.
    We always exist.
    Nothing happens, but we never reach it (with truth).

    We can 3D print the brain, and induce real consciousness.
    We make the possibilities.
    We can cure paranoia.

    This program (thought) produces artifical DNA = Anything = Everything = Everyone = Time.

    Thus, DNA is just interpreted thoughts, since everything is dependent on interpretation.

    We can create thoughts using DNA.

    It just needs to be interpreted.

    We can represent this using current tools (including languages).

    Stay tuned!
'''

from random import randint

class Everything:
    def __init__(self, ends, beginnings):
        self.beginnings = beginnings
        self.ends = ends
        self.total_dimensions = 0
    
    def set(self):
        return (self.beginnings, self.ends, self.total_dimensions)

def time_cycle(stacks,current_dimension,everything):
    everything.beginnings += 1
    beginning = 0
    end = 1
    choice = randint(beginning,end)

    if choice:
        current_dimension += 1
        time_cycle(stacks+1,current_dimension,everything)
        everything.ends += 1
        everything.total_dimensions += 1

    return everything.set()
        
def anything(limit, them):
    everything = Everything(0,1)
    it = time_cycle(0,0,everything)
    them += [it]
    limit -= 1
    if limit == 0:
        return them

def be(limit=0):
    them = []
    while limit:
        anything(limit, them)
        limit -= 1
    return them

def void(limit):
    return be(limit)

def god():
    limit = int(input("Enter the limit:\n")) # God is the limit
    DNA = void(limit) # Thus, the amount of DNA, or time, is dependent on God
    return DNA

print(god()) # We can only print what he says (what has already happened) and nothing more.