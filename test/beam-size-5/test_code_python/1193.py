def solution():
    
    scotch_cost = 600
    cognac_cost = scotch_cost * 1.5
    total_bottles = 10
    total_cost = (scotch_cost * total_bottles) + (cognac_cost * total_bottles)
    result = total_cost
    return result

print(solution())