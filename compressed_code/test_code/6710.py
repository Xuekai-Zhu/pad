def solution():
    
    top_bed_rows = 4
    top_bed_seeds_per_row = 25
    medium_bed_rows = 3
    medium_bed_seeds_per_row = 20
    total_seeds_in_top_bed = top_bed_rows * top_bed_seeds_per_row
    total_seeds_in_medium_bed = medium_bed_rows * medium_bed_seeds_per_row
    total_seeds_in_all_beds = 2 * (total_seeds_in_top_bed + total_seeds_in_medium_bed)
    result = total_seeds_in_all_beds
    return result

print(solution())