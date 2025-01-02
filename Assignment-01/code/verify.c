#include <stdio.h>
#include <math.h>

int main() {
    
double y = M_E;
double x = 1.0;
double h = 0.000001; 
int iterations = 1000000;

 FILE *file = fopen("points.txt", "w");
if (file == NULL){
printf("Error opening file!\n");
return 1;
}

for (int i = 0; i < iterations; i++) {
fprintf(file, "%.6f\t%.6f\n", x, y);
x += h;
y += h *(y*log(y))/x;
}
fclose(file);
return 0;
}

