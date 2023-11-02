def solution():
    """John's piggy bank contains quarters, dimes, and nickels. He has three more dimes than quarters and 6 fewer nickels than quarters.
    If he has 63 coins, how many quarters does John have?"""
    total_coins = 63
    quarters = x
    dimes = x + 3
    nickels = x - 6
    # using the equation total_coins = quarters + dimes + nickels
    x = (total_coins + 3) / 3
    result = x
    return result

print(solution())