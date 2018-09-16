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
    north_side = state[0]
    south_side = state[1]
    list_state = []

    #set_side is dictionry
    set_side = {"north" : north_side ,"south" : south_side}

    if "AS" in set_side["north"] :  #"AS" in north_side
        set_side["north"].remove("AS") # move "AS" to south_side
        set_side["south"].add("AS")
        childs_of_north = list(set_side["north"])
    else :                          #"AS" in south_side                  
        set_side["south"].remove("AS") # move "AS" to north_side
        set_side["north"].add("AS")
        childs_of_north = list(set_side["south"])

def is_goal(state):
    return state[0] == {}

def find_path(queue, set) :
    if queue.isEmpty() :
        return False
    else :
        current_path = queue.dequeue() #current_path  = last queue

    current_state = current_path[-1]    #current_path[-1] = last_state

    if is_goal(current_state) :
        return current_path #return path of goal
    else :
        list_next_state = findNextState(set ,current_state)

        #ex list_next_state = [[{"a"},{"b"}] , [{"c"},{"d"}]]
        #ex state = next_state[0] = [{"a"},{"b"}]  --> state = [next_state[0]]
        #set = [[{"a"},{"b"}] , [{"c"},{"d"}]]

        for state in list_next_state :
            set += [state]
            next_path = current_path + [state]
            queue.add(next_path)

        return find_path(queue, set)

queue = Queue()
first_state = [set({"As","Fo","Go","Gr"}) ,set()]

#implement a set of type list, and inside list have states
#and inside states have sets
set = [first_state]
queue.add(set)

#path = [[{"a","b"},{"b"}{"c"}] , [{"a"},{"b","c","d"}] , ...]
#--> list[list[set{},set{}] , list[set{},set{}] , ... ]
path = find_path(queue, set)
