def solution():
    # Calculate the total amount of oats needed per horse per day
    oats_per_day = 4 * 2

    # Calculate the total amount of grain needed per horse per day
    grain_per_day = 3

    # Calculate the total amount of food needed per horse per day
    total_per_day = oats_per_day + grain_per_day

    # Calculate the total amount of food needed for all four horses per day
    total_per_day_all_horses = total_per_day * 4

    # Calculate the total amount of food needed for all four horses for three days
    total_for_3_days = total_per_day_all_horses * 3
    result = total_for_3_days
    return result

print(solution())