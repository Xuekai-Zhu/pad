def solution():
    
    total_cost = 5*5 + 10*5 + 3*5
    change = 200 - total_cost
    bags = change // 10
    result = bags
    return result

print(solution())