def solution():
    """Aubrey is planting tomatoes and cucumbers in her garden. For each row of tomato plants, she is planting 2 rows of cucumbers. She has enough room for 15 rows of plants in total. There is enough space for 8 tomato plants in each row. If each plant produces 3 tomatoes, how many tomatoes will she have in total?"""
    tomato_rows = 5  # half of the 15 rows will be used for tomato plants
    cucumber_rows = 10  # the remaining 10 rows will be used for cucumber plants
    plants_per_tomato_row = 8
    total_tomato_plants = tomato_rows * plants_per_tomato_row
    tomatoes_per_plant = 3
    total_tomatoes = total_tomato_plants * tomatoes_per_plant
    result = total_tomatoes
    return result

print(solution())