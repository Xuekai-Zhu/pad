def solution():
    num_horses = 4
    oats_per_horse = 4
    meals_per_day = 2
    num_days = 3

    # Calculate the total amount of oats needed per horse for one day
    oats_per_day_per_horse = oats_per_horse * meals_per_day

    # Calculate the total amount of oats needed for all horses for one day
    total_oats_per_day = num_horses * oats_per_day_per_horse

    # Calculate the total amount of oats needed for all horses for three days
    total_oats = total_oats_per_day * num_days
    result = total_oats
    return result

print(solution())