def solution():
    cost_of_food = 3.65 + 2 + 1 + 4 + (3 * 0.5) + 0.2
    cost_per_person = cost_of_food / 2
    toby_initial_cost = 15
    toby_cost = toby_initial_cost / 2
    toby_change = toby_initial_cost - toby_cost
    result = toby_change
    
    return result

print(solution())