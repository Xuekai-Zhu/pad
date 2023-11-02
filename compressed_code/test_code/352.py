def solution():
    
    initial_cost = 500
    additional_cost = initial_cost * (2/5)
    total_cost = initial_cost + additional_cost
    discounted_cost = total_cost * 0.85
    money_needed = discounted_cost - initial_cost
    result = money_needed
    return result

print(solution())