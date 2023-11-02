def solution():
    # Calculate the total number of coins in Linda's bag before her mother gave her more coins
    initial_coins = 2 + 6 + 5

    # Calculate the total number of coins after her mother gave her more coins
    additional_dimes = 2
    additional_quarters = 10
    additional_nickels = 2 * 5  # twice as many nickels as she originally had
    total_coins = initial_coins + additional_dimes + additional_quarters + additional_nickels

    result = total_coins
    return result

print(solution())