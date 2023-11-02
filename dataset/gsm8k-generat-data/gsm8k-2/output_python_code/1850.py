def solution():
    """Aubrey is planting tomatoes and cucumbers in her garden. For each row of tomato plants, she is planting 2 rows of cucumbers. She has enough room for 15 rows of plants in total. There is enough space for 8 tomato plants in each row. If each plant produces 3 tomatoes, how many tomatoes will she have in total?"""
    tomato_rows = 5  # since 2 rows of cucumbers for each tomato row, total rows = 3x tomato rows = 15
    plants_per_row = 8
    plants_per_tomato_row = plants_per_row
    plants_per_cucumber_row = plants_per_row * 2
    total_tomato_plants = tomato_rows * plants_per_tomato_row
    total_cucumber_plants = (tomato_rows * 2) * plants_per_cucumber_row  # double the rows of tomatoes
    total_tomatoes = total_tomato_plants * 3
    result = total_tomatoes
    return result

print(solution())