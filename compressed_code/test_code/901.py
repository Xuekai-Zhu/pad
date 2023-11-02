def solution():
    
    top_bed_rows = 4
    top_bed_seeds_per_row = 25
    medium_bed_rows = 3
    medium_bed_seeds_per_row = 20
    top_bed_capacity = top_bed_rows * top_bed_seeds_per_row
    medium_bed_capacity = medium_bed_rows * medium_bed_seeds_per_row
    total_capacity = 2 * top_bed_capacity + 2 * medium_bed_capacity
    result = total_capacity
    return result

print(solution())