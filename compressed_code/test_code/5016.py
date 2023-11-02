def solution():
    
    bridge_limit = 20000
    empty_weight = 12000
    soda_weight = 20 * 50
    dryer_weight = 3 * 3000
    produce_weight = 2 * soda_weight
    full_weight = empty_weight + soda_weight + dryer_weight + produce_weight
    result = full_weight
    return result

print(solution())