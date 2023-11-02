def solution():
    
    shoes_per_child = 2
    children = 3
    cost_per_shoe = 60
    total_shoes = shoes_per_child * children * children
    total_cost = total_shoes * cost_per_shoe
    result = total_cost
    return result

print(solution())