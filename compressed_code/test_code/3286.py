def solution():
    
    total_cost = 45
    black_cost = 15
    pink_cost = 10
    green_cost = (total_cost - black_cost - pink_cost) / 2
    result = green_cost
    return result

print(solution())