__author__ = "XunFan Zhou"
# UPI: xzho684
# ID: 147040383
import sys
 
def median_of_three(mylist):
    '''Expects list and will return the median song of the songs time'''
    data = {}
    index = 0
    temp = list(mylist)
    data[temp[0].rpartition('&')[-1]] = mylist[len(mylist) // 2]
    data[temp[0].rpartition('&')[-1]] = mylist[-1]
    data[temp[0].rpartition('&')[-1]] = mylist[0]
    key = sorted(data)
 
    temp_list = [mylist[0], mylist[-1], mylist[len(mylist) // 2]]
    x = temp_list.index(str(data.get(key[1])))
    if x == 1:
        index = len(mylist)
    if x == 2:
        index = mylist[len(mylist) // 2]
    if len(key) == 1:
        return data.get(key[0]), index  # if songs have same running time then they will have same key
    return data.get(key[1]), index
 
def quick_sort(a_list):
    '''Sorts list of specified data using the quicksort method'''
    if len(a_list) < 2:
        return a_list
 
    partition = median_of_three(a_list)
    pivot = partition[0]
    left = []
    right = []
    a_list.pop(partition[1])
 
    for item in a_list:
        if item.rpartition('&')[-1] == pivot.rpartition('&')[-1]:  # checking if song time is same length
            if item < pivot:  # if same length compare with lexicographic order
                left.append(item)
            else:
                right.append(item)
        else:
            if item.rpartition('&')[-1] > pivot.rpartition('&')[-1]:
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