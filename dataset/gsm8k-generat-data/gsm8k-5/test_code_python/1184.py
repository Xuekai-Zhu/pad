def solution():
    seeds_per_row_top = 25  # Each row in the top bed can hold 25 seeds
    seeds_per_row_med = 20  # Each row in the medium bed can hold 20 seeds
    rows_per_top_bed = 4  # The top bed can hold 4 rows of lettuce
    rows_per_med_bed = 3  # The medium bed can hold 3 rows of lettuce
    total_seeds_top_bed = seeds_per_row_top * rows_per_top_bed  # Total number of seeds in the top bed
    total_seeds_med_bed = seeds_per_row_med * rows_per_med_bed  # Total number of seeds in the medium bed
    total_seeds_raised_bed = 2 * (total_seeds_top_bed + total_seeds_med_bed)  # Total number of seeds in both beds
    result = total_seeds_raised_bed
    return result

print(solution())