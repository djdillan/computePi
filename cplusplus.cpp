#include <stdlib.h>
#include <omp.h>
#include <math.h>
#include <stdio.h>
#include <time.h>

int main(int argc, char *argv[]) {
    int samp;
    int i;
    int noThread;
    int c = 0;
    clock_t first, last;
    double x;
    double y;
    double f;
    double span;
    double calcPi;

    scanf("%d", &samp); // enter number of samples
    printf("\n");
    scanf("%d", &noThread); // enter threads
    printf("\n");

    first = clock(); // first time collection
    #pragma omp parallel firstprivate(x, y, f, i) shared(c) num_threads(noThread)
    {
        // points of circle in parallel by number of threads
        srand((int)time(NULL) ^ omp_get_thread_num()); // rand no. generator and returns thread number of calling thread
        for (i = 0; i < samp; i++) {
            x = (double)rand() / (double)RAND_MAX; // random x coordinate within square
            y = (double)rand() / (double)RAND_MAX; // random y coordinate within square
            f = pow((x * x) + (y * y), 0.5);
            if (f <= 1) {
                c++;
            }
        }
    }
    calcPi = ((double)c / (double)(samp * noThread)) * 4; // Calculating value for Pi
    last = clock(); // last time collection
    span = ((double)last - first) / CLOCKS_PER_SEC; // working out total time taken for calculation alone
    printf("Pi is: %f\n", calcPi);
    printf("Time taken: %f\n", span);
    return 0;
}

