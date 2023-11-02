def solution():
    
    peanut_butter_cost = 3
    almond_butter_cost = peanut_butter_cost * 3
    jars_per_batch = 0.5
    cost_per_batch_p = peanut_butter_cost * jars_per_batch
    cost_per_batch_a = almond_butter_cost * jars_per_batch
    cost_difference = cost_per_batch_a - cost_per_batch_p
    result = cost_difference
    return result

print(solution())