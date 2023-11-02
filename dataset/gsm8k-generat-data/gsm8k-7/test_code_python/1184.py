def solution():
    top_bed_rows = 4
    top_bed_seeds_per_row = 25
    medium_bed_rows = 3
    medium_bed_seeds_per_row = 20

    # Calculate the total number of seeds in the top bed
    top_bed_seeds = top_bed_rows * top_bed_seeds_per_row

    # Calculate the total number of seeds in the medium bed
    medium_bed_seeds = medium_bed_rows * medium_bed_seeds_per_row

    # Calculate the total number of seeds in both beds
    total_seeds = top_bed_seeds + medium_bed_seeds

    # Double the total number of seeds to account for both raised beds
    total_seeds *= 2

    result = total_seeds
    return result

print(solution())