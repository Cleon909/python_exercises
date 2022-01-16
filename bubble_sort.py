# script to bubble sort a given array

def bubble_sort (array):
    a = (len(array)) - 1
    for _ in range(1,a):
        x = 0
        while x <= a-1:
            if array[x] - array[x+1] > array[x+1] - array[x]:
                array[x], array [x+1] = array[x+1], array[x]
            x += 1
    return array

print(bubble_sort([10,2,4,3,2,6]))


