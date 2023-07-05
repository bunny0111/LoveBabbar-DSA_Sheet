def getminmax(arr):
    arr.sort()
    print(arr)
    minmax = {"min": arr[0], "max": arr[-1]}
    return minmax
arr = [1000, 11, 445, 1, 330, 3000]
minmax = getminmax(arr)
print("Minimum Element= ", minmax["min"])
print("Maximum Element= ", minmax["max"])