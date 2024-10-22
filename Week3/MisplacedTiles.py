import heapq

class Node:
    def __init__(self, state, parent=None, g=0, h=0, move=None):
        self.state = state  
        self.parent = parent  
        self.g = g  
        self.h = h  
        self.f = g + h  
        self.move = move  

    def __lt__(self, other):
        return self.f < other.f

def misplaced_tiles(state, goal_state):
    """Calculate the number of misplaced tiles between the current state and goal state."""
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal_state[i][j]:
                count += 1
    return count

def find_blank(state):
    """Find the position of the blank tile (0) in the current state."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def swap_tiles(state, x1, y1, x2, y2):
    """Swap the blank tile with the tile in the specified direction."""
    new_state = [row[:] for row in state]  
    new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
    return new_state

def get_neighbors(node, goal_state):
    """Generate neighboring states by sliding the blank tile in all possible directions."""
    neighbors = []
    x, y = find_blank(node.state)  
    directions = {
        "up": (x - 1, y),
        "down": (x + 1, y),
        "left": (x, y - 1),
        "right": (x, y + 1)
    }
   
    for move, (new_x, new_y) in directions.items():
        if 0 <= new_x < 3 and 0 <= new_y < 3:  
            new_state = swap_tiles(node.state, x, y, new_x, new_y)
            g = node.g + 1  
            h = misplaced_tiles(new_state, goal_state)  
            neighbors.append(Node(new_state, parent=node, g=g, h=h, move=move))
   
    return neighbors

def reconstruct_path(node):
    """Reconstruct the path from start to goal by following parent nodes."""
    path = []
    while node.parent is not None:
        path.append(node.move)
        node = node.parent
    return path[::-1]  
def print_state(state):
    """Print the state of the puzzle."""
    for row in state:
        print(row)
    print()

def a_star_8_puzzle_misplaced(start_state, goal_state):
    open_list = [] 
    closed_list = set()  
   
    start_node = Node(start_state, g=0, h=misplaced_tiles(start_state, goal_state))
    heapq.heappush(open_list, start_node)
   
    while open_list:
        current_node = heapq.heappop(open_list)
       
        if current_node.state == goal_state:
            print("Reached goal state:")
            print_state(current_node.state)
            return reconstruct_path(current_node)
       
        closed_list.add(tuple(tuple(row) for row in current_node.state))  
       
        print("Current state (g={}, h={}, f={}):".format(current_node.g, current_node.h, current_node.f))
        print_state(current_node.state)
       
        for neighbor in get_neighbors(current_node, goal_state):
            if tuple(tuple(row) for row in neighbor.state) in closed_list:
                continue
            heapq.heappush(open_list, neighbor)
   
    return "No solution found"

start_state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

goal_state = [
    [1, 2, 3],
    [8, 0, 4],
    [7, 6, 5]
]

path = a_star_8_puzzle_misplaced(start_state, goal_state)

if path != "No solution found":
    print("Path to solution:", path)
else:
    print(path)