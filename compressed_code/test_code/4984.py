def solution():
    
    apple_price = 2
    emmy_budget = 200
    gerry_budget = 100
    total_budget = emmy_budget + gerry_budget
    total_apples = total_budget // apple_price
    result = total_apples
    return result

print(solution())