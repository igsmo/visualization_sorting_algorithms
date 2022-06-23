def bubble_sort(arr):
    n = len(arr)

    for i in range(n-1):
        done_swapping = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                done_swapping = True
                arr[j], arr[j+1] = arr[j+1], arr[j]

        if not done_swapping:
            return

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_i = i
        
        for j in range(i+1, n):
            if arr[min_i] > arr[j]:
                min_i = j

        arr[i], arr[min_i] = arr[min_i], arr[i]

def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):

        key = arr[i]

        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key


def merge_sort(arr):
    n = len(arr)

    if n > 1:

        mid = n//2

        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i <len(L) and j <len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[i]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

arr = [123, 231, 5612, 2]
merge_sort(arr)
print(arr)
    































