def solution():
    tomato_rows = 5
    cucumber_rows = 10
    plants_per_row = 8
    tomatoes_per_plant = 3

    # Calculate the total number of tomato plants
    total_tomato_plants = tomato_rows * plants_per_row

    # Calculate the total number of tomatoes
    total_tomatoes = total_tomato_plants * tomatoes_per_plant
    result = total_tomatoes
    return result

print(solution())