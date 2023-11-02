def solution():
    fabric_cost_per_yard = 24
    pattern_cost = 15
    thread_cost = 2 * 3

    total_cost = 141
    fabric_cost = total_cost - pattern_cost - thread_cost

    fabric_yards = fabric_cost / fabric_cost_per_yard
    result = fabric_yards
    return result

print(solution())