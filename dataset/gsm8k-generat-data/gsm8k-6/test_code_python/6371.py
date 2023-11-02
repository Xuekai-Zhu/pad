def solution():
    # Calculate the daily profit
    daily_profit = (40 * 2) + (6 * 12) - 20 - 2  # Marie sells 40 loaves of bread for $2 each and 6 cakes for $12 each, and has to pay $20 for rent and $2 for electricity

    # Calculate the number of days needed to pay for the cash register
    days_to_pay = 1040 / daily_profit
    result = days_to_pay
    return result

print(solution())