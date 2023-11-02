def solution():
    num_records = 200  # Peggy has 200 records

    # Calculate the total profit from selling all records to Sammy
    sammy_profit = 4 * num_records

    # Calculate the profit from selling half of the records to Bryan
    bryan_profit_half = 6 * (num_records / 2)

    # Calculate the profit from selling the other half of the records to Bryan
    bryan_profit_other_half = 1 * (num_records / 2)

    # Calculate the total profit from selling to Bryan
    bryan_profit = bryan_profit_half + bryan_profit_other_half

    # Calculate the difference in profit between Sammy and Bryan's deals
    profit_difference = sammy_profit - bryan_profit
    result = profit_difference
    return result

print(solution())