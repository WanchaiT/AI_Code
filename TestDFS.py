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
    north_side = [state[0]]   #list[set{}]
    south_side = [state[1]]
    list_state = []

    #set_side is dictionry
    set_side = {"north" : north_side ,"south" : south_side}
    #dict{"n" : list[set{}] ,"s" : list[sets{}]}

    if "AS" in set_side["north"] :  #"AS" on north_side
        list_ch = childs_in_side("north" ,"south" ,set_side)
        set_side["north"] = list_ch[0]
        set_side["south"] = list_ch[1]
        childs_in_north = list_ch[0]
        #check can pass by this state and list["north","south"] not in set
        if check_state(set_side) and not([set_side["north"] ,set_side["south"]] in set) :
            list_state = [set_side["north"] ,set_side["south"]]

        for obj in childs_in_north :
            list_state += add_state(set ,obj ,set_side ,"north" ,"south")
    else :                          #"AS" on south_side
        list_ch = childs_in_side("south" ,"north" ,set_side)
        set_side["south"] = list_ch[0]
        set_side["north"] = list_ch[1]
        childs_in_north = list_ch[0]
        #check can pass by this state and list["north","south"] not in set
        if check_state(set_side) and not([set_side["north"] ,set_side["south"]] in set) :
            list_state = [set_side["north"] ,set_side["south"]]

        for obj in childs_in_south :
            list_state += add_state(set ,obj ,set_side ,"south" ,"north")

    return list_state

def childs_in_side(side_insert ,side_remove ,set_side) :
    print(set_side, set_side[side_insert] , type(set_side[side_insert]))
    insert = set_side[side_insert]
    remove = set_side[side_remove]

    set_side[side_insert][0].add("As")
    print(insert)
    set_side[side_remove][0].remove("As")
    print(remove)
    return [insert ,remove ]    #list[set{}]

def add_state(set ,obj ,set_side ,side_insert ,side_remove) :
    if check_state( [{side_insert : set_side[side_insert] + obj
                    ,side_remove : set_side[side_remove] - obj}]) :
        list_c = [set_side[side_insert] + obj , set_side[side_remove] - obj]
        if not(list_c in set) :
            return [list_c]
        else :
            return []

def check_state(state) :
    go_and_fo = {"Go" ,"Fo"}
    gr_and_go = {"Gr" ,"Go"}
    only_as = {"As"}

    north_side = set(state["north"][0]) #set{}
    south_side = set(state["south"][0])

            #not( (t & t) | () | () | () )
    return not((north_side - go_and_fo == set({})) and not(north_side - go_and_fo == only_as)
            or (north_side - gr_and_go == set({})) and not(north_side - gr_and_go == only_as)
            or (south_side - go_and_fo == set({})) and not(south_side - go_and_fo == only_as)
            or (south_side - gr_and_go == set({})) and not(south_side - gr_and_go == only_as))

def is_goal(state):
    return state[0] == {}

def find_path(queue, set) :
    if queue.isEmpty() :
        return False
    else :
        current_path = queue.dequeue() #current_path  = last queue
        print(current_path)
        #list[list[set{} ,set{}]]

    current_state = current_path[-1]    #current_path[-1] = last_state
    #list[set{} ,set{}]

    if is_goal(current_state) :
        return current_path #return path of goal
    else :
        list_next_state = find_next_state(set ,current_state)
        #list[list[set{} ,set{}]]

        #ex list_next_state = [[{"a"},{"b"}] , [{"c"},{"d"}]]
        #ex state = next_state[0] = [{"a"},{"b"}]  --> state = [next_state[0]]
        #set = [[{"a"},{"b"}] , [{"c"},{"d"}]]

        for state in list_next_state :
            set += [state]  #list[list[set{} ,set{}]]
            next_path = current_path + [state]
            queue.add(next_path)

        return find_path(queue, set)

queue = Queue()
first_state = [set(["As","Fo","Go","Gr"]) ,set({})]   #list[set{} ,set{}]
print(type(first_state[0]))
#implement a set of type list, and inside list have states
#and inside states have sets
set = [first_state] #list[list[set{} ,set{}]]
queue.add(set)

#path = [[{"a","b"},{"b"}{"c"}] , [{"a"},{"b","c","d"}] , ...]
#--> list[list[set{},set{}] , list[set{},set{}] , ... ]
path = find_path(queue ,set)
