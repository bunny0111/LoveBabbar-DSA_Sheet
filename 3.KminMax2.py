def findK(k, arr, l):
    arr.sort(reverse = True)
    print("Kth maximum= ", arr[k-1])
    print("Kth minimum= ", arr[l-k])

arr = [1, 7, 6, 8, 9, 2, 4, 5, 3, 0]
k = 2
findK(k, arr, len(arr))