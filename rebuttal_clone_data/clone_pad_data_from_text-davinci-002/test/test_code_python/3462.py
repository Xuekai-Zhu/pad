def solution():
    cost = 30
    tip_percent = 30
    tip_amount = cost * (tip_percent / 100)
    total_cost = cost + tip_amount
    result = total_cost
    return result

print(solution())