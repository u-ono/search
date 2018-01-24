class Node:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ops = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]

    def expand(self):
        node_list = []
        for (xi, yi) in self.ops:
            new_node = Node(self.x + xi, self.y + yi)
            if new_node.in_area():
                node_list.append(new_node)
        return node_list

    def in_area(self):
        if self.x == 0 or self.y == 0 or self.x == 8 or self.y == 6:
            return False
        elif (self.x, self.y) in ((5,2),(5,3),(5,4),(5,5)):
            return False
        else:
            return True
                
def search(n0):
    open_list = [n0]
    close_list = []
    solution = []
    while len(open_list) != 0:
        node = open_list.pop(0)
        if node not in close_list:
            solution.append(node)
            if (node.x, node.y) == (7,3):
                return solution
            open_list = appendToLast(node.expand(), open_list)
            close_list.append(node)
    return False

def appendToLast(nodes, ls):
    return ls + nodes
