def sort(lst):
    # Note: We cannot use sort function
    # we will find the count of 0,1,2 in the given list with help of count function

    count_0 = lst.count(0)
    count_1 = lst.count(1)
    count_2 = lst.count(2)

    # declare new list
    new_list = []

    for i in range(count_0):
        new_list.append(0)

    for i in range(count_1):
        new_list.append(1)

    for i in range(count_2):
        new_list.append(2)

    print("After Sorting-", new_list)

array = [1, 2, 0, 2, 1, 0, 2, 1, 0, 2, 0, 1]
print("Before Sorting-", array)
# call function
sort(array)