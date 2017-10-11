__author__ = "XunFan Zhou"
# UPI: xzho684
# ID: 147040383
import sys

def quick_sort(a_list):
    '''Sorts list of specified data using the quicksort method'''
    if len(a_list) < 2:
        return a_list

    pivot = a_list[-1]

    left = []
    right = []
    a_list.pop()

    for item in a_list:
        if int(item.rpartition('&')[-1]) == int(pivot.rpartition('&')[-1]):  # checking if song time is same length
            if item < pivot:  # if same length compare with lexicographic order
                left.append(item)
            else:
                right.append(item)
        else:
            if int(item.rpartition('&')[-1]) > int(pivot.rpartition('&')[-1]):
                left.append(item)
            else:
                right.append(item)
    return quick_sort(left) + [pivot] + quick_sort(right)


raw_values = sys.stdin.readlines()
if len(raw_values[-1]) < 3:
    raw_values = raw_values[:-1]

unsorted_data = raw_values[2:]

sorted_data = quick_sort(unsorted_data)

for i in sorted_data[:int(raw_values[0])]:
    sys.stdout.write("{}".format(str(i)))
