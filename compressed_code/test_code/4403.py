def solution():
    
    total_cost = 42
    bananas_cost = 12
    bread_cost = 9
    milk_cost = 7
    apples_cost = total_cost - bananas_cost - bread_cost - milk_cost
    result = apples_cost
    return result

print(solution())