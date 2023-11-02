def solution():
    
    crown_cost = 20000
    tip_percent = 10
    tip_amount = crown_cost * (tip_percent / 100)
    total_cost = crown_cost + tip_amount
    result = total_cost
    return result

print(solution())