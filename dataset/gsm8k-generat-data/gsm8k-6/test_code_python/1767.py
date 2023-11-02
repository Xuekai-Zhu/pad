def solution():
    # Calculate the total number of plants in the garden
    total_plants = 20 * 10  # 20 rows with 10 plants in each row
    parsley_rows = 3
    rosemary_rows = 2
    chives_rows = 20 - parsley_rows - rosemary_rows  # calculate the number of rows that will be planted with chives
    chives_plants = chives_rows * 10  # calculate the total number of chives plants
    result = chives_plants
    return result

print(solution())