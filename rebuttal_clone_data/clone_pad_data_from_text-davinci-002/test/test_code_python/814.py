def solution():
    area = 30 * 40
    cost_per_square_foot = 3
    total_cost = area * cost_per_square_foot
    extra_cost = area * 1
    final_cost = total_cost + extra_cost
    return final_cost

print(solution())