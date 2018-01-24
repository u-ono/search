class Node:

    def __init__(self, x, y, par=None):
        self.x = x
        self.y = y
        self.ops = [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]
        self.par = par

    def expand(self):
        node_list = []
        for (xi, yi) in self.ops:
            new_node = Node(self.x + xi, self.y + yi, self)
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
                
def search(n0, queue_func):
    open_list = [n0]
    close_list = []
    solution = []
    path = []
    while len(open_list) != 0:
        node = open_list.pop(0)
        if (node.x, node.y) not in close_list:
            path.append((node.x, node.y))
            if (node.x, node.y) == (7,3):
                n = node
                while n.par != None:
                    solution.append((n.par.x, n.par.y))
                    n = n.par
                return solution[::-1], path
            open_list = queue_func(node.expand(), open_list)
            close_list.append((node.x, node.y))
            #print('open_list')
            #for n in open_list:
            #    print('({}, {})'.format(n.x, n.y))
            #print('close_list')
            #for n in close_list:
            #    print(n)
    return False

def appendToLast(nodes, ls):
    return ls + nodes

def insertToHead(nodes, ls):
    return nodes + ls

def sortByEvaluation(nodes, ls):
    return sorted(ls+nodes, key=a_star)

def heuristic_step(node):
    return max(abs(7-node.x), abs(3-node.y))

def heuristic_dist(node):
    return (7-node.x)**2 + (3-node.y)**2

def a_star(node):
    step = 0
    n = node
    while n.par != None:
        step += 1
        n = n.par
    return step + heuristic_dist(node)**0.5
