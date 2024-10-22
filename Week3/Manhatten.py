import heapq

class Node:
    def __init__(self, state, parent=None, move=None, g=0, h=0):
        self.state = state      
        self.parent = parent    
        self.move = move       
        self.g = g              
        self.h = h              
        self.f = g + h         

    def __lt__(self, other):
        return self.f < other.f

def manhattan_distance(state, goal):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                x, y = divmod(goal.index(state[i][j]), 3)
                distance += abs(x - i) + abs(y - j)
    return distance

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def get_neighbors(node):
    neighbors = []
    x, y = find_blank(node.state)
    directions = [
        ("up", (x - 1, y)),
        ("down", (x + 1, y)),
        ("left", (x, y - 1)),
        ("right", (x, y + 1))
    ]
    for move, (new_x, new_y) in directions:
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in node.state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(Node(new_state, node, move))
    return neighbors

def is_goal(state, goal):
    return state == goal


def reconstruct_path(node):
    path = []
    states = []
    while node.parent:
        path.append(node.move)
        states.append(node.state)
        node = node.parent
    states.append(node.state)  
    return path[::-1], states[::-1]  


def astar_8_puzzle(start, goal):
    goal_flat = sum(goal, [])  
    open_list = []
    heapq.heappush(open_list, Node(start, h=manhattan_distance(start, goal_flat)))
    closed_list = set()

    while open_list:
        current_node = heapq.heappop(open_list)


        if is_goal(current_node.state, goal):
            return reconstruct_path(current_node)

        closed_list.add(tuple(map(tuple, current_node.state))) 


        for neighbor in get_neighbors(current_node):
            neighbor.g = current_node.g + 1
            neighbor.h = manhattan_distance(neighbor.state, goal_flat)
            neighbor.f = neighbor.g + neighbor.h

            if tuple(map(tuple, neighbor.state)) in closed_list:
                continue

            heapq.heappush(open_list, neighbor)

    return None 


def print_state(state):
    for row in state:
        print(row)
    print()


if __name__ == "__main__":
   
    start_state = [
        [2, 8, 3],
        [1, 6, 4],
        [7, 0, 5]
    ]
   
    # Goal state
    goal_state = [
        [1, 2, 3],
        [8, 0, 4],
        [7, 6, 5]
    ]

    result = astar_8_puzzle(start_state, goal_state)

    if result:
        moves, states = result
        print("Solution found in {} moves:".format(len(moves)))
        for i, state in enumerate(states):
            print("Move {}:".format(i))

            print_state(state)
    else:
        print("No solution found.")