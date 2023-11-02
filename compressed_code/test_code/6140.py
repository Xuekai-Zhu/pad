def solution():
    
    hot_tub_capacity = 40 * 4 
    bottles_needed = hot_tub_capacity / 1 
    bottle_cost = 50
    discount = 0.2
    total_cost = bottles_needed * bottle_cost * (1 - discount)
    result = total_cost
    return result

print(solution())