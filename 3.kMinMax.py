def kMax(k, arr):
    arr.sort(reverse = True)    # Sort in descendig order
    print("Kth maximum element= ", arr[k-1])

def kMin(k, arr):
    arr.sort()  # Sort in ascendig order
    print("Kth minimum element", arr[k-1])

arr = [1, 7, 6, 8, 9, 2, 4, 5, 3, 0]
k = 2

kMax(k, arr)
kMin(k, arr)