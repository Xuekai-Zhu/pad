def solution():
    """Aubrey is planting tomatoes and cucumbers in her garden. For each row of tomato plants, she is planting 2 rows of cucumbers. She has enough room for 15 rows of plants in total. There is enough space for 8 tomato plants in each row. If each plant produces 3 tomatoes, how many tomatoes will she have in total?"""
    # Calculate the number of rows of tomato plants
    tomato_rows = 5
    # Calculate the number of rows of cucumber plants
    cucumber_rows = 2 * tomato_rows
    # Calculate the total number of plants
    total_plants = 8 * (tomato_rows + cucumber_rows)
    # Calculate the total number of tomatoes
    total_tomatoes = 3 * (8 * tomato_rows)
    # Display the total number of tomatoes
    result = total_tomatoes
    return result

print(solution())