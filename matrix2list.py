__author__ = "XunFan Zhou"
# UPI: xzho684
# ID: 147040383
def convert_to_list():
    temp = []
    output = []
    index_count = 0
    file = open('matrix.txt', 'r')
    data = file.readlines()

    for line in data:
        for index in line:
            if index == "1":
                temp.append(index_count // 2)
            index_count += 1
        output.append(temp)
        temp = []
        index_count = 0

    outfile = open("list.txt", 'w')
    for row in output:
        outfile.write(",".join(repr(column) for column in row) + "\n")

convert_to_list()
