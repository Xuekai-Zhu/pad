def solution():
    """John's piggy bank contains quarters, dimes, and nickels. He has three more dimes than quarters and 6 fewer nickels than quarters. If he has 63 coins, how many quarters does John have?"""
    # Initialize the number of quarters
    quarters = None
    
    # Define the total number of coins and the difference in the number of dimes and quarters
    total_coins = 63
    dimes_diff = 3
    nickels_diff = -6
    
    # Set up an equation system to solve the problem
    #    q + d + n = total_coins
    #    d = q + dimes_diff
    #    n = q + nickels_diff
    # Substitute the second and third equations into the first equation and simplify
    #    q + q + dimes_diff + q + nickels_diff = total_coins
    #    3q + dimes_diff + nickels_diff = total_coins
    #    3q - 3 = total_coins
    #    q = (total_coins + 3) / 3
    quarters = (total_coins + 3) / 3
    
    result = quarters
    return result

print(solution())