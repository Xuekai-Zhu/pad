def solution():
    """Kelly has 5 quarters and 2 dimes. If she buys a can of pop for 55 cents, how many cents will she have left?"""
    quarters = 5
    dimes = 2
    total_change = (quarters * 25) + (dimes * 10)
    price_of_pop = 55
    cents_left = total_change - price_of_pop
    result = cents_left
    return result

print(solution())