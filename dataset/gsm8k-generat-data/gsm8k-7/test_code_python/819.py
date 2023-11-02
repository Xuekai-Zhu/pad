def solution():
    total_tins = 500
    first_day_tins = 50
    second_day_tins = 3 * first_day_tins
    third_day_tins = second_day_tins - 50
    remaining_days = 4

    # Calculate the total number of tins collected on the first three days
    total_first_three_days = first_day_tins + second_day_tins + third_day_tins

    # Calculate the total number of tins left to collect
    remaining_tins = total_tins - total_first_three_days

    # Calculate the number of tins collected per day on the remaining days
    num_tins_per_day = remaining_tins / remaining_days
    result = num_tins_per_day
    return result

print(solution())