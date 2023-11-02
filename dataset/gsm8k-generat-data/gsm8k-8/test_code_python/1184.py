def solution():
    # Define the number of rows and seeds per row for the top and medium beds
    top_bed_rows = 4
    top_bed_seeds_per_row = 25
    medium_bed_rows = 3
    medium_bed_seeds_per_row = 20

    # Calculate the total number of seeds for the top and medium beds
    top_bed_seeds = top_bed_rows * top_bed_seeds_per_row
    medium_bed_seeds = medium_bed_rows * medium_bed_seeds_per_row

    # Calculate the total number of seeds for all four beds
    total_seeds = 2 * (top_bed_seeds + medium_bed_seeds)
    result = total_seeds
    return result

print(solution())