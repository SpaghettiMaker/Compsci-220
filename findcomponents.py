__author__ = "XunFan Zhou"
# UPI: xzho684
# ID: 147040383
import matrix2list
import list2reverse

matrix2list.convert_to_list()
list2reverse.reverse_list()

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
        """initializes all instance variables needed to perform DFS"""
        self.file_reverse = open('reverselist.txt', 'r')
        self.data_reverse = self.file_reverse.read().splitlines()
        self.digraph_reverse = self.convert_to_iterable(self.data_reverse)
        self.colour_reverse = {}
        for i in range(0, len(self.data_reverse)):
            self.colour_reverse.update({i: 'white'})

        self.file = open('list.txt', 'r')
        self.data = self.file.read().splitlines()
        self.digraph = self.convert_to_iterable(self.data)
        self.colour = {}
        for i in range(0, len(self.data)):
            self.colour.update({i: 'white'})

        self.stack = Stack()
        self.output = []
        self.reverse_order = []
        self.node_number = 0
        self.line_index = 0
        self.total_trees = 0
        self.outfile_reverse = open("dfsreverse.txt", 'w')
        self.outfile = open("components.txt", 'w')

    def best_node_reverse(self):
        """will select the best node to restart the dfs search after 1 tree is found
        this will be the lowest number value of the vertex by specification and
        returns True if there are still white nodes
        """
        for colour_index in range(0, len(self.data_reverse) - 1):
            if self.colour_reverse.get(colour_index) == 'white':
                self.node_number = colour_index
                return True
        return False

    def best_node_strong_component(self):
        """will select the best node to restart strongly connected components search after 1 component is found
        this will be the closest to the bottom of the list from the reverse dfs search and
        returns True if there are still white nodes
        """
        for i in self.reverse_order:
            if self.colour.get(i) == 'white':
                self.node_number = i
                return True
        return False

    def dfs_search_reverse_graph(self):
        """performs DFS search on given graph in the form [[1,2],[2],[1]] recursively"""
        self.colour_reverse.update({self.node_number: 'grey'})
        self.stack.push(self.node_number)
        for i in self.digraph_reverse[self.node_number]:
            if self.colour_reverse.get(i) == 'white':
                self.node_number = i
                self.dfs_search_reverse_graph()
        self.colour_reverse.update({self.node_number: 'black'})
        self.reverse_order.append(self.stack.peek())
        self.output.append(self.stack.pop())

        if self.stack.is_empty():
            self.print_tree_reverse()
            if self.best_node_reverse():
                self.dfs_search_reverse_graph()
            return
        self.node_number = self.stack.peek()

    def search_strongly_connected_components(self):
        """performs DFS search on given graph in the form [[1,2],[2],[1]] recursively to
        find strongly connected components"""
        self.colour.update({self.node_number: 'grey'})
        self.stack.push(self.node_number)
        for i in self.digraph[self.node_number]:
            if self.colour.get(i) == 'white':
                self.node_number = i
                self.search_strongly_connected_components()
        self.colour.update({self.node_number: 'black'})
        self.output.append(self.stack.pop())

        if self.stack.is_empty():
            self.print_strongly_connected_components()
            if self.best_node_strong_component():
                self.search_strongly_connected_components()
            return
        self.node_number = self.stack.peek()

    def print_strongly_connected_components(self):
        """Will print strongly connected components into a txt file in the specified format"""
        self.output.sort()
        self.outfile.write(",".join(repr(i) for i in self.output)+"\n")
        self.output = []

    def print_tree_reverse(self):
        """Will print the tree into a txt file in the specified format"""
        if self.total_trees >= 1:
            self.outfile_reverse.write("\n")
        for line in self.output:
            self.outfile_reverse.write("{},{}\n".format(self.line_index, line))
            self.line_index += 1
            self.output = []
        self.total_trees += 1

    def convert_to_iterable(self, data):
        """gets data and returns an iterable list of lists i.e. each list within the list is a node with its arcs
        and the outer list index is the vertex value"""
        digraph = []
        for line in data:
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

    def reset(self):
        self.reverse_order = self.reverse_order[::-1]
        self.node_number = self.reverse_order[0]


a = DFS()
a.dfs_search_reverse_graph()
a.reset()
a.search_strongly_connected_components()

