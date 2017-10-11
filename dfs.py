__author__ = "XunFan Zhou"
# UPI: xzho684
# ID: 147040383

# start by first node appearing in text file ie the first line as start node for dfs search
# use stack for the output tracking
# use dictionary with node number as key and colour as value for colour tracking
# note white will be not visited grey will be visited and black will be finished
# change node to grey from white if being visited
# change node to black if all neighbours are grey or black
# output style will be index 0 for first finished black node then increment by 1
# if stack is empty check if there is still white nodes and if yes separate trees by new line
# search dictionary by node value using incrementation to find start of new tree
# if current node is black increment by one !!!note there should be no grey nodes at this point and then
# if the node key value doesn't exist in dictionary then that
# node will be start of new tree which is current incrementation



class Stack:
    '''The class Stack will create a stack object as a list'''
    def __init__(self):
        '''This function is the initializer for the class Stack and defines the stack as a empty list'''
        self.stack = []

    def is_empty(self):
        '''This function returns True if there are no elements in the stack'''
        return len(self.stack) == 0

    def push(self, item):
        '''This item appends an item to the top of the stack'''
        return self.stack.append(item)

    def pop(self):
        '''This function deletes the item at the top of the stack and returns that element'''
        return self.stack.pop()

    def peek(self):
        '''This function checks what the element is at the top of the stack'''
        return self.stack[len(self.stack) - 1]

    def size(self):
        '''This function will return the amount of elements in the stack'''
        return len(self.stack)