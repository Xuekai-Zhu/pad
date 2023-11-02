def solution():
    total_coins = 63  # John's piggy bank has a total of 63 coins

    # Let q be the number of quarters John has
    # Then, he has q + 3 dimes and q - 6 nickels
    # The total value of these coins is given by:
    # 0.25q + 0.10(q + 3) + 0.05(q - 6) = total_value
    # Simplifying the equation, we get:
    # 0.40q - 0.15 = total_value
    # Solving for q, we get:
    # q = (total_value + 0.15) / 0.40

    total_value = 0  # Initialize the total value of coins

    # Iterate through possible values of q and find the value that satisfies the equation
    for q in range(1, total_coins):
        total_value = 0.25 * q + 0.10 * (q + 3) + 0.05 * (q - 6)
        if total_value == total_coins:
            result = q
            break

    return result

print(solution())