def solution():
    """The price of electricity went up by 25%. John's old computer used 800 watts and his new computer uses 50% more. If the old price of electricity was 12 cents per kilowatt-hour, how much does his computer cost, in dollars, to run for 50 hours?"""
    old_wattage = 800
    new_wattage = old_wattage * 1.5
    old_price_per_kwh = 0.12
    new_price_per_kwh = old_price_per_kwh * 1.25
    hours = 50
    old_kwh_per_hour = old_wattage / 1000
    new_kwh_per_hour = new_wattage / 1000
    old_cost = old_price_per_kwh * old_kwh_per_hour * hours
    new_cost = new_price_per_kwh * new_kwh_per_hour * hours
    result = new_cost - old_cost
    return result

print(solution())