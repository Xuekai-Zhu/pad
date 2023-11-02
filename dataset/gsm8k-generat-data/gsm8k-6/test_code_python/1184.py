def solution():
    # Calculate the number of seeds Grace can plant in the top bed
    top_bed_seeds = 4 * 25  # 4 rows with 25 seeds per row
    # Calculate the number of seeds Grace can plant in the medium bed
    medium_bed_seeds = 3 * 20  # 3 rows with 20 seeds per row
    # Calculate the total number of seeds Grace can plant in all four beds
    total_seeds = (top_bed_seeds * 2) + (medium_bed_seeds * 2)  # 2 large beds on top and 2 medium beds on the bottom
    result = total_seeds
    return result

print(solution())