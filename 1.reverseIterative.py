# Reverse the array
# Iterative python program to reverse an array

def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
    
# Function to test above code 
A = [1, 2, 3, 4, 5, 6]
print("Original List", A)
reverseList(A, 0, 5)
print("Reverse List= ", A)