def solution():
    """Dana normally drinks a 500 ml bottle of soda each day. Since the 500 ml bottles are currently out of stock at the store, she buys a 2-liter bottle of soda instead. If Dana continues to drink 500 ml of soda each day, how long will the 2-liter bottle of soda last? There are 1,000 ml in 1 liter."""
    daily_consumption = 0.5  # in liters
    total_volume = 2  # in liters
    remaining_volume = total_volume - daily_consumption
    days = remaining_volume / daily_consumption
    result = days
    return result

print(solution())