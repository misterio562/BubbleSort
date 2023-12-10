def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range (0, n-i-1):
            if array[j] > array[j+1]:
                array[j] , array[j+1] = array[j+1], array[j]

mi_list = [45, 1, 47, 89, 100]
bubble_sort(mi_list)

print(mi_list)