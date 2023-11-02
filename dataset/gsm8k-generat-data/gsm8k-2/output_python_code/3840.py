def solution():
    """Laura bought 2 pairs of pants for $54 each and 4 shirts for $33 each. She gave $250 to the cashier. So how much change did she take?"""
    pants_price = 54
    shirt_price = 33
    total_pants_price = 2 * pants_price
    total_shirt_price = 4 * shirt_price
    total_price = total_pants_price + total_shirt_price
    change = 250 - total_price
    result = change
    return result

print(solution())