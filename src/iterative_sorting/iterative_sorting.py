# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        smallest_index = i

        for j in range(i, len(arr)):

            if arr[j] < arr [smallest_index]:
                smallest_index = j

        arr[smallest_index], arr[i] = arr[i], arr[smallest_index]

    return arr


# TO-DO:  implement the Bubble Sort function below
"""
refer to https://en.wikipedia.org/wiki/Bubble_sort for visualization of algorithm

A single loop in bubble sort goes through every pair inside the list (compares i to i+1)
Switches values if i+1 is smaller than i

For the first loop, this has the effect of pushing the largest value to the end of the list

The second loop does the same. But instead of moving the largest value to the 
last index, it moves the second largest value to then 2nd to last position.

So by continually looping, we will eventually push the smallest value to the first index.


Setting up the basic loop is simple.
for i in range(0, len(array)):
    if arr[i] > arr[i+1]:
        arr[i], arr[i+1] = arr[i+1], arr[i]


How do you run this enough times to sort the whole list?
Since we push the largest value to the end, each loop should reduce the length of the unsorted array by 1. 
i.e. after the first loop, the largest value is in the last index so we stop caring about that index.

So we can loop backwards going from len(array) to 0.
"""
def bubble_sort(arr):
    
    # Run the loop enough times, reducing the length of the array every time (see explanation above)
    for j in range(len(arr), 0, -1):
        
        # After every iteration of this loop, the largest value of the remaining array 
        # will be moved to the end (see explanation above)
        for i in range(0, j-1):

            # if i > i+1, swap the values (move the larger one to the right)
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        
    return arr

#arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
#print(bubble_sort(arr))

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
