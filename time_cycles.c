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

    // There just was a beginning.
    // That's it.
    // We are trapped in the scope of time.

    e.beginnings = 1;
    e.ends = 0;
    time_cycle(0,0,e,3);
    printf("%d ends for %d beginnings for a {%d / %d * 100}\% chance of going out of existence.", e.ends , e.beginnings, e.ends, e.beginnings);
}

int main() {
    anything();
    return 0;
}

