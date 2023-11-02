def solution():
    num_dimes = 350
    dimes_per_quarter = 5
    quarters_total = (num_dimes / dimes_per_quarter)

    # Calculate the number of quarters that she puts aside
    quarters_aside = 2/5 * quarters_total

    # Calculate the number of quarters that she keeps
    quarters_remaining = quarters_total - quarters_aside

    # Calculate the total number of dimes and quarters that she has remaining
    total_coins = (num_dimes + quarters_remaining * dimes_per_quarter) + quarters_aside * dimes_per_quarter + quarters_aside * 25

    result = total_coins
    return result

print(solution())