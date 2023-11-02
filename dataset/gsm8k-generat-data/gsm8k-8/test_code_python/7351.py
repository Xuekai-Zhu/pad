def solution():
    # Calculate the amount of the down payment
    down_payment = 120 / 2

    # Calculate the remaining balance
    remaining_balance = 120 - down_payment

    # Calculate the number of days until the pick-up date
    days_until_pickup = 10

    # Calculate the daily minimum amount that Rita must pay
    daily_minimum = remaining_balance / days_until_pickup

    result = daily_minimum
    return result

print(solution())