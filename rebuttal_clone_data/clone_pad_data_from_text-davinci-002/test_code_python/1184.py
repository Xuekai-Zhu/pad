def solution():
    top_bed_rows = 4
    top_bed_seeds_per_row = 25
    top_bed_total_seeds = top_bed_rows * top_bed_seeds_per_row
    
    bottom_bed_rows = 3
    bottom_bed_seeds_per_row = 20
    bottom_bed_total_seeds = bottom_bed_rows * bottom_bed_seeds_per_row
    
    total_seeds = top_bed_total_seeds + bottom_bed_total_seeds
    
    result = total_seeds
    return result

print(solution())