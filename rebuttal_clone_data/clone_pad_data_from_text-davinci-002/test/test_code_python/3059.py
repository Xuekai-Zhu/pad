def solution():
    initial_cost = 160
    down_payment = 40
    remaining_amount = initial_cost - down_payment
    weeks_to_save = 8
    weekly_savings = remaining_amount / weeks_to_save
    result = weekly_savings
    return result

print(solution())