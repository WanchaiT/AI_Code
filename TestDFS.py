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


def findPath(queue ):
    '''count = 1
    dict = {}
    strCount = str(count)
    dict[strCount] = queue.dequeue()

    if dict[strCount][0] == {"Gr","Go","As","Fo"}:
        a = [set({Go,Gr}), set({As,Fo})]
        b = [set({Go,Gr,Fo}), set({As})]
        print(s)'''

    count = 1
    while True:
        dict = {}
        dict[numToChar[str(count)]] = queue.dequeue()
        print(graph)
        if dict[numToChar[str(count)]][1] == {"Go","Gr","As","Fo"} :
            print(dict)
            queue.add(dict)
            break

        #else:




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

Go = "Go"
Gr = 'Gr'
As = "As"
Fo = 'Fo'

# list node
s = [set({Go,Gr,As,Fo}), set({})]

goal = [set({}), set({As,Go,Gr,Fo})]

queue = Queue()

queue.enqueue(s)

findPath(queue)
queue.show()
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
