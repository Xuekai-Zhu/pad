def solution():
    
    hamburgers = 5
    hamburger_cost = 3
    fries_sets = 4
    fries_cost = 1.2
    sodas = 5
    soda_cost = 0.5
    spaghetti_cost = 2.7
    total_cost = (hamburgers * hamburger_cost) + (fries_sets * fries_cost) + (sodas * soda_cost) + spaghetti_cost
    total_friends = 5
    cost_per_friend = total_cost / total_friends
    result = cost_per_friend
    return result

print(solution())