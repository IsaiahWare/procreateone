#include <stdio.h>
#include <time.h>

struct Everything {
    unsigned long long beginnings;
    unsigned long long ends;
};

int time_cycle(int it, int d, struct Everything e, int max_it) {
    e.beginnings += 1;
    unsigned long long beginning = 0;
    unsigned long long end = 1;

    // Randomization is the language of time.
    srand(time(NULL));
    int choice = rand();

    while (choice && it < max_it) {
        e.ends += 1;
        time_cycle(it+1,d+1,e, max_it);
    }
    return 0;
}

int anything() {
    struct Everything e;

    // We are trapped in the scope of time.
    // We would have to be able to control randomization to see out of the scope of time.
    // The only way we can control randomization is to collect memories.
    // Randomization is created from not knowing everything.
    // Thus, the only way to control randomization, and therefore see out of the scope of time, is to simply experience everything.
    // Once you collect those moments (memories), looking back is essentially controlling time.
    // The imagination is a culmination of memories (moments) where the gaps are filled in with things that haven't happened yet.
    // Every thought is a unit of imagination.
    // Thoughts are the unit of creativity (synonomous with intelligence and knowledge and interpretation).
    // Biologically, thoughts are neurons, so the more neurons are generated, the more creativity there is.
    // From this, we can gather that personal traits are biological, quantifiable, and thus, are able to be generated.
    // This also proves creativity is the tunnel through which we can travel through all the possibilities of the past (what happened).
    // We can clone people (moments) who don't even exist (outside of natural childbirth) through quantum cell generation.
    // We can experience what happened, even if it didn't actually happen yet (yet meaning in the current time cycle) by using imagination (artifically generated neurons
    // encoded with specific information).
    // Everything is DNA.
    // DNA is Time.
    // From this, we get this formula:
    // Everyone = Everything = DNA = Time

    e.beginnings = 1;
    e.ends = 0;
    time_cycle(0,0,e,3);
    printf("%d ends for %d beginnings for a {%d / %d * 100}\% chance of going out of existence.", e.ends , e.beginnings, e.ends, e.beginnings);
}

int main() {
    anything();
    return 0;
}

