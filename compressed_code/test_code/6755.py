def solution():
    
    remove_cost = 50
    length = 8
    width = 7
    area = length * width
    cost_per_square_foot = 1.25
    replacement_cost = area * cost_per_square_foot + remove_cost
    result = replacement_cost
    return result

print(solution())