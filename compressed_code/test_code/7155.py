def solution():
    
    cost_1dozen = 8
    cost_2dozen = 14
    cost_6sets_1dozen = 6 * cost_1dozen
    cost_3sets_2dozen = 3 * cost_2dozen
    savings = cost_6sets_1dozen - cost_3sets_2dozen
    result = savings
    return result

print(solution())