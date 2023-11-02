def solution():
    # Set up the ratio between dimes and quarters
    dimes_to_quarters = 5

    # Calculate the number of quarters
    quarters = 350 / (dimes_to_quarters + 1)

    # Calculate the number of dimes
    dimes = 5 * quarters

    # Calculate the number of quarters put aside
    quarters_aside = 2/5 * quarters

    # Calculate the total number of coins after putting aside some quarters
    total_coins = quarters + dimes - quarters_aside

    result = total_coins
    return result

print(solution())