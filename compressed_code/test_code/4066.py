def solution():
    
    total_cost = 2100
    sister_days = 4
    sue_days = 7 - sister_days
    sister_percentage = sister_days / 7
    sue_percentage = sue_days / 7
    sue_payment = sue_percentage * total_cost
    result = sue_payment
    return result

print(solution())