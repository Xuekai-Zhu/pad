def solution():
    
    sandbox_area = 3 * 3
    sandbag_area = 3
    sandbag_cost = 4
    bags_needed = sandbox_area / sandbag_area
    cost = bags_needed * sandbag_cost
    result = cost
    return result

print(solution())