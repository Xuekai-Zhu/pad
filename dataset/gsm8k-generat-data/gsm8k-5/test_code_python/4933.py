def solution():
    dimes = 350  # Gloria has 350 dimes
    quarters = dimes/5  # Gloria has 5 times as many dimes as quarters
    quarters_to_put_aside = 2/5 * quarters  # Gloria puts 2/5 of the quarters aside for future use
    remaining_quarters = quarters - quarters_to_put_aside  # Gloria has remaining quarters after putting some aside

    # Calculate the number of dimes and quarters Gloria has after putting aside 2/5 of the quarters
    total_dimes_and_quarters = dimes + remaining_quarters * 25 + quarters_to_put_aside * 25
    result = total_dimes_and_quarters
    return result

print(solution())