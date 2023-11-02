def solution():
    total_cost = 120
    down_payment = total_cost / 2
    balance = total_cost - down_payment
    num_days = 10

    # Calculate the daily minimum amount that Rita must pay
    daily_minimum = balance / num_days
    result = daily_minimum
    return result

print(solution())