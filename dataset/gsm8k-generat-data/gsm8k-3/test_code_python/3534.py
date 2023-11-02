def solution():
    """John's piggy bank contains quarters, dimes, and nickels.  He has three more dimes than quarters and 6 fewer nickels than quarters.  If he has 63 coins, how many quarters does John have?"""
    # Let q be the number of quarters John has
    # Then he has q+3 dimes and q-6 nickels
    # The total number of coins is q + q+3 + q-6 = 3q-3
    total_coins = 63

    # Solve for q
    q = (total_coins + 3) / 3

    # Display the number of quarters John has
    result = int(q)
    return result

print(solution())