def solution():
    # Calculate the number of rows of tomato and cucumber plants
    tomato_rows = 5
    cucumber_rows = 2 * tomato_rows

    # Calculate the total number of plants
    total_plants = tomato_rows + cucumber_rows

    # Calculate the total number of tomato plants
    total_tomato_plants = tomato_rows * 8

    # Calculate the total number of tomatoes
    total_tomatoes = total_tomato_plants * 3

    result = total_tomatoes
    return result

print(solution())