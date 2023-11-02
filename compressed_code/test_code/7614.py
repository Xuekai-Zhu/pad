def solution():
    
    length = 3
    width = 3
    area = length * width
    bags_needed = area / 3
    cost_per_bag = 4
    total_cost = bags_needed * cost_per_bag
    result = total_cost
    return result

print(solution())