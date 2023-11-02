def solution():
    today_liters = 10
    friday_liters = 25
    price_per_liter_today = 1.4
    price_per_liter_friday = price_per_liter_today - 0.4

    # Calculate the cost for the 10 liters of gas today
    today_cost = today_liters * price_per_liter_today

    # Calculate the cost for the 25 liters of gas on Friday after the price rollback
    friday_cost = friday_liters * price_per_liter_friday

    # Calculate the total cost for the 35 liters of gas
    total_cost = today_cost + friday_cost
    result = total_cost
    return result

print(solution())