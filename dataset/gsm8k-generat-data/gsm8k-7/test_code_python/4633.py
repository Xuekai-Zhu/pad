def solution():
    cost_per_person = (2 * 3.65 + 2 + 1 + 4 + 3 * 0.5 + 0.2) / 2
    total_cost = cost_per_person * 2
    change = 15 - total_cost
    result = change
    return result

print(solution())