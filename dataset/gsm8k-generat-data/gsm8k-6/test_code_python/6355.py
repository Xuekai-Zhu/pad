def solution():
    # Calculate the total cost of pattern and threads
    pattern_thread_cost = 15 + 2*3  # pattern costs $15, two spools of thread cost $3 each
    fabric_cost = 141 - pattern_thread_cost  # remaining cost is for fabric
    fabric_yards = fabric_cost / 24  # 1 yard of fabric costs $24

    result = fabric_yards
    return result

print(solution())