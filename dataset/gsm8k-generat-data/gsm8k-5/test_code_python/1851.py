def solution():
    tomato_rows = 5 # Aubrey is planting one row of tomatoes for every two rows of cucumbers
    cucumber_rows = 10 # Aubrey is planting two rows of cucumbers for every one row of tomatoes
    total_rows = 15 # Aubrey has enough room for 15 rows in total
    plants_per_row = 8 # There are 8 tomato plants per row
    tomatoes_per_plant = 3 # Each tomato plant produces 3 tomatoes

    # Calculate the total number of tomato plants
    total_tomato_plants = tomato_rows * plants_per_row

    # Calculate the total number of tomatoes
    total_tomatoes = total_tomato_plants * tomatoes_per_plant
    result = total_tomatoes
    return result

print(solution())