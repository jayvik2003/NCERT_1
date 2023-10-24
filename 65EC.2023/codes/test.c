#include <stdio.h>
#include <math.h>

// Function to calculate the LCM of two integers
int findLCM(double a, double b) {
    int max = (a > b) ? a : b;
    int min = (a < b) ? a : b;

    for (int i = 1; i <= max; i++) {
        int multiple = min * i;
        if (multiple % max == 0) {
            return multiple;
        }
    }

    return a * b; // If no LCM is found, return the product of the numbers
}

int main() {
    int n=8;
    double arr[8];
    double arr[] = {0.5, 0.25, 0.125, 0.0625, 0.03125, 0.015626, 0.0078125, 0.0078125};
    
    // Find LCM by converting double to integers
    int lcm_result = 1;
    for (int i = 0; i < n; i++) {
        double int_part = (double)round(arr[i]); // Convert to integer
        lcm_result = findLCM(lcm_result, int_part);
    }

    printf("LCM of the array is: %d\n", lcm_result);

    return 0;
}
