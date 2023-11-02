def solution():
    # Number of nickels Val has before finding new ones
    num_nickels = 20

    # Number of dimes Val has
    num_dimes = 3 * num_nickels

    # New number of nickels after finding more in brother's treasure box
    num_new_nickels = 2 * num_nickels

    # Total number of coins Val has
    total_coins = num_nickels + num_dimes + num_new_nickels

    # Total value of coins in dollars
    total_value = (num_nickels * 0.05) + (num_dimes * 0.10) + (num_new_nickels * 0.05)

    result = total_value
    return result

print(solution())