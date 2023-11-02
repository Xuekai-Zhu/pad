def solution():
    """Zain has 10 more of each coin than Emerie. If Emerie has six quarters, seven dimes, and five nickels, how many coins does Zain have?"""
    emerie_quarters = 6
    emerie_dimes = 7
    emerie_nickels = 5
    zain_quarters = emerie_quarters + 10
    zain_dimes = emerie_dimes + 10
    zain_nickels = emerie_nickels + 10
    total_coins = zain_quarters + zain_dimes + zain_nickels
    result = total_coins
    return result

print(solution())