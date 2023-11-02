def solution():
    # Calculate the total power used by all bulbs in a day
    total_power_per_day = 60 * 40  # 60 watts per bulb, 40 bulbs

    # Calculate the total power used in June (30 days)
    total_power_in_june = total_power_per_day * 30

    # Calculate the total cost for the power used in June
    cost_in_cents = total_power_in_june * 20  # 20 cents per watt
    cost_in_dollars = cost_in_cents / 100

    result = cost_in_dollars
    return result

print(solution())