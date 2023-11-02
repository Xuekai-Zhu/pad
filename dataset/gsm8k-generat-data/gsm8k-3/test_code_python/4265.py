def solution():
    """Zain has 10 more of each coin than Emerie. If Emerie has six quarters, seven dimes, and five nickels, how many coins does Zain have?"""
    # Define the number of coins Emerie has
    emerie_quarters = 6
    emerie_dimes = 7
    emerie_nickels = 5

    # Calculate the total number of coins Emerie has
    emerie_total_coins = emerie_quarters + emerie_dimes + emerie_nickels

    # Calculate the number of coins Zain has
    zain_quarters = emerie_quarters + 10
    zain_dimes = emerie_dimes + 10
    zain_nickels = emerie_nickels + 10

    # Calculate the total number of coins Zain has
    zain_total_coins = zain_quarters + zain_dimes + zain_nickels

    # Display the total number of coins Zain has
    result = zain_total_coins
    return result

print(solution())