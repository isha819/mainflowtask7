def generate_permutations(arr):
    if len(arr) == 0:
        return [[]]
    perms = []
    for i in range(len(arr)):
        chosen = arr[i]
        rest = arr[:i] + arr[i+1:]
        for p in generate_permutations(rest):
            perms.append([chosen] + p)
    return perms

def solve_tsp():
    n = int(input("Enter number of cities: ").strip())
    if n <= 0:
        print("No cities.")
        return

    print(f"Enter distance matrix ({n} rows, each {n} integers separated by space):")
    dist = []
    for i in range(n):
        row = input().strip().split()

        row_ints = [int(x) for x in row]
        if len(row_ints) != n:
            print("Each row must have", n, "integers. Exiting.")
            return
        dist.append(row_ints)

    start_city = 0
    other_cities = list(range(1, n))
    perms = generate_permutations(other_cities)

    best_path = None
    best_dist = 10**18 

    for perm in perms:
        path = [start_city] + perm + [start_city]
        total = 0
        for i in range(len(path) - 1):
            u = path[i]
            v = path[i + 1]
            total += dist[u][v]
        if total < best_dist:
            best_dist = total
            best_path = path[:]

    if best_path is None:
        print("No route found.")
    else:
        print("Shortest route (visit order):", " -> ".join(str(x) for x in best_path))
        print("Total distance:", best_dist)

if __name__ == "__main__":
    solve_tsp()
