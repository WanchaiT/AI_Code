class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item ):
        self.items.insert(0,item)

    def add(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)

def find_next_state(set ,state) :
    #code

def is_goal(state):
    return state[0] = {}

def find_path(queue, set) :
    if queue.isEmpty() :
        return False
    else :
        current_path = queue.dequeue() #current_path  = last queue

    if is_goal(current_path) :
        return current_path #return path of goal
    else :
        current_state = current_path[-1]
        list_next_state = find_next_state(set ,current_state)

        #ex list_next_state = [[{"a"},{"b"}] , [{"c"},{"d"}]]
        #ex state = next_state[0] = [{"a"},{"b"}]  --> state = [next_state[0]]
        #set = [[{"a"},{"b"}] , [{"c"},{"d"}]]

        for state in list_next_state :
            set += [state]
            current_path += [state]
            queue.add(current_path)

        return find_path(queue, set)

queue = Queue
first_state = [set({"As","Fo","Go","Gr"}) ,set()]

#implement a set of type list, and inside list have states
#and inside states have sets
set = [first_state]
queue.add(set)
path = find_path(queue, set)
