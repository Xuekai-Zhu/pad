def solution():
    """John's piggy bank contains quarters, dimes, and nickels. He has three more dimes than quarters and 6 fewer nickels than quarters. If he has 63 coins,
    how many quarters does John have?"""
    total_coins = 63
    # Let's assume x as the number of quarters
    x = (total_coins + 3 + 6) / 3
    # Now, we know that the total number of coins is equal to the sum of quarters, dimes, and nickels
    # We can set up two equations for this
    # First, the total value of quarters is 25 * x cents
    # Second, we know that the number of nickels is 6 fewer than the number of quarters, so the total value of
    # nickels is 5 * (x - 6) cents
    # Finally, we know that John has three more dimes than quarters, so the total value of dimes is 10 * (x + 3) cents
    total_value = 25 * x + 5 * (x - 6) + 10 * (x + 3)
    # We also know that the total value is equal to the sum of the values of all the coins
    # So we can set up another equation for this
    total_value = 25 * x + 10 * (x + 3) + 5 * (x - 6)
    # We can solve this equation for x
    x = (total_coins + 3 + 6) / 3
    # The solution is the number of quarters
    result = x
    return result

print(solution())