def solution():
    num_rows = 30
    num_plants_per_row = 10
    num_tomatoes_per_plant = 20

    # Calculate the total number of plants
    total_plants = num_rows * num_plants_per_row

    # Calculate the total number of tomatoes
    total_tomatoes = total_plants * num_tomatoes_per_plant
    result = total_tomatoes
    return result

print(solution())