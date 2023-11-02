def solution():
    """Aubrey is planting tomatoes and cucumbers in her garden. For each row of tomato plants, she is planting 2 rows of cucumbers. She has enough room for 15 rows of plants in total. There is enough space for 8 tomato plants in each row. If each plant produces 3 tomatoes, how many tomatoes will she have in total?"""
    # Define the number of rows of tomato plants and cucumber plants
    tomato_rows = 5
    cucumber_rows = 10

    # Define the number of tomato plants in each row
    tomato_plants_per_row = 8

    # Calculate the total number of tomato plants
    total_tomato_plants = tomato_rows * tomato_plants_per_row

    # Calculate the total number of tomatoes produced
    total_tomatoes = total_tomato_plants * 3

    # return the result
    result = total_tomatoes
    return result

print(solution())