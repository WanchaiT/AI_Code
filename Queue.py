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
        item = []
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

Go = "Go"
Gr = 'Gr'
As = "As"
Fo = 'Fo'

queue = Queue()
count = 1
n = {}  # dict
s = [{Go,Gr,As,Fo},{}]  #list  {} = set
n[str(count)] = s
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1

a = [{Go,Gr},{As,Fo}]
n[str(count)] = a
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1

b = [{Go,Gr,Fo},{As}]
n[str(count)] = b
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1

c = [{Go,Fo},{As,Gr}]
n[str(count)] = c
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1

d = [{Gr,Fo},{As,Go}]
n[str(count)] = d
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1

e = [{As,Gr,Fo},{Go}]
n[str(count)] = e
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1

f = [{Gr},{As,Go,Fo}]
n[str(count)] = f
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1

g = [{Go,Gr,Fo},{As}]
n[str(count)] = g
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1

b = [{Go,Gr,Fo},{As}]
n[str(count)] = b
queue.enqueue(n[str(count)],count)
queue.show()
count = count+1
