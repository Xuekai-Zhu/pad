def solution():
    
    total_rows = 20
    parsley_rows = 3
    rosemary_rows = 2
    chive_rows = total_rows - parsley_rows - rosemary_rows
    plants_per_row = 10
    chives_planted = chive_rows * plants_per_row
    result = chives_planted
    return result

print(solution())