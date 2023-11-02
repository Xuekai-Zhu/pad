def solution():
    """The price of electricity went up by 25%. John's old computer used 800 watts and his new computer uses 50% more. If the old price of electricity was 12 cents per kilowatt-hour, how much does his computer cost, in dollars, to run for 50 hours?"""
    old_price_per_kwh = 0.12
    new_price_per_kwh = old_price_per_kwh * 1.25
    old_power_usage = 800 / 1000 # convert watts to kilowatts
    new_power_usage = old_power_usage * 1.5
    total_power_usage = new_power_usage * 50 # in kilowatt-hours
    cost = total_power_usage * new_price_per_kwh
    result = cost
    return result

print(solution())