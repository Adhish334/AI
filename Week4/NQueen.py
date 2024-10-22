import random
def calculate_attacks(board):
    attacks = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_neighbors(board):
    neighbors = []
    n = len(board)
    
    for row in range(n):
        for col in range(n):
            if col != board[row]:  
                new_board = board[:]
                new_board[row] = col
                neighbors.append(new_board)
    
    return neighbors


def hill_climbing(n):

    current_board = [random.randint(0, n-1) for _ in range(n)]
    
    
    step = 0  
    while True:
     
        current_attacks = calculate_attacks(current_board)
        
 
        print(f"Step {step}:")
        print_board(current_board)
        print(f"Heuristic (attacks): {current_attacks}\n")
        
      
        neighbors = get_neighbors(current_board)
        

        best_board = current_board
        best_attacks = current_attacks
        
        for neighbor in neighbors:
            attacks = calculate_attacks(neighbor)
            if attacks < best_attacks:
                best_board = neighbor
                best_attacks = attacks
        

        if best_attacks == current_attacks:
            break
        else:
            current_board = best_board
            step += 1
    
    return current_board


def print_board(board):
    n = len(board)
    for i in range(n):
        row = ['Q' if col == board[i] else '.' for col in range(n)]
        print(" ".join(row))


n = 10000000
solution = hill_climbing(n)


print("Final Solution:")
print_board(solution)
print(f"Heuristic (attacks): {calculate_attacks(solution)}")