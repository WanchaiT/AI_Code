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


def findPath(queue,start,end) :
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(queue,node, end, path)
            if newpath: return newpath
    return None


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

graph = {   's' : ['a','d','c','b'],
            'd' : ['e'],
            'e' : ['f','g'],
            'f' : ['j'],
            'g' : ['h'],
            'j' : ['i'],
            'h' : ['i'],
            'i' : ['k'],
            'k' : ['goal'],
            'goal' : ['m','n']
        }

queue = Queue()
queue.enqueue(s)
queue.show()

path = findPath()
