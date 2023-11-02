def solution():
    old_cost = 200
    new_capacity = 2
    cost_increase = 20
    new_cost = old_cost * new_capacity * (1 + (cost_increase / 100))
    result = new_cost
    return result

print(solution())