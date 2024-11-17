#include <stdio.h>

int findLRU(int time[], int n) {
    int lru_index = 0;
    for (int i = 1; i < n; i++) {
        if (time[i] < time[lru_index]) {
            lru_index = i;
        }
    }
    return lru_index;
}

int main() {
    int frames[10], time[10], pages[30];
    int numFrames, numPages, pageFaults = 0, counter = 0;

    printf("Enter the number of frames: ");
    scanf("%d", &numFrames);

    printf("Enter the number of pages: ");
    scanf("%d", &numPages);

    printf("Enter the page references:\n");
    for (int i = 0; i < numPages; i++) {
        scanf("%d", &pages[i]);
    }

    // Initialize frames to -1 (indicating empty)
    for (int i = 0; i < numFrames; i++) {
        frames[i] = -1;
    }

    for (int i = 0; i < numPages; i++) {
        int found = 0;

        // Check if the page is already in frames
        for (int j = 0; j < numFrames; j++) {
            if (frames[j] == pages[i]) {
                found = 1;
                time[j] = ++counter;  // Update time for the accessed page
                break;
            }
        }

        // If page is not in frames, replace the least recently used page
        if (!found) {
            int lru_index;

            // Find an empty frame, or if full, find the LRU page
            if (frames[i % numFrames] == -1) {
                lru_index = i % numFrames;
            } else {
                lru_index = findLRU(time, numFrames);
            }

            frames[lru_index] = pages[i];  // Replace the page
            time[lru_index] = ++counter;   // Update time for the new page
            pageFaults++;
        }

        // Print the current state of frames
        printf("Frames after page %d: ", pages[i]);
        for (int j = 0; j < numFrames; j++) {
            if (frames[j] != -1)
                printf("%d ", frames[j]);
            else
                printf("- ");
        }
        printf("\n");
    }

    printf("\nTotal Page Faults: %d\n", pageFaults);
    return 0;
}

