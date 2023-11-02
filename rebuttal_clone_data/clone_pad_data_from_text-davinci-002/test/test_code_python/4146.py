def solution():
    total_cost = 120
    down_payment = total_cost / 2
    balance = total_cost - down_payment
    daily_minimum = balance / 10
    result = daily_minimum
    return result

print(solution())