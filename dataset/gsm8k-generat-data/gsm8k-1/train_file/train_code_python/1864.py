def solution():
    """Linda's bag has 2 dimes, 6 quarters, and 5 nickels. Her mother gives her 2 more dimes, 10 quarters, and twice as many nickels as she has. How many coins does she have altogether?"""
    dimes = 2 + 2
    quarters = 6 + 10
    nickels = 5 + (5 * 2)
    total_coins = dimes + quarters + nickels
    result = total_coins
    return result

print(solution())