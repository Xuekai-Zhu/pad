def solution():
    total_rows = 20
    plants_per_row = 10
    parsley_rows = 3
    rosemary_rows = 2

    # Calculate the total number of plants for parsley and rosemary
    parsley_plants = parsley_rows * plants_per_row
    rosemary_plants = rosemary_rows * plants_per_row

    # Calculate the total number of plants in the garden
    total_plants = total_rows * plants_per_row

    # Calculate the number of chives plants
    chives_plants = total_plants - parsley_plants - rosemary_plants
    result = chives_plants
    return result

print(solution())