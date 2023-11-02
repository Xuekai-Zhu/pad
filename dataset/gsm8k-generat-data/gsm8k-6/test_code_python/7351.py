def solution():
    # Calculate the amount left to pay after down payment
    amount_left = 120 / 2

    # Calculate the number of days to pay
    days_to_pay = 10

    # Calculate the daily minimum amount to pay
    daily_amount = amount_left / days_to_pay
    result = daily_amount
    return result

print(solution())