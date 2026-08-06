import sys

N = 4

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

visited = [False] * N
min_cost = sys.maxsize
best_path = []


def tsp(curr_pos, count, cost, path):
    global min_cost, best_path

    if count == N and graph[curr_pos][0]:
        total_cost = cost + graph[curr_pos][0]

        if total_cost < min_cost:
            min_cost = total_cost
            best_path = path[:] + [0]
        return

    for i in range(N):
        if not visited[i] and graph[curr_pos][i]:
            visited[i] = True
            tsp(
                i,
                count + 1,
                cost + graph[curr_pos][i],
                path + [i]
            )
            visited[i] = False


visited[0] = True
tsp(0, 1, 0, [0])

print("Minimum Cost:", min_cost)
print("Optimal Path:", best_path)
