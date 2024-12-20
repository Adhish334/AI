import math
def alpha_beta_search(state):
    best_value = max_value(state, -math.inf, math.inf)
    return best_value
def max_value(state, alpha, beta):
    if terminal_test(state):
        return utility(state)
    
    value = -math.inf
    for action in actions(state):
        value = max(value, min_value(result(state, action), alpha, beta))
        if value >= beta:  
            return value
        alpha = max(alpha, value)
    return value
def min_value(state, alpha, beta):
    if terminal_test(state):
        return utility(state)
    
    value = math.inf
    for action in actions(state):
        value = min(value, max_value(result(state, action), alpha, beta))
        if value <= alpha:  
            return value
        beta = min(beta, value)
    return value
def terminal_test(state):
    return state.get("terminal", False)

def utility(state):
    return state.get("value", 0)

def actions(state):
    return state.get("actions", [])

def result(state, action):
    return action
def input_game_tree():
    print("Define your game tree for Alpha-Beta Pruning.")
    print("Each state can either be a 'terminal node' with a utility value or have 'actions' leading to child states.\n")
    
    game_tree = {}
    game_tree["actions"] = []

    num_actions = int(input("Enter the number of actions from the root node: "))
    for i in range(num_actions):
        print(f"\nAction {i+1}:")
        node_type = input("Is this a terminal node? (yes/no): ").lower()
        
        if node_type == "yes":
            value = int(input("Enter the utility value for this terminal node: "))
            game_tree["actions"].append({"value": value, "terminal": True})
        else:
            print("For non-terminal nodes, we will recursively define its children.")
            game_tree["actions"].append(input_subtree())
    return game_tree

def input_subtree():
    subtree = {}
    subtree["actions"] = []
    
    while True:
        try:
            num_actions = int(input("Enter the number of actions from this node: "))
            if num_actions < 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    for i in range(num_actions):
        print(f"  Sub-action {i+1}:")
        node_type = input("  Is this a terminal node? (yes/no): ").lower()
        
        if node_type == "yes":
            while True:
                try:
                    value = int(input("  Enter the utility value for this terminal node: "))
                    break
                except ValueError:
                    print("Invalid input! Please enter a valid integer for utility value.")
            subtree["actions"].append({"value": value, "terminal": True})
        elif node_type == "no":
            print("  For non-terminal nodes, define its children.")
            subtree["actions"].append(input_subtree())
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")
            i -= 1  
    return subtree
if __name__ == "__main__":
    print("Welcome to Alpha-Beta Pruning Algorithm")
    game_tree = input_game_tree()
    print("\nRunning Alpha-Beta Pruning on the provided game tree...")
    final_value = alpha_beta_search(game_tree)
    print(f"\nThe Final Value at the Root Node is: {final_value}")
