def solution():
    
    total_rows = 20
    parsley_rows = 3
    rosemary_rows = 2
    chive_rows = total_rows - parsley_rows - rosemary_rows
    plants_per_row = 10
    chive_plants = chive_rows * plants_per_row
    result = chive_plants
    return result

print(solution())