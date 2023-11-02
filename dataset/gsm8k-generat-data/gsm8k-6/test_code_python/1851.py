def solution():
    # Calculate the number of rows of tomato plants and cucumber plants
    tomato_rows = 5  # she plants 1 row of tomato plants for every 2 rows of cucumber plants
    cucumber_rows = tomato_rows * 2  # for each row of tomato plants, she plants 2 rows of cucumber plants

    # Calculate the total number of tomato plants and cucumber plants
    total_plants = tomato_rows + cucumber_rows
    total_tomato_plants = tomato_rows * 8  # there are 8 tomato plants in each row

    # Calculate the total number of tomatoes
    total_tomatoes = total_tomato_plants * 3  # each plant produces 3 tomatoes

    result = total_tomatoes
    return result

print(solution())