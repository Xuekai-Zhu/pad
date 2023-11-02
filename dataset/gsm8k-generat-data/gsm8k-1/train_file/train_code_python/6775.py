def solution():
    """Liz sold her car at 80% of what she originally paid. She uses the proceeds of that sale and needs only $4,000 to buy herself a new $30,000 car. How much cheaper is her new car versus what she originally paid for her old one?"""
    original_price = x    #variable to be asked by the person who uses this code
    sold_price = original_price * 0.8
    difference = original_price - sold_price - 30000 + 4000
    result = difference
    return result

print(solution())