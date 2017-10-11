__author__ = "XunFan Zhou"
# UPI: xzho684
# ID: 147040383

file = open('list.txt', 'r')
data = file.read().splitlines()
temp = ""
output = [[] for i in range(len(data))]
index_count = 0

for line in data:
    for index in line:
        if index != ",":
            temp += index
        else:
            output[int(temp)].append(index_count)
            temp = ""
    output[int(temp)].append(index_count)
    temp = ""
    index_count += 1

outfile = open("reverselist.txt", 'w')
for row in output:
    outfile.write(",".join(repr(column) for column in row) + "\n")
