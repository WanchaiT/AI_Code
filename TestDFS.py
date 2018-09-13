class Queue:
    def __init__(self):
        self.items = {}

    def isEmpty(self):
        return self.items == {}

    def enqueue(self, item ,num):
        self.items[str(num)] = item
        print(item)
        #self.show()

    def add(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def show(self):
        i = 1
        item =
        for item in self.items[str(i)] :
            #print(item)
            print(type(item))


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

s=[set({"Go","Gr","As","Fo"}),set({})]
a=[set({"Go","Gr"}),set({"As","Fo"})]
b=[set({"Go","Gr","Fo"}),set({"As"})]
c=[set({"Go","Fo"}),set({"As","Gr"})]
d=[set({"Gr","Fo"}),set({"As","Go"})]
e=[set({"As","Gr","Fo"}),set({"Go"})]
f=[set({"Gr"}),set({"As","Go","Fo"})]
g=[set({"Fo"}),set({"As","Go","Gr"})]
h=[set({"As","Go","Fo"}),set({"Gr"})]
i=[set({"Go"}),set({"As","Fo","Gr"})]
j=[set({"As","Go","Gr"}),set({"Fo"})]
k=[set({"As","Go"}),set({"Gr","Fo"})]
l=[set({"As","Fo"}),set({"Go","Gr"})]
m=[set(){"As"}),set({"Go","Gr","Fo"})]
n=[set({"As","Gr"}),set({"Go","Fo"})]
goal = [set({}),set({"As","Go","Gr","Fo"})]


Go = "Go"
Gr = 'Gr'
As = "As"
Fo = 'Fo'

queue = Queue()
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
count = count+1
