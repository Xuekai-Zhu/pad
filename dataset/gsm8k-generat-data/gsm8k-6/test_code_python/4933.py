def solution():
    dimes = 350
    # Determine the number of quarters Gloria has by dividing the number of dimes by 5
    quarters = dimes / 5
    # Determine the number of quarters Gloria will put aside for future use
    quarters_aside = 2/5 * quarters
    # Subtract the number of quarters put aside from the total number of quarters to get the remaining quarters
    remaining_quarters = quarters - quarters_aside
    # Calculate the total number of quarters and dimes Gloria has after putting aside 2/5 of the quarters
    total_coins = remaining_quarters + dimes
    result = total_coins
    return result

print(solution())