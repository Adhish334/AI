import numpy as np
from collections import deque

class Node:
    def __init__(self, state, parent, action):
        self.state = state  
        self.parent = parent  
        self.action = action  

class Puzzle:
    def __init__(self, start, goal):
        self.start = start 
        self.goal = goal  

    def neighbors(self, state):
        """Generate all possible neighbor states from the current state by sliding tiles."""
        mat, (row, col) = state
        results = []

        # Move the blank tile up
        if row > 0:
            mat1 = np.copy(mat)
            mat1[row][col], mat1[row - 1][col] = mat1[row - 1][col], mat1[row][col]
            results.append(('up', [mat1, (row - 1, col)]))

        # Move the blank tile left
        if col > 0:
            mat1 = np.copy(mat)
            mat1[row][col], mat1[row][col - 1] = mat1[row][col - 1], mat1[row][col]
            results.append(('left', [mat1, (row, col - 1)]))

        # Move the blank tile down
        if row < 2:
            mat1 = np.copy(mat)
            mat1[row][col], mat1[row + 1][col] = mat1[row + 1][col], mat1[row][col]
            results.append(('down', [mat1, (row + 1, col)]))

        # Move the blank tile right
        if col < 2:
            mat1 = np.copy(mat)
            mat1[row][col], mat1[row][col + 1] = mat1[row][col + 1], mat1[row][col]
            results.append(('right', [mat1, (row, col + 1)]))

        return results

    def bfs(self):
        """Breadth-First Search algorithm to find the solution to the 8-puzzle problem."""
        start_node = Node(state=self.start, parent=None, action=None)  # Create the root node
        frontier = deque([start_node])  # Frontier queue for BFS
        visited = set()  # Set to store visited states

        while frontier:
            node = frontier.popleft()  # Get the node from the front of the queue

            # Check if the current state is the goal state
            if (node.state[0] == self.goal[0]).all():
                return self.get_solution(node)  # Return the solution path if goal is reached

            visited.add(tuple(map(tuple, node.state[0])))  # Mark the current state as visited

            # Explore the neighbors (possible moves)
            for action, state in self.neighbors(node.state):
                if tuple(map(tuple, state[0])) not in visited:
                    child_node = Node(state=state, parent=node, action=action)  # Create child node
                    frontier.append(child_node)  # Add the child to the frontier queue
        return None  # Return None if no solution is found

    def get_solution(self, node):
        """Backtrack from the goal node to the start node to find the solution path."""
        actions = []  # List to store the actions (up, down, left, right)
        cells = []  # List to store the states of the puzzle
        while node.parent is not None:
            actions.append(node.action)  # Record the action that led to this state
            cells.append(node.state)  # Record the current state
            node = node.parent  # Move to the parent node
        actions.reverse()  # Reverse the actions list (from start to goal)
        cells.reverse()  # Reverse the cells list (from start to goal)
        return actions, cells

    def print_solution(self, solution):
        """Print the actions and states taken to reach the goal."""
        if solution:
            actions, states = solution
            print("Solution found in", len(actions), "moves:")
            for i, (action, state) in enumerate(zip(actions, states)):
                print(f"Step {i + 1}: Move {action}")
                print(state[0])
        else:
            print("No solution found.")

# Example usage
if __name__ == "__main__":
    # Initial state of the puzzle (2D numpy array and the position of the blank tile)
    start = [np.array([[1, 3, 2], [4, 0, 6], [5, 7, 8]]), (1, 1)]  # Blank tile (0) is at position (1, 1)

    # Goal state of the puzzle
    goal = [np.array([[1, 2, 3], [4, 5, 6], [7, 8, 0]]), (2, 2)]  # Blank tile (0) should be at position (2, 2)

    puzzle = Puzzle(start, goal)
    solution = puzzle.bfs()  # Solve the puzzle using BFS
    puzzle.print_solution(solution)  # Print the solution