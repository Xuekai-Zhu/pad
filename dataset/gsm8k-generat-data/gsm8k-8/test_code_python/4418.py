def solution():
    total_cost = 50
    entree_cost = 0.8 * total_cost / 4
    appetizer_cost = (total_cost - (4 * entree_cost)) / 2
    result = appetizer_cost
    return result

print(solution())