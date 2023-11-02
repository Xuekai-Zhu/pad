def solution():
    power_per_day = 60 * 60  # 60 bulbs, each using 60 watts per day
    monthly_power_usage = power_per_day * 30  # assuming 30 days in June
    total_cost = monthly_power_usage * 0.20  # 20 cents per power watt used
    result = total_cost
    return result

print(solution())