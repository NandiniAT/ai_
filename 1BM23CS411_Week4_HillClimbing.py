import random
def generate_initial_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]
def calculate_heuristic(board):
    heuristic = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                heuristic += 1
    return heuristic
def generate_neighbors(board):
    neighbors = []
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i] != j:
                neighbor = board[:]
                neighbor[i] = j
                neighbors.append(neighbor)
    return neighbors
def hill_climbing_with_random_restart(n, max_restarts=100, initial_state=None):
    for restart in range(max_restarts):
        if initial_state is not None and restart == 0:
            current_state = initial_state
        else:
            current_state = generate_initial_board(n)
        current_heuristic = calculate_heuristic(current_state)
        print(f"Restart {restart + 1}: Initial State {current_state} with cost: {current_heuristic}")
        while True:
            neighbors = generate_neighbors(current_state)
            next_state = None
            next_heuristic = current_heuristic
            neighbor_costs = []
            for neighbor in neighbors:
                neighbor_heuristic = calculate_heuristic(neighbor)
                neighbor_costs.append((neighbor, neighbor_heuristic))
                if neighbor_heuristic < next_heuristic:
                    next_state = neighbor
                    next_heuristic = neighbor_heuristic
            print("\nNeighbor States and Costs:")
            for neighbor, cost in neighbor_costs:
                print(f"State: {neighbor} | Cost: {cost}")
            if next_heuristic >= current_heuristic:
                print(f"\nFinal State: {current_state} with cost: {current_heuristic}")
                if current_heuristic == 0:
                    return current_state
                else:
                    break  
            current_state = next_state
            current_heuristic = next_heuristic
            print(f"\nMove to state: {current_state} with cost: {current_heuristic}")
    print("No solution found after maximum restarts.")
    return None
def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[row] == col:
                line += "Q "
            else:
                line += ". "
        print(line)
    print()
if __name__ == "__main__":
    n = 4  
    max_restarts = 10  
    fixed_initial_state = [3, 2, 1, 0]  
    solution = hill_climbing_with_random_restart(n, max_restarts, initial_state=fixed_initial_state)
    if solution:
        print("\nSolution found:")
        print_board(solution)
    else:
        print("\nNo solution found.")