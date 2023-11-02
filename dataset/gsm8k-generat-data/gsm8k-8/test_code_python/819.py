def solution():
    # Define the tins collected on the first three days
    tins_day1 = 50
    tins_day2 = 3 * tins_day1
    tins_day3 = tins_day2 - 50

    # Calculate the total tins collected on the first three days
    total_tins_first3days = tins_day1 + tins_day2 + tins_day3

    # Calculate the remaining tins needed to reach 500 tins
    remaining_tins = 500 - total_tins_first3days

    # Calculate the number of days left in the week
    days_left = 4

    # Calculate the number of tins needed to be collected each remaining day
    tins_per_day = remaining_tins / days_left
    result = tins_per_day
    return result

print(solution())