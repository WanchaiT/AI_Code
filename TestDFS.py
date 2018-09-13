class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item ):
        self.items.insert(0,item)
        #print(item)
        #self.show()

    def add(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)


def findPath(graph, start, end, path=[]):

    path = path + [start]
    if start == end:
        return [path]

    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))



    #print(queue.)

'''q=Queue()
q.enqueue(4)
q.enqueue('dog')
q.add('6')
q.enqueue('cat')
out = q.dequeue()
print(out)
q.show()
q.enqueue(True)
print(q.isEmpty())
'''


numToChar = {   "1" : "a",
                "2" : "b",
                "3" : "c",
                "4" : "d",
                "5" : "e",
                "6" : "f",
                "7" : "g",
                "8" : "h",
                "9" : "i",
                "10" : "j",
                "11" : "k",
                "12" : "l",
                "13" : "m",
                "14" : "n"
            }

graph = {   's' : set(['a','d','c','b']),
            'd' : set(['e']),
            'e' : set(['f','g']),
            'f' : set(['j']),
            'g' : set(['h']),
            'j' : set(['i']),
            'h' : set(['i']),
            'i' : set(['k']),
            'k' : set(['goal']),
            'goal' : set(['m','n'])
        }

Go = "Go"
Gr = 'Gr'
As = "As"
Fo = 'Fo'

s = [set({"Go","Gr","As","Fo"}), set({})]
a = [set({"Go","Gr"}), set({"As","Fo"})]
b = [set({"Go","Gr","Fo"}), set({"As"})]
c = [set({"Go","Fo"}), set({"As","Gr"})]
d = [set({"Gr","Fo"}), set({"As","Go"})]
e = [set({"As","Gr","Fo"}), set({"Go"})]
f = [set({"Gr"}), set({"As","Go","Fo"})]
g = [set({"Fo"}), set({"As","Go","Gr"})]
h = [set({"As","Go","Fo"}), set({"Gr"})]
i = [set({"Go"}), set({"As","Fo","Gr"})]
j = [set({"As","Go","Gr"}), set({"Fo"})]
k = [set({"As","Go"}), set({"Gr","Fo"})]
l = [set({"As","Fo"}), set({"Go","Gr"})]
m = [set({"As"}), set({"Go","Gr","Fo"})]
n = [set({"As","Gr"}), set({"Go","Fo"})]
goal = [set({}), set({"As","Go","Gr","Fo"})]
# list node
s = [set({Go,Gr,As,Fo}), set({})]

goal = [set({}), set({As,Go,Gr,Fo})]

queue = Queue()

list(dfs_paths(graph,s,goal))
queue.enqueue(graph)
#queue.show()
#findPath(graph ,s,goal)
#queue.show()

'''queue = Queue()
count = 1
n = {}  # dict
n[str(count)] = s
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1

n[str(count)] = a
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1

n[str(count)] = b
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1

n[str(count)] = c
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1

n[str(count)] = d
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1

n[str(count)] = e
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1

n[str(count)] = f
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1

n[str(count)] = g
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1

n[str(count)] = b
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1'''
