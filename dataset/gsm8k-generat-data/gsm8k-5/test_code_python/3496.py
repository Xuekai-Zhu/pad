def solution():
    rows_of_tomatoes = 30  # The farmer planted 30 rows of tomatoes
    plants_per_row = 10  # There are 10 plants in each row
    tomatoes_per_plant = 20  # Each tomato plant yields 20 pieces of tomatoes

    # Calculate the total number of tomato plants
    total_plants = rows_of_tomatoes * plants_per_row

    # Calculate the total number of tomatoes
    total_tomatoes = total_plants * tomatoes_per_plant
    result = total_tomatoes
    return result

print(solution())