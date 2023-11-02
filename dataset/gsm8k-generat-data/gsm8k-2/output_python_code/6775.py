def solution():
    """Liz sold her car at 80% of what she originally paid. She uses the proceeds of that sale and needs only $4,000 to buy herself a new $30,000 car. How much cheaper is her new car versus what she originally paid for her old one?"""
    original_price = 100
    selling_price = 80
    percent_difference = (original_price - selling_price) / original_price
    old_car_cost = 30000 / (1 - percent_difference)
    savings = old_car_cost - 30000
    result = savings
    return result

print(solution())