def solution():
    num_bean_seedlings = 64
    bean_seedlings_per_row = 8
    num_pumpkin_seeds = 84
    pumpkin_seeds_per_row = 7
    num_radishes = 48
    radishes_per_row = 6
    rows_per_bed = 2

    # Calculate the number of rows for the bean seedlings
    bean_rows = num_bean_seedlings / bean_seedlings_per_row

    # Calculate the number of rows for the pumpkin seeds
    pumpkin_rows = num_pumpkin_seeds / pumpkin_seeds_per_row

    # Calculate the number of rows for the radishes
    radish_rows = num_radishes / radishes_per_row

    # Calculate the total number of rows
    total_rows = bean_rows + pumpkin_rows + radish_rows

    # Calculate the number of plant beds needed
    num_beds = total_rows / rows_per_bed
    result = num_beds
    return result

print(solution())