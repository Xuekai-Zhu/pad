def solution():
    cost = 150
    cashback_percent = 10
    rebate = 25
    total_cashback = cost * (cashback_percent / 100)
    total_cost = cost - total_cashback - rebate
    result = total_cost
    return result

print(solution())