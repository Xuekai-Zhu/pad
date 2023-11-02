def solution():
    num_records = 200
    half_records = num_records / 2

    # Calculate the profit from Sammy's deal
    profit_Sammy = 4 * num_records

    # Calculate the profit from Bryan's deal
    profit_Bryan = (6 * half_records) + (1 * half_records)

    # Calculate the difference in profit between the two deals
    difference = profit_Sammy - profit_Bryan
    result = difference
    return result

print(solution())