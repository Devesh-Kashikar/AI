from queue import PriorityQueue

goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Manhattan Distance
def heuristic(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                x, y = divmod(val - 1, 3)
                dist += abs(x - i) + abs(y - j)
    return dist

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# A* Algorithm
def astar(start):
    q = PriorityQueue()
    q.put((heuristic(start), 0, start, []))
    visited = set()

    while not q.empty():
        est_cost, cost_so_far, state, path = q.get()
        t_state = tuple(map(tuple, state))
        if t_state in visited:
            continue
        visited.add(t_state)

        if state == goal:
            return path + [(state, cost_so_far)]

        x, y = find_zero(state)
        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_state = [row[:] for row in state]
                new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
                q.put((
                    cost_so_far + 1 + heuristic(new_state),
                    cost_so_far + 1,
                    new_state,
                    path + [(state, cost_so_far)]
                ))
    return None

# User Input
print("Enter puzzle (use 0 for blank):")
start = [list(map(int, input().split())) for _ in range(3)]

# Solve
solution = astar(start)

# Output
if solution:
    print("\n✅ Solved in", len(solution) - 1, "steps:\n")
    for i, (step, cost_so_far) in enumerate(solution):
        print(f"Step {i}:")
        for row in step:
            print(row)
        h = heuristic(step)
        total_cost = cost_so_far + h
        print(f"Manhattan Distance (h): {h}")
        print(f"Total Cost (g + h): {cost_so_far} + {h} = {total_cost}")
        print("-----------")
else:
    print("❌ No solution found.")


