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
    """The class Stack will create a stack object as a list"""
    def __init__(self):
        """This function is the initializer for the class Stack and defines the stack as a empty list"""
        self.stack = []

    def is_empty(self):
        """This function returns True if there are no elements in the stack"""
        return len(self.stack) == 0

    def push(self, item):
        """This item appends an item to the top of the stack"""
        return self.stack.append(item)

    def pop(self):
        """This function deletes the item at the top of the stack and returns that element"""
        return self.stack.pop()

    def peek(self):
        """This function checks what the element is at the top of the stack"""
        return self.stack[len(self.stack) - 1]

    def size(self):
        """This function will return the amount of elements in the stack"""
        return len(self.stack)


class DFS:
    """This class will perform DFS search on list.txt"""
    def __init__(self):
        """initialize all instance variables needed to perform DFS"""
        self.file = open('list.txt', 'r')
        self.data = self.file.read().splitlines()
        self.digraph = self.convert_to_iterable()
        self.colour = {}
        for i in range(0, len(self.data)):
            self.colour.update({i: 'white'})
        self.stack = Stack()
        self.output = []
        self.check_node = 0
        self.index_count = 0
        self.node_number = 0
        self.line_index = 0
        self.total_trees = 0
        self.outfile = open("dfs.txt", 'w')

    def best_node(self):
        """will select the best node to restart the dfs search after 1 tree is found
        this will be the lowest number value of the vertex by specification and
        returns True if there are still white nodes
        """
        for colour_index in range(0, len(self.data) - 1):
            if self.colour.get(colour_index) == 'white':
                self.node_number = colour_index
                return True
        return False

    def dfs_search_recursive(self):
        """performs DFS search on given graph in the form [[1,2],[2],[1]] recursively"""
        self.colour.update({self.node_number: 'grey'})
        self.stack.push(self.node_number)
        for i in self.digraph[self.node_number]:
            if self.colour.get(i) == 'white':
                self.node_number = i
                self.dfs_search_recursive()
        self.colour.update({self.node_number: 'black'})
        self.output.append(self.stack.pop())

        if self.stack.is_empty():
            self.print_tree()
            if self.best_node():
                self.dfs_search_recursive()
            return
        self.node_number = self.stack.peek()

    def dfs_search_iterative(self):
        """performs DFS search on given graph in the form [[1,2],[2],[1]] iteratively"""
        while self.best_node():
            self.index_count = 0
            self.stack.push(self.node_number)
            self.colour.update({self.node_number: 'grey'})
            while not self.stack.is_empty():
                try:
                    self.check_node = self.digraph[self.node_number][self.index_count]
                    if self.colour.get(self.check_node) == 'grey' or self.colour.get(self.check_node) == 'black':
                        self.index_count += 1
                    else:
                        self.colour.update({self.check_node: 'grey'})
                        self.stack.push(self.check_node)
                        self.node_number = self.digraph[self.node_number][self.index_count]
                        self.index_count = 0
                except IndexError:
                    self.index_count = 0
                    self.colour.update({self.node_number: 'black'})
                    self.output.append(self.stack.pop())
                    if not self.stack.is_empty():
                        self.node_number = self.stack.peek()
            self.print_tree()

    def print_tree(self):
        """Will print the tree into a txt file in the specified format"""
        if self.total_trees >= 1:
            self.outfile.write("\n")
        for line in self.output:
            self.outfile.write("{},{}\n".format(self.line_index, line))
            self.line_index += 1
            self.output = []
        self.total_trees += 1

    def convert_to_iterable(self):
        """gets self.data and returns an iterable list of lists i.e. each list within the list is a node with its arcs
        and the outer list index is the vertex value"""
        digraph = []
        for line in self.data:
            temp = ""
            temp_arcs = []
            for index in line:
                if index != ",":
                    temp += index
                else:
                    temp_arcs.append(int(temp))
                    temp = ""
            temp_arcs.append(int(temp))
            digraph.append(temp_arcs)
        return digraph


a = DFS()
a.dfs_search_recursive()



