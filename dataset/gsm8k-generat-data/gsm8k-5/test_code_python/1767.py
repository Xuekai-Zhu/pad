def solution():
    total_rows = 20  # Juvy's garden has 20 rows
    plants_per_row = 10  # Each row has 10 plants
    parsley_rows = 3  # Juvy plants parsley in the first 3 rows
    rosemary_rows = 2  # Juvy plants rosemary in the last 2 rows

    # Calculate the total number of parsley and rosemary plants
    parsley_plants = parsley_rows * plants_per_row
    rosemary_plants = rosemary_rows * plants_per_row
    total_herbs_planted = parsley_plants + rosemary_plants

    # Calculate the number of chive plants to be planted
    chive_rows = total_rows - parsley_rows - rosemary_rows
    chive_plants = chive_rows * plants_per_row
    result = chive_plants
    return result

print(solution())